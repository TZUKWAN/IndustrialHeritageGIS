/**
 * 工业文化遗产GIS智能体 — 遗产详情抽屉
 * 概览 / 历史故事 / 时间线 / 核心物项 / 关系与谱系 / 资料来源 / 数据质量
 * 复用 OpenGIS 玻璃浮层样式(与 FeatureAttributePanel 同族), 不遮挡地图主体。
 */
import { useMemo, useState } from 'react'
import {
  AlertTriangle,
  ExternalLink,
  Factory,
  FileText,
  Link2,
  Loader2,
  ShieldCheck,
  X,
} from 'lucide-react'
import { useT } from '@/i18n'
import { useHeritageStore } from '@/stores/heritageStore'
import { INDUSTRY_COLORS } from '@/services/heritage/heritageLayer'
import {
  eventsOf,
  peekDetail,
  sourcesOf,
} from '@/services/heritage/heritageService'
import profilesRaw from '@/data/heritage/profiles.json'
import relationsRaw from '@/data/heritage/relations.json'
import type { HeritageProfile, HeritageRelation } from '@/services/heritage/types'

const profiles = profilesRaw as unknown as Record<string, HeritageProfile>
const relations = relationsRaw as unknown as HeritageRelation[]

type Tab = 'overview' | 'story' | 'timeline' | 'core' | 'relations' | 'sources' | 'quality'

