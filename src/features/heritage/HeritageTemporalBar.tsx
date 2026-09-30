/**
 * 工业文化遗产GIS智能体 — 地图时间维度控件
 * “形成时间”(已核实始建/投产年份, 子集) 与 “认定时间”(工信部公布年份, 全量) 双维度,
 * 年代滑块 + 播放。筛选结果同步到地图图层与统计。
 */
import { useEffect, useMemo, useRef } from 'react'
import { Info, Pause, Play } from 'lucide-react'
import { useT } from '@/i18n'
import { useHeritageStore } from '@/stores/heritageStore'
import { recognitionYear } from '@/services/heritage/heritageLayer'
import { sites as allSites, siteTemporalBounds } from '@/services/heritage/heritageService'

const DECADE_START = 1860
const DECADE_END = 2020
const STEP_MS = 900

export function HeritageTemporalBar(): JSX.Element | null {
  const t = useT()
  const filters = useHeritageStore((s) => s.filters)
  const setFilters = useHeritageStore((s) => s.setFilters)
  const dim = useHeritageStore((s) => s.temporalDimension)
  const setDim = useHeritageStore((s) => s.setTemporalDimension)
  const playing = useHeritageStore((s) => s.playingYear)
  const setPlaying = useHeritageStore((s) => s.setPlayingYear)
  const timer = useRef<number | null>(null)

  const years = useMemo(() => {
    const out: number[] = []
    for (let y = DECADE_START; y <= DECADE_END; y += 10) out.push(y)
    return out
  }, [])

  // 播放循环
  useEffect(() => {
    if (playing == null) {
      if (timer.current) window.clearInterval(timer.current)
      timer.current = null
      return
    }
    timer.current = window.setInterval(() => {
      const cur = useHeritageStore.getState().playingYear
      if (cur == null) return
      const idx = years.indexOf(cur)
      if (idx < 0 || idx === years.length - 1) {
        useHeritageStore.getState().setPlayingYear(null)
        useHeritageStore.getState().setFilters({ temporal: null })
      } else {
        const next = years[idx + 1]
        useHeritageStore.getState().setPlayingYear(next)
        useHeritageStore.getState().setFilters({
          temporal: { fromYear: next, toYear: next + 9 },
        })
      }
    }, STEP_MS)
    return () => {
      if (timer.current) window.clearInterval(timer.current)
    }
  }, [playing, years])

  // 认定维度下无核实年份的遗产也参与(全部点都有认定年份)
  const formationCount = useMemo(
    () => allSites.filter((s) => siteTemporalBounds(s) != null).length,
    [],
  )

  const activeYear = filters.temporal ? filters.temporal.fromYear : null

  const setYear = (y: number) => {
    setFilters({ temporal: { fromYear: y, toYear: y + 9 } })
    setPlaying(null)
  }

  return (
    <div className="absolute bottom-6 left-1/2 -translate-x-1/2 z-10 glass rounded-lg px-3 py-2 text-xs text-text-primary w-[min(680px,calc(100%-160px))]">
      <div className="flex items-center gap-2 flex-wrap">
        <button
          onClick={() => setPlaying(playing != null ? null : (activeYear ?? DECADE_START))}
          className="w-7 h-7 rounded-full bg-accent-primary/20 text-accent-primary flex items-center justify-center shrink-0"
          title={playing != null ? t.heritage.pause : t.heritage.play}
        >
          {playing != null ? <Pause className="w-3.5 h-3.5" /> : <Play className="w-3.5 h-3.5" />}
        </button>
        <div className="flex rounded-md overflow-hidden border border-border shrink-0">
          <button
            onClick={() => setDim('formation')}
            className={`px-2 py-1 text-[11px] ${dim === 'formation' ? 'bg-accent-primary/20 text-accent-primary' : 'text-text-secondary'}`}
          >
            {t.heritage.timelineFormation}
          </button>
          <button
            onClick={() => setDim('recognition')}
            className={`px-2 py-1 text-[11px] ${dim === 'recognition' ? 'bg-accent-primary/20 text-accent-primary' : 'text-text-secondary'}`}
          >
            {t.heritage.timelineRecognition}
          </button>
        </div>
        <input
          type="range"
          min={DECADE_START}
          max={DECADE_END}
          step={10}
          value={activeYear ?? DECADE_START}
          onChange={(e) => setYear(Number(e.target.value))}
          className="flex-1 accent-current min-w-[120px]"
        />
        <span className="w-16 text-right font-medium shrink-0">
          {activeYear != null ? `${activeYear}–${activeYear + 9}` : '—'}
        </span>
        {activeYear != null && (
          <button
            onClick={() => {
              setFilters({ temporal: null })
              setPlaying(null)
            }}
            className="text-[11px] text-text-secondary hover:text-accent-primary shrink-0"
          >
            ✕
          </button>
        )}
      </div>
      <div className="flex items-center gap-1 mt-1 text-[10px] text-text-muted">
        <Info className="w-3 h-3 shrink-0" />
        <span className="truncate">
          {dim === 'formation'
            ? `${t.heritage.timelineHint}（${formationCount}/${allSites.length}）`
            : t.heritage.timelineHint}
        </span>
      </div>
    </div>
  )
}

export { recognitionYear }
