/**
 * 工业文化遗产GIS智能体 — 地图图层构建
 *
 * 把内置遗产数据包装成 OpenGIS 原生 MapLayerDefinition(分类/分级/栅格渲染器),
 * 使遗产点、省级统计、核密度图层走与其他图层完全一致的同步/过滤/identify 管道。
 */
import kdePng from '@/data/heritage/analysis/kde_raster.png?inline'
import kdeMetaRaw from '@/data/heritage/analysis/kde_meta.json'
import provinceBoundaries from '@/data/heritage/analysis/province_boundaries.geojson'
import type { GeoJSONFeatureCollection } from '@/services/geo'
import type {
  MapLayerDefinition,
  LayerFilterSpec,
  LayerAttributeFilter,
  ParsedVectorData,
  ParsedRasterData,
  FieldDescriptor,
} from '@/services/geo'
import { HERITAGE_LAYER_ID, HERITAGE_PROVINCE_LAYER_ID, HERITAGE_KDE_LAYER_ID, type HeritageFilters } from './heritageService'
import type { HeritageSite, KdeMeta } from './types'

export const kdeMeta = kdeMetaRaw as unknown as KdeMeta

/** 行业一级分类 → 颜色(与 OpenGIS 暗色主题协调的 17 色) */
export const INDUSTRY_COLORS: Record<string, string> = {
  煤炭工业: '#8d6e63',
  石油天然气: '#5d8aa8',
  核工业军工: '#b0574f',
  冶金: '#c0392b',
  金属与非金属采矿: '#d4a017',
  铁路交通: '#46627f',
  船舶工业: '#2e8b8b',
  航空航天: '#7c5cbf',
  电子通信: '#3f7cac',
  电力能源: '#e67e22',
  医药化工: '#9ccc65',
  纺织工业: '#d17ba0',
  食品酿酒: '#f2c14e',
  机械装备: '#6b8e23',
  建材陶瓷: '#95a5a6',
  轻工业: '#c9a227',
  其他: '#9ca3af',
}

export const INDUSTRY_ORDER = Object.keys(INDUSTRY_COLORS)

// ─── 属性打包(标量化以便 MapLibre 表达式/过滤使用) ────────────────

export function siteProps(s: HeritageSite): Record<string, unknown> {
  return {
    heritage_id: s.heritage_id,
    name: s.name,
    batch: s.initial_batch,
    batches_str: s.batches.join('|'),
    province: s.province ?? '',
    city: s.city ?? '',
    district: s.district_county ?? '',
    industry: s.industry_category_l1,
    start_year: s.founded_year ?? s.production_start_year ?? -1,
    end_year: s.closure_year ?? 2026,
    periods_str: (s.historical_period ?? []).join('|'),
    enriched: s.enrichment_status === 'verified' ? 1 : 0,
    geo_review: s.needs_review?.geocode ? 1 : 0,
    completeness: s.field_completeness ?? 0,
  }
}

export function buildSitesGeoJSON(
  rows: HeritageSite[],
): GeoJSONFeatureCollection {
  return {
    type: 'FeatureCollection',
    features: rows
      .filter((s) => s.longitude != null && s.latitude != null)
      .map((s) => ({
        type: 'Feature' as const,
        geometry: { type: 'Point' as const, coordinates: [s.longitude, s.latitude] },
        properties: siteProps(s),
      })),
  }
}

// ─── 字段描述符 ──────────────────────────────────────────────────

function fieldsFromGeoJSON(gj: GeoJSONFeatureCollection): FieldDescriptor[] {
  const first = gj.features[0]?.properties ?? {}
  return Object.keys(first).map((name) => {
    const v = first[name]
    return {
      name,
      type: typeof v === 'number' ? 'number' : typeof v === 'boolean' ? 'boolean' : 'string',
      nullCount: 0,
      sampleValues: [v],
    }
  })
}

// ─── 图层定义 ────────────────────────────────────────────────────

