/**
 * 工业文化遗产GIS智能体 — 侧栏面板
 * 遗产列表 + 筛选 + 分析面板。沿用 OpenGIS 玻璃面板视觉语言。
 */
import { useMemo, useState } from 'react'
import {
  BarChart3,
  List,
  MapPin,
  Play,
  RotateCcw,
  Search,
} from 'lucide-react'
import { useT } from '@/i18n'
import { mapEngine } from '@/features/map/engine/MapEngine'
import {
  PERIOD_TAGS,
  countBy,
  filterSites,
  filtersAreDefault,
  industriesOf,
  provincesOf,
  sites as allSites,
  analysisMeta,
} from '@/services/heritage/heritageService'
import { INDUSTRY_COLORS } from '@/services/heritage/heritageLayer'
import { toggleAnalysisLayer } from './heritageBootstrap'
import {
  HERITAGE_KDE_LAYER_ID,
  HERITAGE_PROVINCE_LAYER_ID,
} from '@/services/heritage/heritageService'
import annRaw from '@/data/heritage/analysis/ann_stats.json'
import moranRaw from '@/data/heritage/analysis/moran_stats.json'
import kdeMetaRaw from '@/data/heritage/analysis/kde_meta.json'
import { useHeritageStore } from '@/stores/heritageStore'
import type { AnnResult, MoranResult, KdeMeta } from '@/services/heritage/types'

const ann = (annRaw as { result: AnnResult }).result
const moran = (moranRaw as { result: MoranResult }).result
const kdeMeta = kdeMetaRaw as unknown as KdeMeta

const BATCHES = [1, 2, 3, 4, 5, 6, 7]

