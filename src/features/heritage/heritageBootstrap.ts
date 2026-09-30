/**
 * 工业文化遗产GIS智能体 — 地图集成引导
 *
 * 在 MapView 内挂载: 自动装载遗产点图层、把筛选同步到图层过滤、
 * 点击遗产点打开详情、鼠标悬停指针。全部通过 mapStore/mapEngine 现有管道。
 */
import { useEffect } from 'react'
import { mapEngine } from '@/features/map/engine/MapEngine'
import { useMapStore } from '@/stores/mapStore'
import { useHeritageStore } from '@/stores/heritageStore'
import {
  HERITAGE_LAYER_ID,
  HERITAGE_KDE_LAYER_ID,
  HERITAGE_PROVINCE_LAYER_ID,
  sites as allSites,
} from '@/services/heritage/heritageService'
import { buildHeritageLayerDef, compileHeritageFilter } from '@/services/heritage/heritageLayer'

let bootstrapped = false
let chinaViewApplied = false

const CHINA_BBOX: [[number, number], [number, number]] = [
  [73.5, 18.0],
  [135.0, 53.6],
]

/**
 * 遗产图层生命周期与交互。必须在 MapView(持有 MapEngine 的组件)内调用一次。
 */
export function useHeritageBootstrap(enabled: boolean): void {
  // 1) 装载遗产点图层(幂等)
  useEffect(() => {
    if (!enabled || bootstrapped) return
    const store = useMapStore.getState()
    if (store.getLayerById(HERITAGE_LAYER_ID)) {
      bootstrapped = true
      return
    }
    store.addLayer(buildHeritageLayerDef(allSites))
    bootstrapped = true
  }, [enabled])

  // 2) 首次就绪后定位到全国范围(不覆盖用户后续操作)
  useEffect(() => {
    if (!enabled || chinaViewApplied) return
    const t = window.setInterval(() => {
      const map = mapEngine.getMap()
      if (map && mapEngine.isReady()) {
        window.clearInterval(t)
        if (!chinaViewApplied) {
          try {
            mapEngine.fitBounds(CHINA_BBOX, { padding: 40, maxZoom: 5, duration: 0 })
          } catch {
            // fitBounds 失败不阻塞
          }
          chinaViewApplied = true
        }
      }
    }, 300)
    const timeout = window.setTimeout(() => window.clearInterval(t), 15000)
    return () => {
      window.clearInterval(t)
      window.clearTimeout(timeout)
    }
  }, [enabled])

  // 3) 筛选/时间维度 → 图层过滤
  const filters = useHeritageStore((s) => s.filters)
  const dim = useHeritageStore((s) => s.temporalDimension)
  useEffect(() => {
    if (!enabled || !bootstrapped) return
    const spec = compileHeritageFilter(filters, dim)
    useMapStore.getState().updateLayerStyle(HERITAGE_LAYER_ID, { filter: spec })
  }, [filters, dim, enabled])

  // 4) 点选 → 详情; 悬停指针
  useEffect(() => {
    if (!enabled) return
    const t = window.setInterval(() => {
      const map = mapEngine.getMap()
      if (!map || !mapEngine.isReady()) return
      window.clearInterval(t)

      const layerIds = [HERITAGE_LAYER_ID]
      const onClick = (e: { point: { x: number; y: number } }) => {
        const feats = map.queryRenderedFeatures([e.point.x, e.point.y], { layers: layerIds })
        if (feats.length > 0) {
          const hid = feats[0].properties?.heritage_id
          if (typeof hid === 'string') {
            useHeritageStore.getState().select(hid)
          }
        }
      }
      const onMove = (e: { point: { x: number; y: number } }) => {
        const canvas = map.getCanvas()
        const feats = map.queryRenderedFeatures([e.point.x, e.point.y], { layers: layerIds })
        canvas.style.cursor = feats.length > 0 ? 'pointer' : ''
      }
      map.on('click', onClick)
      map.on('mousemove', onMove)
    }, 300)
    return () => {
      window.clearInterval(t)
      const map = mapEngine.getMap()
      // MapLibre Evented 无 off 的类型化重载一致问题, 用 unbind 兜底
      try {
        ;(map as unknown as { off: (t: string, l: unknown) => void })?.off?.('click', undefined)
      } catch {
        // ignore
      }
    }
  }, [enabled])
}

/** 分析图层开关(省级统计/KDE): 添加到底部避免遮挡点位 */
export function toggleAnalysisLayer(id: string, want: boolean): void {
  const store = useMapStore.getState()
  const has = !!store.getLayerById(id)
  if (want && !has) {
    const def = id === HERITAGE_PROVINCE_LAYER_ID
      ? requireProvinceLayer()
      : requireKdeLayer()
    store.addLayer(def)
    // 移到最底(索引0), 保证遗产点始终在分析层之上
    const idx = useMapStore.getState().layers.findIndex((l) => l.id === id)
    if (idx > 0) {
      useMapStore.getState().reorderLayers(idx, 0)
    }
  } else if (!want && has) {
    store.removeLayer(id)
  }
}

function requireProvinceLayer() {
  // 延迟 require 避免 boot 顺序耦合
  // eslint-disable-next-line @typescript-eslint/no-var-requires
  const mod = require('@/services/heritage/heritageLayer') as typeof import('@/services/heritage/heritageLayer')
  return mod.buildProvinceLayerDef()
}

function requireKdeLayer() {
  // eslint-disable-next-line @typescript-eslint/no-var-requires
  const mod = require('@/services/heritage/heritageLayer') as typeof import('@/services/heritage/heritageLayer')
  return mod.buildKdeLayerDef()
}

export { HERITAGE_KDE_LAYER_ID, HERITAGE_PROVINCE_LAYER_ID }