export function buildHeritageLayerDef(
  rows: HeritageSite[],
): MapLayerDefinition {
  const geojson = buildSitesGeoJSON(rows)
  const data: ParsedVectorData = {
    kind: 'vector',
    geojson,
    geometryType: 'Point',
    featureCount: geojson.features.length,
    bbox: { minX: 73, minY: 17, maxX: 136, maxY: 54 },
    crs: 'EPSG:4326',
    fields: fieldsFromGeoJSON(geojson),
  }
  return {
    id: HERITAGE_LAYER_ID,
    name: '国家工业遗产点位',
    sourceType: 'geojson',
    visible: true,
    style: {
      renderType: 'categorized',
      color: '#e67e22',
      opacity: 0.9,
      strokeColor: '#ffffff',
      strokeWidth: 1,
      strokeOpacity: 0.9,
      radius: 6,
      categorized: {
        field: 'industry',
        colors: INDUSTRY_COLORS,
        categories: INDUSTRY_ORDER,
        otherColor: '#9ca3af',
      },
      legend: {
        visible: true,
        title: '行业类别',
        order: INDUSTRY_ORDER,
      },
    },
    data,
    meta: {
      fileName: 'heritage_sites.geojson',
      extension: '.geojson',
      sourceType: 'geojson',
      fileSize: 0,
      mimeType: 'application/geo+json',
    },
    addedAt: Date.now(),
  }
}

export function buildProvinceLayerDef(): MapLayerDefinition {
  const gj = provinceBoundaries as unknown as GeoJSONFeatureCollection
  const data: ParsedVectorData = {
    kind: 'vector',
    geojson: gj,
    geometryType: 'Polygon',
    featureCount: gj.features.length,
    bbox: { minX: 73, minY: 17, maxX: 136, maxY: 54 },
    crs: 'EPSG:4326',
    fields: [
      { name: 'name', type: 'string', nullCount: 0, sampleValues: ['北京市'] },
      { name: 'count', type: 'number', nullCount: 0, sampleValues: [0] },
    ],
  }
  return {
    id: HERITAGE_PROVINCE_LAYER_ID,
    name: '省级行政区遗产统计',
    sourceType: 'geojson',
    visible: true,
    style: {
      renderType: 'graduated',
      color: '#46627f',
      opacity: 0.75,
      strokeColor: '#8fa8c7',
      strokeWidth: 0.8,
      strokeOpacity: 0.7,
      fillOpacity: 0.75,
      graduated: {
        field: 'count',
        method: 'quantile',
        classes: 5,
        palette: ['#12263a', '#1d435f', '#2d6a86', '#4b95ab', '#8fc1c9'],
      },
      legend: { visible: true, title: '省级遗产数量' },
    },
    data,
    meta: {
      fileName: 'province_boundaries.geojson',
      extension: '.geojson',
      sourceType: 'geojson',
      fileSize: 0,
      mimeType: 'application/geo+json',
    },
    addedAt: Date.now(),
  }
}

export function buildKdeLayerDef(): MapLayerDefinition {
  const corners = kdeMeta.extent_wgs84_corners
  const data: ParsedRasterData = {
    kind: 'raster',
    source: 'image',
    imageUrl: kdePng as unknown as string,
    bbox: {
      minX: Math.min(...corners.map((c) => c[0])),
      minY: Math.min(...corners.map((c) => c[1])),
      maxX: Math.max(...corners.map((c) => c[0])),
      maxY: Math.max(...corners.map((c) => c[1])),
    },
    imageCoordinates: [
      [corners[0][0], corners[0][1]],
      [corners[1][0], corners[1][1]],
      [corners[2][0], corners[2][1]],
      [corners[3][0], corners[3][1]],
    ],
    width: kdeMeta.png_size[0],
    height: kdeMeta.png_size[1],
    bandCount: 4,
    crs: 'EPSG:4326',
  }
  return {
    id: HERITAGE_KDE_LAYER_ID,
    name: '核密度估计(KDE)',
    sourceType: 'geojson',
    visible: true,
    style: {
      renderType: 'raster',
      color: '#e67e22',
      opacity: 0.8,
      strokeColor: '#000000',
      strokeWidth: 1,
      raster: { mode: 'rgb', opacity: 0.8 },
    },
    data,
    meta: {
      fileName: 'kde_raster.png',
      extension: '.png',
      sourceType: 'geotiff',
      fileSize: 0,
    },
    addedAt: Date.now(),
  }
}

