"""Local finalization for simple successful tool turns.

Some GIS turns are fully resolved by a side-effecting map/style tool. Sending
the tool result back to the provider just to get a one-line confirmation costs
another full prompt. This module keeps that optimization explicit and narrow.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any

from opengis_backend.agent.loop.turn_runner import ToolSettlement


_AUTO_FINAL_TOOLS: set[str] = {
    "fly_to",
    "zoom_to_layer",
    "set_basemap_visibility",
    "set_map_camera",
    "enter_3d_view",
    "exit_3d_view",
    "update_layer_style",
    "set_graduated_style",
    "set_categorized_style",
    "set_extrusion_style",
    "set_layer_visual_variables",
    "set_layer_filter",
    "set_layer_label",
    "highlight_features",
    "set_layer_order",
    "update_legend_spec",
    "set_raster_style",
}

_TOOL_MESSAGES: dict[str, str] = {
    "fly_to": "已调整地图视角。",
    "zoom_to_layer": "已缩放到目标图层。",
    "set_basemap_visibility": "已更新底图显示状态。",
    "set_map_camera": "已更新地图相机。",
    "enter_3d_view": "已切换到三维视角。",
    "exit_3d_view": "已切回二维视角。",
    "update_layer_style": "已更新图层样式，请在地图中确认效果。",
    "set_graduated_style": "已完成数值分级设色，请在地图中确认效果。",
    "set_categorized_style": "已完成分类设色，请在地图中确认效果。",
    "set_extrusion_style": "已更新三维拉伸样式，请在地图中确认效果。",
    "set_layer_visual_variables": "已更新图层大小、透明度或排序规则，请在地图中确认效果。",
    "set_layer_filter": "已更新图层显示过滤。",
    "set_layer_label": "已更新图层标注。",
    "highlight_features": "已完成要素高亮。",
    "set_layer_order": "已更新图层显示顺序。",
    "update_legend_spec": "已更新图例配置。",
    "set_raster_style": "已更新栅格渲染样式，请在地图中确认效果。",
}


@dataclass(frozen=True)
class AutoFinalDecision:
    text: str
    reason: str


def maybe_auto_final_tool_results(settlements: list[ToolSettlement]) -> AutoFinalDecision | None:
    """Return a deterministic final reply when tool results settle the turn.

    The rule is intentionally conservative:
    - every settlement must be a known map/style side-effect tool;
    - every settlement must be successful;
    - code/file/data/worker/operation/workflow tools never auto-finalize.
    """
    if not settlements:
        return None
    if any(item.name not in _AUTO_FINAL_TOOLS for item in settlements):
        return None
    if any(not _settlement_success(item) for item in settlements):
        return None

    names = [item.name for item in settlements]
    if len(set(names)) == 1 and len(settlements) == 1:
        return AutoFinalDecision(
            text=_TOOL_MESSAGES.get(names[0], "已完成操作。"),
            reason=names[0],
        )

    return AutoFinalDecision(
        text=f"已完成 {len(settlements)} 项地图/样式操作，请在地图中确认效果。",
        reason="batch:" + ",".join(names),
    )


def _settlement_success(settlement: ToolSettlement) -> bool:
    if settlement.error:
        return False
    parsed = _parse_json_object(settlement.content)
    if parsed is None:
        return True
    if parsed.get("success") is False:
        return False
    if parsed.get("error"):
        return False
    return True


def _parse_json_object(content: str) -> dict[str, Any] | None:
    try:
        parsed = json.loads(content)
    except Exception:
        return None
    return parsed if isinstance(parsed, dict) else None


__all__ = ["AutoFinalDecision", "maybe_auto_final_tool_results"]