export function HeritagePanel(): JSX.Element {
  const t = useT()
  const [query, setQuery] = useState('')
  const filters = useHeritageStore((s) => s.filters)
  const setFilters = useHeritageStore((s) => s.setFilters)
  const resetFilters = useHeritageStore((s) => s.resetFilters)
  const select = useHeritageStore((s) => s.select)
  const selectedId = useHeritageStore((s) => s.selectedId)
  const panelView = useHeritageStore((s) => s.panelView)
  const setPanelView = useHeritageStore((s) => s.setPanelView)

  const filtered = useMemo(
    () => filterSites(allSites, { ...filters, text: query }),
    [filters, query],
  )
  const provinces = useMemo(() => provincesOf(allSites), [])
  const industries = useMemo(() => industriesOf(allSites), [])

  const locate = (id: string) => {
    const s = allSites.find((x) => x.heritage_id === id)
    select(id)
    if (s?.longitude != null && s.latitude != null) {
      try {
        mapEngine.flyTo([s.longitude, s.latitude], 11, { duration: 800 })
      } catch {
        // 地图未就绪时忽略
      }
    }
  }

  return (
    <div className="flex flex-col h-full text-xs text-text-primary">
      <div className="mx-2 mt-2 rounded-md border border-accent-primary/30 bg-accent-primary/10 px-2 py-1.5 text-[11px] text-text-secondary">
        <span className="font-medium text-accent-primary">{t.heritage.scopeBanner}</span>
        <span className="ml-1">{analysisMeta.scope ?? '湖北省'} · {analysisMeta.site_count}处 · {t.heritage.culturalArchive} · {t.heritage.inventoryCount.replace('{n}', String(analysisMeta.inventory_count ?? 0))}</span>
      </div>
      {/* 视图切换 */}
      <div className="flex items-center gap-1 px-2 pt-2 pb-1">
        <button
          onClick={() => setPanelView('list')}
          className={`flex-1 flex items-center justify-center gap-1 rounded-md py-1.5 transition-colors ${
            panelView === 'list'
              ? 'bg-accent-primary/20 text-accent-primary'
              : 'text-text-secondary hover:text-text-primary'
          }`}
        >
          <List className="w-3.5 h-3.5" /> {t.heritage.list}
        </button>
        <button
          onClick={() => setPanelView('analysis')}
          className={`flex-1 flex items-center justify-center gap-1 rounded-md py-1.5 transition-colors ${
            panelView === 'analysis'
              ? 'bg-accent-primary/20 text-accent-primary'
              : 'text-text-secondary hover:text-text-primary'
          }`}
        >
          <BarChart3 className="w-3.5 h-3.5" /> {t.heritage.analysis}
        </button>
      </div>

      {panelView === 'list' ? (
        <>
          {/* 搜索 */}
          <div className="px-2 pb-2">
            <div className="glass rounded-md flex items-center gap-1.5 px-2 py-1.5">
              <Search className="w-3.5 h-3.5 text-text-muted shrink-0" />
              <input
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder={t.heritage.searchPlaceholder}
                className="bg-transparent outline-none w-full text-xs placeholder:text-text-muted"
              />
            </div>
          </div>

          {/* 筛选区 */}
          <div className="px-2 pb-2 space-y-2 border-b border-border">
            <div>
              <div className="text-text-secondary mb-1">{t.heritage.batch}</div>
              <div className="flex flex-wrap gap-1">
                {BATCHES.map((b) => {
                  const on = filters.batches.includes(b)
                  return (
                    <button
                      key={b}
                      onClick={() =>
                        setFilters({
                          batches: on
                            ? filters.batches.filter((x) => x !== b)
                            : [...filters.batches, b],
                        })
                      }
                      className={`px-1.5 py-0.5 rounded border text-[11px] transition-colors ${
                        on
                          ? 'border-accent-primary text-accent-primary bg-accent-primary/10'
                          : 'border-border text-text-secondary hover:text-text-primary'
                      }`}
                    >
                      {b}
                    </button>
                  )
                })}
              </div>
            </div>
            <div className="grid grid-cols-2 gap-2">
              <div>
                <div className="text-text-secondary mb-1">{t.heritage.province}</div>
                <select
                  value={filters.provinces[0] ?? ''}
                  onChange={(e) =>
                    setFilters({ provinces: e.target.value ? [e.target.value] : [] })
                  }
                  className="glass rounded-md px-1.5 py-1 w-full bg-bg-sidebar text-[11px] outline-none"
                >
                  <option value="">{t.heritage.dataAll}</option>
                  {provinces.map((p) => (
                    <option key={p} value={p}>
                      {p}
                    </option>
                  ))}
                </select>
              </div>
              <div>
                <div className="text-text-secondary mb-1">{t.heritage.industry}</div>
                <select
                  value={filters.industries[0] ?? ''}
                  onChange={(e) =>
                    setFilters({ industries: e.target.value ? [e.target.value] : [] })
                  }
                  className="glass rounded-md px-1.5 py-1 w-full bg-bg-sidebar text-[11px] outline-none"
                >
                  <option value="">{t.heritage.dataAll}</option>
                  {industries.map((i) => (
                    <option key={i} value={i}>
                      {i}
                    </option>
                  ))}
                </select>
              </div>
            </div>
            <div>
              <div className="text-text-secondary mb-1">{t.heritage.period}</div>
              <div className="flex flex-wrap gap-1">
                {PERIOD_TAGS.map((p) => {
                  const on = filters.periods.includes(p)
                  return (
                    <button
                      key={p}
                      title={t.heritage.periodHint}
                      onClick={() =>
                        setFilters({
                          periods: on
                            ? filters.periods.filter((x) => x !== p)
                            : [...filters.periods, p],
                        })
                      }
                      className={`px-1.5 py-0.5 rounded border text-[11px] transition-colors ${
                        on
                          ? 'border-accent-primary text-accent-primary bg-accent-primary/10'
                          : 'border-border text-text-secondary hover:text-text-primary'
                      }`}
                    >
                      {p}
                    </button>
                  )
                })}
              </div>
            </div>
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-1">
                {([null, true, false] as const).map((v) => (
                  <button
                    key={String(v)}
                    onClick={() => setFilters({ enrichedOnly: v })}
                    className={`px-1.5 py-0.5 rounded border text-[11px] transition-colors ${
                      filters.enrichedOnly === v
                        ? 'border-accent-primary text-accent-primary bg-accent-primary/10'
                        : 'border-border text-text-secondary hover:text-text-primary'
                    }`}
                  >
                    {v === null ? t.heritage.dataAll : v ? t.heritage.dataVerified : t.heritage.dataPending}
                  </button>
                ))}
              </div>
              {!filtersAreDefault(filters) && (
                <button
                  onClick={resetFilters}
                  className="flex items-center gap-1 text-[11px] text-text-secondary hover:text-accent-primary"
                >
                  <RotateCcw className="w-3 h-3" /> {t.heritage.clearFilters}
                </button>
              )}
            </div>
            <label className="flex items-center gap-1.5 text-[11px] text-text-secondary cursor-pointer">
              <input
                type="checkbox"
                checked={filters.hideLowConfidenceGeo}
                onChange={(e) => setFilters({ hideLowConfidenceGeo: e.target.checked })}
                className="accent-current"
              />
              {t.heritage.hideLowConfGeo}
            </label>
          </div>

          {/* 数量 */}
          <div className="px-2 py-1.5 text-text-secondary">
            {t.heritage.count.replace('{n}', String(filtered.length))}
          </div>

          {/* 列表 */}
          <div className="flex-1 overflow-y-auto px-2 pb-2 space-y-1">
            {filtered.length === 0 && (
              <div className="glass rounded-md px-2 py-3 text-text-secondary text-center">
                {t.heritage.noResults}
              </div>
            )}
            {filtered.map((s) => (
              <button
                key={s.heritage_id}
                onClick={() => locate(s.heritage_id)}
                className={`w-full text-left rounded-md px-2 py-1.5 border transition-colors ${
                  selectedId === s.heritage_id
                    ? 'border-accent-primary bg-accent-primary/10'
                    : 'border-transparent hover:bg-bg-hover/60'
                }`}
              >
                <div className="flex items-center gap-1.5">
                  <span
                    className="w-2 h-2 rounded-full shrink-0"
                    style={{ background: INDUSTRY_COLORS[s.industry_category_l1] ?? '#9ca3af' }}
                  />
                  <span className="truncate font-medium">{s.name}</span>
                </div>
                <div className="flex items-center gap-2 mt-0.5 text-[10px] text-text-muted">
                  <span>第{s.initial_batch}批</span>
                  <span className="truncate">
                    {s.province}
                    {s.city ? `·${s.city}` : ''}
                  </span>
                  <span
                    className="ml-auto shrink-0"
                    style={{ color: INDUSTRY_COLORS[s.industry_category_l1] ?? '#9ca3af' }}
                  >
                    {s.industry_category_l1}
                  </span>
                </div>
              </button>
            ))}
          </div>
        </>
      ) : (
        <HeritageAnalysisView />
      )}
    </div>
  )
}

