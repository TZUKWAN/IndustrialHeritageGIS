/**
 * 工业文化遗产GIS智能体 — 数据访问层
 *
 * 职责:
 *  - 加载内置数据包 (sites 首屏 / details 懒加载并缓存)
 *  - 筛选(批次/省份/行业/历史时期/资料状态/文本) 与统计
 *  - 事件/来源查询
 * 全部为纯函数 + 单例缓存, 便于 vitest 覆盖。
 */
import rawSites from '@/data/heritage/sites.json'
import rawEvents from '@/data/heritage/events.json'
import rawSources from '@/data/heritage/sources.json'
import rawMeta from '@/data/heritage/meta.json'
import type {
  HeritageSite,
  HeritageDetail,
  HeritageEvent,
  HeritageSource,
  AnalysisMeta,
  TemporalWindow,
} from './types'

export const sites = rawSites as unknown as HeritageSite[]
export const events = rawEvents as unknown as HeritageEvent[]
export const sources = rawSources as unknown as HeritageSource[]
export const analysisMeta = rawMeta as unknown as AnalysisMeta

export const HERITAGE_LAYER_ID = 'heritage-sites'
export const HERITAGE_PROVINCE_LAYER_ID = 'heritage-province-stats'
export const HERITAGE_KDE_LAYER_ID = 'heritage-kde'

/** 当前使用的历史时期标签(与 data-pipeline 字典一致) */
export const PERIOD_TAGS = [
  '晚清近代工业',
  '民国时期',
  '新中国初期',
  '一五二五时期',
  '三线建设时期',
  '改革开放后',
] as const

// ─── 详情缓存(懒加载) ────────────────────────────────────────────

let detailsCache: Record<string, HeritageDetail> | null = null
let detailsPromise: Promise<Record<string, HeritageDetail>> | null = null

export async function loadDetails(): Promise<Record<string, HeritageDetail>> {
  if (detailsCache) return detailsCache
  if (!detailsPromise) {
    detailsPromise = import('@/data/heritage/details.json').then((m) => {
      detailsCache = m.default as unknown as Record<string, HeritageDetail>
      return detailsCache
    })
  }
  return detailsPromise
}

export async function getDetail(id: string): Promise<HeritageDetail | null> {
  const d = await loadDetails()
  return d[id] ?? null
}

/** 同步取缓存中的详情(未加载返回 null) */
export function peekDetail(id: string): HeritageDetail | null {
  return detailsCache?.[id] ?? null
}

// ─── 筛选 ────────────────────────────────────────────────────────

export interface HeritageFilters {
  batches: number[]
  provinces: string[]
  industries: string[]
  periods: string[]
  /** null = 全部; true = 只看资料已核实; false = 只看待补充 */
  enrichedOnly: boolean | null
  /** 低置信地理编码同时隐藏 */
  hideLowConfidenceGeo: boolean
  /** 时间窗(基于遗产形成/存续年份, 与认定批次无关) */
  temporal: TemporalWindow | null
  text: string
}

export const DEFAULT_FILTERS: HeritageFilters = {
  batches: [],
  provinces: [],
  industries: [],
  periods: [],
  enrichedOnly: null,
  hideLowConfidenceGeo: false,
  temporal: null,
}

export function filtersAreDefault(f: HeritageFilters): boolean {
  return (
    f.batches.length === 0 &&
    f.provinces.length === 0 &&
    f.industries.length === 0 &&
    f.periods.length === 0 &&
    f.enrichedOnly === null &&
    !f.hideLowConfidenceGeo &&
    f.temporal === null &&
    f.text.trim() === ''
  )
}

/** 遗产存续时间窗(用于时间轴过滤; 无形成年份的用认定年份并如实降级) */
export function siteTemporalBounds(s: HeritageSite): [number, number] | null {
  const start = s.founded_year ?? s.production_start_year
  if (start == null) return null
  const end = s.closure_year ?? 2026
  return [start, Math.max(start, end)]
}

