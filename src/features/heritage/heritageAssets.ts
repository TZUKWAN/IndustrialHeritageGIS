/**
 * 工业文化遗产GIS智能体 — 分析产物资产绑定
 * 把 KDE 栅格与省界 GeoJSON 注入图层构建器; 集中在此以便测试与运行时解耦。
 */
import kdePng from '@/data/heritage/analysis/kde_raster.png?inline'
import provinceBoundaries from '@/data/heritage/analysis/province_boundaries.json'
import type { GeoJSONFeatureCollection } from '@/services/geo'
import { buildKdeLayerDef, buildProvinceLayerDef } from '@/services/heritage/heritageLayer'
import type { MapLayerDefinition } from '@/services/geo'

export function makeProvinceLayerDef(): MapLayerDefinition {
  return buildProvinceLayerDef(provinceBoundaries as unknown as GeoJSONFeatureCollection)
}

export function makeKdeLayerDef(): MapLayerDefinition {
  return buildKdeLayerDef(kdePng as unknown as string)
}