function HeritageAnalysisView(): JSX.Element {
  const t = useT()
  const byIndustry = useMemo(() => countBy(allSites, (s) => s.industry_category_l1), [])
  const byBatch = useMemo(
    () => countBy(allSites, (s) => `第${s.initial_batch}批`),
    [],
  )
  const maxInd = Math.max(...Object.values(byIndustry))

  return (
    <div className="flex-1 overflow-y-auto px-2 pb-3 space-y-3">
      {/* 分析图层 */}
      <div className="glass rounded-md p-2 space-y-1.5">
        <div className="text-text-secondary">{t.heritage.analysis}</div>
        <label className="flex items-center gap-1.5 cursor-pointer">
          <input
            type="checkbox"
            defaultChecked={false}
            onChange={(e) => toggleAnalysisLayer(HERITAGE_PROVINCE_LAYER_ID, e.target.checked)}
          />
          {t.heritage.provinceLayer}
        </label>
        <label className="flex items-center gap-1.5 cursor-pointer">
          <input
            type="checkbox"
            defaultChecked={false}
            onChange={(e) => toggleAnalysisLayer(HERITAGE_KDE_LAYER_ID, e.target.checked)}
          />
          {t.heritage.kdeLayer}
        </label>
      </div>

      {/* KDE */}
      <div className="glass rounded-md p-2 space-y-1">
        <div className="font-medium">{t.heritage.kdeLayer}</div>
        <div className="text-text-secondary">
          {t.heritage.kdeParams.replace('{bw}', String(Math.round(kdeMeta.bandwidth_m / 1000)))}
        </div>
        <div className="text-text-muted text-[10px]">{t.heritage.sample.replace('{n}', String(ann.n))}</div>
      </div>

      {/* ANN */}
      <div className="glass rounded-md p-2 space-y-1">
        <div className="font-medium flex items-center gap-1">
          <Play className="w-3 h-3" /> {t.heritage.annTitle}
        </div>
        <div className="text-text-secondary">
          {Math.abs(ann.z_score) >= 1.96
            ? t.heritage.annResult.replace('{r}', ann.R.toFixed(3)).replace('{z}', String(ann.z_score))
            : t.heritage.annDescriptive.replace('{r}', ann.R.toFixed(3)).replace('{z}', String(ann.z_score))}
        </div>
        <div className="text-text-muted text-[10px]">{t.heritage.annParams}</div>
      </div>

      {/* Moran */}
      <div className="glass rounded-md p-2 space-y-1">
        <div className="font-medium">{t.heritage.moranTitle}</div>
        <div className="text-text-secondary">
          {moran.I == null
            ? t.heritage.moranUnavailable
            : moran.z_value != null && Math.abs(moran.z_value) > 1.96
              ? t.heritage.annResult.replace('{r}', String(moran.I)).replace('{z}', String(moran.z_value))
              : t.heritage.moranNotSignificant.replace('{z}', String(moran.z_value ?? '-'))}
        </div>
        <div className="text-text-muted text-[10px]">{t.heritage.moranParams}</div>
      </div>

      <div className="glass rounded-md p-2 text-[10px] text-text-muted leading-relaxed">
        <span className="text-text-secondary font-medium">{t.heritage.boundary}：</span>
        {t.heritage.boundaryNote}
      </div>

      {/* 行业构成 */}
      <div className="glass rounded-md p-2 space-y-1.5">
        <div className="text-text-secondary">{t.heritage.industry}</div>
        {Object.entries(byIndustry)
          .sort((a, b) => b[1] - a[1])
          .map(([k, v]) => (
            <div key={k} className="space-y-0.5">
              <div className="flex justify-between text-[11px]">
                <span className="truncate" style={{ color: INDUSTRY_COLORS[k] ?? '#9ca3af' }}>
                  {k}
                </span>
                <span className="text-text-muted">{v}</span>
              </div>
              <div className="h-1 rounded bg-bg-hover overflow-hidden">
                <div
                  className="h-full rounded"
                  style={{
                    width: `${(v / maxInd) * 100}%`,
                    background: INDUSTRY_COLORS[k] ?? '#9ca3af',
                  }}
                />
              </div>
            </div>
          ))}
      </div>

      {/* 批次构成 */}
      <div className="glass rounded-md p-2 space-y-1">
        <div className="text-text-secondary">{t.heritage.batch}</div>
        {Object.entries(byBatch).sort((a, b) => a[0].localeCompare(b[0], 'zh')).map(([k, v]) => (
          <div key={k} className="flex justify-between text-[11px]">
            <span>{k}</span>
            <span className="text-text-muted">{v}</span>
          </div>
        ))}
      </div>

      <div className="flex items-center gap-1 text-[10px] text-text-muted px-1">
        <MapPin className="w-3 h-3" /> data {analysisMeta.data_version} · {analysisMeta.generated_at.slice(0, 10)}
      </div>
    </div>
  )
}
