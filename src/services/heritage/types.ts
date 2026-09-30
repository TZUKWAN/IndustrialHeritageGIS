/**
 * 工业文化遗产GIS智能体 — 数据类型定义
 *
 * 数据来源: src/data/heritage/*.json (由 data-pipeline/scripts/export_frontend.py 生成)
 * 字段语义见 docs/DATA_DICTIONARY.md
 */

export interface HeritageSite {
  heritage_id: string
  name: string
  aliases: string[]
  initial_batch: number
  batches: number[]
  province: string | null
  city: string | null
  district_county: string
  address_raw: string
  industry_category_l1: string
  core_item_categories: string[]
  longitude: number | null
  latitude: number | null
  geocode_quality: string
  geocode_precision: string | null
  geocode_level: string | null
  needs_review: { geocode: boolean; classification: boolean; duplicate: boolean }
  founded_year: number | null
  founded_year_precision: string | null
  production_start_year: number | null
  closure_year: number | null
  recognition_years: number[]
  historical_period: string[]
  current_use: string | null
  enrichment_status: string
  field_completeness: number
  source_ids: string[]
}

export interface HeritageDetail extends HeritageSite {
  applicant_unit: string
  core_items_raw: string
  classification_basis: { matched_keywords: string[]; name_hit: boolean; basis: string }
  address_components: { district_adcodes: (string | number)[]; district_names: string[] }
  coordinate_system: string | null
  geocode_source: string | null
  geocode_source_crs: string | null
  geocode_gcj02: [number, number] | null
  geocode_adcode: string | number | null
  geocode_note: string
  data_version: string
}

export interface HeritageEvent {
  event_id: string
  heritage_id: string
  event_date_start: string
  event_date_end: string | null
  date_precision: string
  event_type: string
  title: string
  description: string
  place_name: string | null
  related_orgs: string[]
  related_people: string[]
  source_ids: string[]
  confidence: string
  disputed: boolean
  notes: string
}

export interface HeritageRelation {
  relation_id: string
  source_entity: string
  relation_type: string
  target_entity: string
  start_date: string | null
  end_date: string | null
  description: string
  source_ids: string[]
  confidence: string
  inferred: boolean
}

export interface HeritageProfile {
  heritage_id: string
  overview: string
  origin_story: string | null
  development_story: string | null
  transformation_story: string | null
  recognition_story: string | null
  current_use: string | null
  period_tags: string[]
  research_status: string
  generated_from_event_version: string
  note: string | null
  people: { name: string; roles: string[]; source_ids: string[] }[]
}

export interface HeritageSource {
  source_id: string
  source_type: string
  title: string
  publisher?: string
  organization?: string
  author?: string | null
  publication_date?: string | null
  url: string | null
  accessed_at?: string | null
  authority_level: string
  notes: string
  origin_file?: string
  sha256?: string
}

export interface AnalysisMeta {
  data_version: string | null
  generated_at: string
  site_count: number
  event_count: number
  relation_count: number
  source_count: number
  enriched_sites: number
}

export interface AnnResult {
  n: number
  mean_observed_m: number
  mean_random_expected_m: number
  R: number
  z_score: number
  interpretation: string[]
  interpretation_note: string
}

export interface MoranResult {
  I: number
  E_I: number
  z_value: number | null
  n_units: number
  weights: string
}

export interface KdeMeta {
  bandwidth_m: number
  cell_size_m?: number
  grid_shape: number[]
  extent_proj: [number, number, number, number]
  extent_wgs84_corners: [number, number][]
  max_density: number
  png_size: number[]
  kernel: string
  bandwidth_rule: string
  crs_analysis: string
  note: string
  created_at: string
}

/** 地图时间窗过滤用(由服务层从 founded/closure 推导) */
export interface TemporalWindow {
  /** 十进制年份下界(含) */
  fromYear: number
  /** 十进制年份上界(含) */
  toYear: number
}
