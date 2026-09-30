/**
 * 工业文化遗产GIS智能体 — 前端状态
 *
 * 面板/筛选/选中状态。地图图层单一数据源仍是 mapStore; 此 store 只表达
 * 遗产功能的 UI 状态, 筛选变化时由 bootstrap 同步到遗产图层的 style.filter。
 */
import { create } from 'zustand'
import {
  DEFAULT_FILTERS,
  eventsOf,
  getDetail,
  type HeritageFilters,
} from '@/services/heritage/heritageService'
import type { HeritageDetail } from '@/services/heritage/types'

export type HeritagePanelView = 'list' | 'analysis'
export type TemporalDimension = 'formation' | 'recognition'

interface HeritageStore {
  filters: HeritageFilters
  selectedId: string | null
  detail: HeritageDetail | null
  detailLoading: boolean
  detailPanelVisible: boolean
  panelView: HeritagePanelView
  temporalDimension: TemporalDimension
  /** 时间轴播放中的年份(十进制); null = 未播放 */
  playingYear: number | null

  setFilters: (f: Partial<HeritageFilters>) => void
  resetFilters: () => void
  select: (id: string | null) => void
  setDetailPanelVisible: (v: boolean) => void
  setPanelView: (v: HeritagePanelView) => void
  setTemporalDimension: (d: TemporalDimension) => void
  setPlayingYear: (y: number | null) => void
}

export const useHeritageStore = create<HeritageStore>((set) => ({
  filters: { ...DEFAULT_FILTERS },
  selectedId: null,
  detail: null,
  detailLoading: false,
  detailPanelVisible: false,
  panelView: 'list',
  temporalDimension: 'formation',
  playingYear: null,

  setFilters: (f) => set((s) => ({ filters: { ...s.filters, ...f } })),
  resetFilters: () => set({ filters: { ...DEFAULT_FILTERS } }),
  select: (id) => {
    if (!id) {
      set({ selectedId: null, detail: null, detailPanelVisible: false })
      return
    }
    set({ selectedId: id, detailLoading: true, detailPanelVisible: true })
    void getDetail(id).then((detail) => {
      const cur = useHeritageStore.getState()
      if (cur.selectedId === id) {
        useHeritageStore.setState({ detail, detailLoading: false })
      }
    })
  },
  setDetailPanelVisible: (v) => set({ detailPanelVisible: v }),
  setPanelView: (v) => set({ panelView: v }),
  setTemporalDimension: (d) => set({ temporalDimension: d }),
  setPlayingYear: (y) => set({ playingYear: y }),
}))

/** 事件数量辅助(供列表徽标) */
export function eventCountOf(id: string): number {
  return eventsOf(id).length
}