export function HeritageDetailPanel(): JSX.Element | null {
  const t = useT()
  const visible = useHeritageStore((s) => s.detailPanelVisible)
  const selectedId = useHeritageStore((s) => s.selectedId)
  const detail = useHeritageStore((s) => s.detail)
  const loading = useHeritageStore((s) => s.detailLoading)
  const close = () => useHeritageStore.getState().select(null)
  const [tab, setTab] = useState<Tab>('overview')

  const site = detail ?? (selectedId ? peekDetail(selectedId) : null)
  if (!visible || !selectedId || !site) return null

  const profile = profiles[selectedId]
  const events = useMemo(() => eventsOf(selectedId), [selectedId])
  const siteRelations = relations.filter((r) => r.source_entity === selectedId)
  const sourceIds = useMemo(() => {
    const ids = new Set<string>(site.source_ids ?? [])
    events.forEach((e) => e.source_ids.forEach((id) => ids.add(id)))
    return sourcesOf([...ids])
  }, [selectedId, events, site.source_ids])

  const tabs: { key: Tab; label: string }[] = [
    { key: 'overview', label: t.heritage.overview },
    { key: 'story', label: t.heritage.story },
    { key: 'timeline', label: t.heritage.timeline },
    { key: 'core', label: t.heritage.coreItems },
    { key: 'relations', label: t.heritage.relations },
    { key: 'sources', label: t.heritage.sourcesTab },
    { key: 'quality', label: t.heritage.qualityTab },
  ]

  return (
    <div className="absolute top-3 right-3 bottom-14 w-[360px] max-w-[80%] z-20 glass rounded-lg border border-border flex flex-col overflow-hidden">
      {/* 头部 */}
      <div className="px-3 py-2 border-b border-border flex items-start gap-2">
        <Factory
          className="w-4 h-4 mt-0.5 shrink-0"
          style={{ color: INDUSTRY_COLORS[site.industry_category_l1] ?? '#9ca3af' }}
        />
        <div className="min-w-0 flex-1">
          <div className="font-semibold text-sm truncate">{site.name}</div>
          <div className="text-[10px] text-text-muted truncate">
            {site.province}
            {site.city ? ` ${site.city}` : ''}
            {site.district_county ? ` ${site.district_county}` : ''} · 第{site.initial_batch}批 ·{' '}
            {site.industry_category_l1}
          </div>
        </div>
        <button onClick={close} className="text-text-secondary hover:text-text-primary shrink-0">
          <X className="w-4 h-4" />
        </button>
      </div>

      {/* Tab 栏 */}
      <div className="px-2 py-1 border-b border-border flex gap-1 overflow-x-auto shrink-0">
        {tabs.map((tb) => (
          <button
            key={tb.key}
            onClick={() => setTab(tb.key)}
            className={`px-2 py-1 rounded text-[11px] whitespace-nowrap transition-colors ${
              tab === tb.key
                ? 'bg-accent-primary/20 text-accent-primary'
                : 'text-text-secondary hover:text-text-primary'
            }`}
          >
            {tb.label}
          </button>
        ))}
      </div>

      {/* 内容 */}
      <div className="flex-1 overflow-y-auto px-3 py-2 space-y-3 text-xs leading-relaxed">
        {loading && !site && (
          <div className="flex items-center gap-2 text-text-secondary">
            <Loader2 className="w-4 h-4 animate-spin" /> …
          </div>
        )}

        {tab === 'overview' && (
          <>
            <Info label={t.heritage.recognition}>
              {site.batches.map((b) => `第${b}批`).join('、')}
              {site.recognition_years?.length ? `（${site.recognition_years.join('/')}）` : ''}
            </Info>
            <Info label={t.heritage.founded}>
              {site.founded_year ?? '—'}
              {site.founded_year ? `（${site.founded_year_precision ?? 'year'}）` : ''}
            </Info>
            <Info label={t.heritage.production}>{site.production_start_year ?? '—'}</Info>
            <Info label={t.heritage.closure}>{site.closure_year ?? '—'}</Info>
            <Info label={t.heritage.location}>
              {site.address_raw}
            </Info>
            {site.current_use && <Info label={t.heritage.currentUse}>{site.current_use}</Info>}
            {site.aliases?.length > 0 && (
              <Info label={t.heritage.aliases}>{site.aliases.join('、')}</Info>
            )}
            <Info label={t.heritage.period}>
              {site.historical_period?.length ? site.historical_period.join('、') : '—'}
            </Info>
            {profile && (
              <p className="pt-1 border-t border-border">{profile.overview}</p>
            )}
          </>
        )}

        {tab === 'story' && (
          <>
            {profile?.origin_story && <Section title={t.heritage.story}>{profile.origin_story}</Section>}
            {profile?.development_story && (
              <Section title={t.heritage.timeline}>{profile.development_story}</Section>
            )}
            {profile?.transformation_story && (
              <Section title={t.heritage.currentUse}>{profile.transformation_story}</Section>
            )}
            {profile?.recognition_story && (
              <Section title={t.heritage.recognition}>{profile.recognition_story}</Section>
            )}
            {!profile?.origin_story && !profile?.development_story && (
              <div className="glass rounded-md p-2 text-text-secondary">{t.heritage.noStory}</div>
            )}
          </>
        )}

        {tab === 'timeline' && (
          <div className="relative pl-4 space-y-3">
            <div className="absolute left-1 top-1 bottom-1 w-px bg-border" />
            {events.length === 0 && (
              <div className="text-text-secondary">{t.heritage.noStory}</div>
            )}
            {events.map((e) => (
              <div key={e.event_id} className="relative">
                <span className="absolute -left-[11px] top-1 w-2 h-2 rounded-full bg-accent-primary" />
                <div className="flex items-center gap-1.5 flex-wrap">
                  <span className="font-medium">
                    {e.event_date_start || '—'}
                    {e.date_precision && e.date_precision !== 'exact_date' && (
                      <span className="text-text-muted font-normal">
                        {' '}
                        ({e.date_precision})
                      </span>
                    )}
                  </span>
                  <span className="px-1 rounded bg-bg-hover text-[10px] text-text-secondary">
                    {e.event_type}
                  </span>
                  {e.disputed && (
                    <span className="flex items-center gap-0.5 text-[10px] text-amber-400">
                      <AlertTriangle className="w-3 h-3" /> {t.heritage.disputed}
                    </span>
                  )}
                </div>
                <div className="font-medium mt-0.5">{e.title}</div>
                {e.description && (
                  <div className="text-text-secondary">
                    {e.description}
                    {e.source_ids.length > 0 && (
                      <span className="text-text-muted">［{e.source_ids.join('；')}］</span>
                    )}
                  </div>
                )}
              </div>
            ))}
          </div>
        )}

        {tab === 'core' && (
          <>
            <p className="whitespace-pre-wrap">{site.core_items_raw || t.heritage.noCoreItems}</p>
          </>
        )}

        {tab === 'relations' && (
          <>
            {siteRelations.length === 0 && (
              <div className="glass rounded-md p-2 text-text-secondary">{t.heritage.noRelations}</div>
            )}
            {siteRelations.map((r) => (
              <div key={r.relation_id} className="glass rounded-md p-2 space-y-0.5">
                <div className="flex items-center gap-1.5">
                  <Link2 className="w-3 h-3 text-accent-primary" />
                  <span className="font-medium">{r.relation_type}</span>
                  {r.inferred && (
                    <span className="text-[10px] text-amber-400">inferred</span>
                  )}
                </div>
                <div>{r.target_entity}</div>
                {r.description && (
                  <div className="text-text-secondary">
                    {r.description}
                    <span className="text-text-muted">［{r.source_ids.join('；')}］</span>
                  </div>
                )}
              </div>
            ))}
            {profile?.people && profile.people.length > 0 && (
              <Section title="人物">
                {profile.people.map((p) => (
                  <div key={p.name}>
                    {p.name}（{p.roles.join('、')}）［{p.source_ids.join('；')}］
                  </div>
                ))}
              </Section>
            )}
          </>
        )}

        {tab === 'sources' && (
          <>
            {sourceIds.length === 0 && (
              <div className="text-text-secondary">{t.heritage.sourceNone}</div>
            )}
            {sourceIds.map((s) => (
              <div key={s.source_id} className="glass rounded-md p-2 space-y-0.5">
                <div className="flex items-center gap-1.5">
                  <FileText className="w-3 h-3 shrink-0 text-accent-primary" />
                  <span className="font-medium">{s.title || s.source_id}</span>
                </div>
                <div className="text-text-secondary">
                  {s.publisher || s.organization || ''}
                  {s.publication_date ? ` · ${s.publication_date}` : ''}
                </div>
                <div className="flex items-center gap-2 text-[10px] text-text-muted">
                  <span>
                    {s.source_id} · {t.heritage.authority} {s.authority_level}
                  </span>
                  {s.accessed_at && <span>{t.heritage.accessed} {s.accessed_at.slice(0, 10)}</span>}
                </div>
                {s.url && (
                  <a
                    href={s.url}
                    target="_blank"
                    rel="noreferrer"
                    className="flex items-center gap-1 text-accent-primary hover:underline break-all"
                  >
                    <ExternalLink className="w-3 h-3 shrink-0" />
                    <span className="truncate">{s.url}</span>
                  </a>
                )}
                {s.notes && <div className="text-[10px] text-text-muted">{s.notes}</div>}
              </div>
            ))}
          </>
        )}

        {tab === 'quality' && (
          <>
            <div className="glass rounded-md p-2 space-y-1">
              <div className="flex items-center gap-1.5 font-medium">
                <ShieldCheck className="w-3.5 h-3.5 text-accent-primary" />
                {t.heritage.qualityTab}
              </div>
              <div className="text-text-secondary">
                {t.heritage.qualityGeo.replace('{p}', site.geocode_precision ?? '—')}
              </div>
              {site.needs_review?.geocode && (
                <div className="flex items-start gap-1.5 text-amber-400">
                  <AlertTriangle className="w-3.5 h-3.5 shrink-0 mt-0.5" />
                  <span>{t.heritage.geoReviewTag}{site.geocode_note ? `: ${site.geocode_note}` : ''}</span>
                </div>
              )}
              {events.some((e) => e.disputed) && (
                <div className="flex items-start gap-1.5 text-amber-400">
                  <AlertTriangle className="w-3.5 h-3.5 shrink-0 mt-0.5" />
                  <span>{t.heritage.reviewEvents}</span>
                </div>
              )}
              {!site.needs_review?.geocode && !events.some((e) => e.disputed) && (
                <div className="text-text-secondary">{t.heritage.qualityOk}</div>
              )}
              {site.enrichment_status !== 'verified' && (
                <div className="text-text-secondary">{t.heritage.noStory}</div>
              )}
              <div className="text-[10px] text-text-muted pt-1 border-t border-border">
                {t.heritage.dataVersion}: {site.data_version} · heritage_id {site.heritage_id}
              </div>
            </div>
          </>
        )}
      </div>
    </div>
  )
}

function Info(props: { label: string; children: React.ReactNode }): JSX.Element {
  return (
    <div className="flex gap-2">
      <span className="text-text-secondary shrink-0 w-16">{props.label}</span>
      <span className="min-w-0">{props.children}</span>
    </div>
  )
}

function Section(props: { title: string; children: React.ReactNode }): JSX.Element {
  return (
    <div className="glass rounded-md p-2 space-y-1">
      <div className="font-medium text-text-secondary">{props.title}</div>
      <div>{props.children}</div>
    </div>
  )
}
