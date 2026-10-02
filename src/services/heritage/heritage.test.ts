/**
 * 工业文化遗产GIS智能体 — 数据访问层与图层构建测试
 */
import { describe, expect, it } from 'vitest'
import fs from 'node:fs'
import path from 'node:path'
import { DEFAULT_FILTERS, filterSites, searchSites, eventsOf, sourcesOf, sites, culturalProfiles } from '@/services/heritage/heritageService'
import { buildHeritageLayerDef, buildSitesGeoJSON, compileHeritageFilter, INDUSTRY_COLORS } from '@/services/heritage/heritageLayer'

describe('heritageService.filterSites', () => {
  it('returns all sites with default filters', () => {
    expect(filterSites(sites, DEFAULT_FILTERS).length).toBe(13)
    expect(sites.every((s) => s.province === '湖北省')).toBe(true)
  })

  it('filters by batch', () => {
    const out = filterSites(sites, { ...DEFAULT_FILTERS, batches: [1] })
    expect(out.length).toBeGreaterThan(0)
    expect(out.every((s) => s.batches.includes(1))).toBe(true)
  })

  it('filters by province and industry', () => {
    const out = filterSites(sites, {
      ...DEFAULT_FILTERS,
      provinces: ['湖北省'],
      industries: ['食品酿酒'],
    })
    expect(out.every((s) => s.province === '湖北省')).toBe(true)
    expect(out.every((s) => s.industry_category_l1 === '食品酿酒')).toBe(true)
  })

  it('temporal filter excludes sites without verified formation year', () => {
    const out = filterSites(sites, {
      ...DEFAULT_FILTERS,
      temporal: { fromYear: 1890, toYear: 1899 },
    })
    expect(out.length).toBeGreaterThan(0)
    for (const s of out) {
      expect(s.founded_year ?? s.production_start_year).toBeTruthy()
    }
    // 汉阳铁厂1890年创办应在窗口内
    expect(out.some((s) => s.name.includes('汉阳铁厂'))).toBe(true)
  })

  it('text filter matches alias/city/event', () => {
    expect(searchSites('武汉').length).toBeGreaterThan(0)
    expect(searchSites('不存在的遗产xyz').length).toBe(0)
  })

  it('hide low confidence geo removes flagged sites', () => {
    const all = filterSites(sites, DEFAULT_FILTERS)
    const out = filterSites(sites, { ...DEFAULT_FILTERS, hideLowConfidenceGeo: true })
    expect(out.length).toBe(all.length)
    expect(out.every((s) => !s.needs_review.geocode)).toBe(true)
  })
})

describe('heritage events/sources', () => {
  it('every site has a recognition event', () => {
    const sample = sites.slice(0, 20)
    for (const s of sample) {
      const evs = eventsOf(s.heritage_id)
      expect(evs.length).toBeGreaterThan(0)
      expect(evs.some((e) => e.event_type === '遗产认定')).toBe(true)
    }
  })

  it('recognition events have A-level official sources', () => {
    const evs = eventsOf(sites[0].heritage_id)
    const rec = evs.find((e) => e.event_type === '遗产认定')!
    const srcs = sourcesOf(rec.source_ids)
    expect(srcs.length).toBeGreaterThan(0)
    expect(srcs.every((s) => s.authority_level === 'A')).toBe(true)
    expect(srcs[0].url).toContain('miit.gov.cn')
  })

  it('pilot sites have verified historical events with sources', () => {
    const hanyang = sites.find((s) => s.name.includes('汉阳铁厂'))!
    const evs = eventsOf(hanyang.heritage_id).filter((e) => e.event_type !== '遗产认定')
    expect(evs.length).toBeGreaterThanOrEqual(5)
    for (const e of evs) {
      expect(e.source_ids.length).toBeGreaterThan(0)
    }
  })
})

describe('heritageLayer', () => {
  it('builds geojson with all geocoded sites and scalar props', () => {
    const gj = buildSitesGeoJSON(sites)
    expect(gj.features.length).toBe(sites.length) // 全部站点均有行政区划中心点坐标
    for (const f of gj.features) {
      expect(typeof f.properties.name).toBe('string')
      expect(typeof f.properties.batch).toBe('number')
    }
  })

  it('builds categorized layer definition in mapStore shape', () => {
    const def = buildHeritageLayerDef(sites)
    expect(def.id).toBe('heritage-sites')
    expect(def.style.renderType).toBe('categorized')
    expect(def.style.categorized?.field).toBe('industry')
    expect(def.data.kind).toBe('vector')
    if (def.data.kind === 'vector') {
      expect(def.data.featureCount).toBe(13)
    }
  })

  it('has a color for every industry category present in data', () => {
    const cats = new Set(sites.map((s) => s.industry_category_l1))
    for (const c of cats) {
      expect(INDUSTRY_COLORS[c]).toBeTruthy()
    }
  })
})

describe('cultural archive', () => {
  it('has one cultural archive for every Hubei site', () => {
    expect(Object.keys(culturalProfiles)).toHaveLength(sites.length)
    for (const site of sites) {
      const profile = culturalProfiles[site.heritage_id]
      expect(profile).toBeTruthy()
      expect(profile.carrier_types.length).toBeGreaterThan(0)
      expect(profile.cultural_dimensions.length).toBeGreaterThanOrEqual(4)
      expect(profile.source_ids.length).toBeGreaterThan(0)
    }
  })
})

describe('filter compilation', () => {
  it('compiles batches to in-condition', () => {
    const spec = compileHeritageFilter({
      ...DEFAULT_FILTERS,
      batches: [1, 3],
    })
    expect(spec?.attribute).toContainEqual({ field: 'batch', op: 'in', value: [1, 3] })
  })

  it('compiles periods to OR (anyAttribute)', () => {
    const spec = compileHeritageFilter({
      ...DEFAULT_FILTERS,
      periods: ['晚清近代工业', '民国时期'],
    })
    expect(spec?.anyAttribute?.length).toBe(2)
  })

  it('compiles temporal window to intersection conditions', () => {
    const spec = compileHeritageFilter({
      ...DEFAULT_FILTERS,
      temporal: { fromYear: 1900, toYear: 1909 },
    })
    expect(spec?.attribute).toContainEqual({ field: 'start_year', op: '<=', value: 1909 })
    expect(spec?.attribute).toContainEqual({ field: 'end_year', op: '>=', value: 1900 })
  })
})

describe('branding (user-visible)', () => {
  it('index.html title is 工业文化遗产GIS智能体', () => {
    const html = fs.readFileSync(
      path.resolve(__dirname, '../../../index.html'),
      'utf-8',
    )
    expect(html).toContain('<title>工业文化遗产GIS智能体</title>')
  })

  it('zh i18n emptyState title is 工业文化遗产GIS智能体', async () => {
    const zh = (await import('@/i18n/zh')).zh as unknown as {
      chat: { emptyState: { title: string } }
    }
    expect(zh.chat.emptyState.title).toBe('工业文化遗产GIS智能体')
  })
})