// ─── 筛选 → LayerFilterSpec(标量属性条件) ────────────────────────

const TEMPORAL_DIM_NOTE = 'temporal'

export function temporalFilterBasisLabel(dim: 'formation' | 'recognition'): string {
  return dim === 'formation' ? '基于已核实的形成/存续年份' : '基于国家工业遗产认定批次年份'
}

/** 遗产筛选 → 图层过滤(只影响地图点显隐; 与列表统计共用同一来源字段) */
export function compileHeritageFilter(
  f: HeritageFilters,
  dim: 'formation' | 'recognition' = 'formation',
): LayerFilterSpec | undefined {
  const attribute: LayerAttributeFilter[] = []
  const anyAttribute: LayerAttributeFilter[] = []

  if (f.batches.length) {
    attribute.push({ field: 'batch', op: 'in', value: f.batches })
  }
  if (f.provinces.length) {
    attribute.push({ field: 'province', op: 'in', value: f.provinces })
  }
  if (f.industries.length) {
    attribute.push({ field: 'industry', op: 'in', value: f.industries })
  }
  if (f.enrichedOnly === true) {
    attribute.push({ field: 'enriched', op: '=', value: 1 })
  } else if (f.enrichedOnly === false) {
    attribute.push({ field: 'enriched', op: '=', value: 0 })
  }
  if (f.hideLowConfidenceGeo) {
    attribute.push({ field: 'geo_review', op: '=', value: 0 })
  }
  if (f.periods.length) {
    // OR: 任一所选历史时期
    for (const p of f.periods) {
      anyAttribute.push({ field: 'periods_str', op: 'contains', value: p })
    }
  }
  if (f.temporal) {
    if (dim === 'formation') {
      // 遗产存续窗口与所选年份区间相交: start<=to AND end>=from
      attribute.push({ field: 'start_year', op: '<=', value: f.temporal.toYear })
      attribute.push({ field: 'end_year', op: '>=', value: f.temporal.fromYear })
    } else {
      const fromY = Math.floor(f.temporal.fromYear)
      const toY = Math.floor(f.temporal.toYear)
      if (fromY === toY) {
        attribute.push({ field: 'batch', op: 'in', value: batchForYear(fromY) })
      } else {
        attribute.push({ field: 'batch', op: 'in', value: batchRange(fromY, toY) })
      }
    }
  }
  if (attribute.length === 0 && anyAttribute.length === 0) return undefined
  return { attribute, anyAttribute }
}

function batchForYear(year: number): number[] {
  const table: [number, number][] = [
    [2017, 1], [2018, 2], [2019, 3], [2020, 4], [2021, 5], [2024, 6], [2025, 7],
  ]
  return table.filter(([, b]) => recognitionYear(b) === year).map(([, b]) => b)
}

function batchRange(fromYear: number, toYear: number): number[] {
  const table: [number, number][] = [
    [2017, 1], [2018, 2], [2019, 3], [2020, 4], [2021, 5], [2024, 6], [2025, 7],
  ]
  return table.filter(([y]) => y >= fromYear && y <= toYear).map(([, b]) => b)
}

export function recognitionYear(batch: number): number {
  const table: Record<number, number> = {
    1: 2017, 2: 2018, 3: 2019, 4: 2020, 5: 2021, 6: 2024, 7: 2025,
  }
  return table[batch]
}

export { TEMPORAL_DIM_NOTE }