export function filterSites(
  all: HeritageSite[],
  f: HeritageFilters,
): HeritageSite[] {
  const q = f.text.trim().toLowerCase()
  return all.filter((s) => {
    if (f.batches.length && !f.batches.some((b) => s.batches.includes(b))) return false
    if (f.provinces.length && !s.province) return false
    if (f.provinces.length && !f.provinces.includes(s.province as string)) return false
    if (f.industries.length && !f.industries.includes(s.industry_category_l1))
      return false
    if (f.periods.length) {
      if (!f.periods.some((p) => s.historical_period.includes(p))) return false
    }
    if (f.enrichedOnly === true && s.enrichment_status !== 'verified') return false
    if (f.enrichedOnly === false && s.enrichment_status === 'verified') return false
    if (f.hideLowConfidenceGeo) {
      if (s.needs_review?.geocode) return false
      if (!s.longitude || !s.latitude) return false
    }
    if (f.temporal) {
      const tb = siteTemporalBounds(s)
      // 没有形成年份的遗产不参与时间过滤(不冒充)
      if (!tb) return false
      const [a, b] = tb
      if (b < f.temporal.fromYear || a > f.temporal.toYear) return false
    }
    if (q) {
      const hay = [
        s.name,
        ...(s.aliases ?? []),
        s.city ?? '',
        s.province ?? '',
        s.industry_category_l1,
        s.current_use ?? '',
      ]
        .join(' ')
        .toLowerCase()
      if (!hay.includes(q)) return false
    }
    return true
  })
}

// ─── 统计 ────────────────────────────────────────────────────────

export function countBy<T>(items: T[], key: (x: T) => string): Record<string, number> {
  const out: Record<string, number> = {}
  for (const it of items) {
    const k = key(it)
    out[k] = (out[k] ?? 0) + 1
  }
  return out
}

export function provincesOf(all: HeritageSite[]): string[] {
  return Object.keys(countBy(all, (s) => s.province ?? '未知')).sort((a, b) =>
    a.localeCompare(b, 'zh'),
  )
}

export function industriesOf(all: HeritageSite[]): string[] {
  return Object.keys(countBy(all, (s) => s.industry_category_l1)).sort(
    (a, b) => countBy(all, (s) => s.industry_category_l1)[b] -
      countBy(all, (s) => s.industry_category_l1)[a],
  )
}

// ─── 事件/来源 ───────────────────────────────────────────────────

const eventsBySite: Map<string, HeritageEvent[]> = new Map()
for (const e of events) {
  const list = eventsBySite.get(e.heritage_id) ?? []
  list.push(e)
  eventsBySite.set(e.heritage_id, list)
}

export function eventsOf(heritageId: string): HeritageEvent[] {
  return (eventsBySite.get(heritageId) ?? [])
    .slice()
    .sort((a, b) => (a.event_date_start || '9999').localeCompare(b.event_date_start || '9999'))
}

const sourceById: Map<string, HeritageSource> = new Map(
  sources.map((s) => [s.source_id, s]),
)

export function sourceOf(id: string): HeritageSource | undefined {
  return sourceById.get(id)
}

export function sourcesOf(ids: string[]): HeritageSource[] {
  return ids.map((id) => sourceById.get(id)).filter(Boolean) as HeritageSource[]
}

/** 全库检索: 名称/别名/城市/行业/事件关键词 → 命中遗产 */
export function searchSites(query: string, all: HeritageSite[] = sites): HeritageSite[] {
  const q = query.trim().toLowerCase()
  if (!q) return []
  const direct = new Set(
    filterSites(all, { ...DEFAULT_FILTERS, text: q }).map((s) => s.heritage_id),
  )
  for (const e of events) {
    if (
      (e.title && e.title.toLowerCase().includes(q)) ||
      (e.description && e.description.toLowerCase().includes(q))
    ) {
      const s = all.find((x) => x.heritage_id === e.heritage_id)
      if (s) direct.add(s.heritage_id)
    }
  }
  return all.filter((s) => direct.has(s.heritage_id))
}
