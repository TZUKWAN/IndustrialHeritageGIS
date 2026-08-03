"""Tool schema materialization for LLM turns.

Tool availability is an agent/profile contract, not a per-turn heuristic.
The executor and the provider should see the same stable tool surface after
registry/group/permission filtering.  Token pressure is handled by context
projection and observation compression, not by making tools disappear mid-run.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from opengis_backend.agent.execution.tool_packs import (
    ALWAYS_AVAILABLE_SCHEMA_NAMES,
    tool_pack_for_name,
)

_TOOL_VISIBILITY_MISS_RE = re.compile(
    r"(没有|不存在|无法|不能).{0,12}(工具|tool|接口)|"
    r"(no|do not|don't|cannot|can't).{0,24}(tool|function|interface)",
    re.IGNORECASE,
)

@dataclass
class ToolMaterialization:
    schemas: list[dict]
    selected_names: list[str]
    total_count: int
    reason: str


class ToolMaterializer:
    """Expose the stable profile tool-schema set for one provider turn."""

    def __init__(self, schemas: list[dict] | None) -> None:
        self.schemas = list(schemas or [])

    def materialize(
        self,
        force_all: bool = False,
        selected_packs: list[str] | set[str] | tuple[str, ...] | None = None,
    ) -> ToolMaterialization:
        # If a profile registered a tool, the model sees its schema until
        # permission/profile filtering removes it upstream.
        if force_all:
            return ToolMaterialization(
                schemas=self.schemas,
                selected_names=[self._name(schema) for schema in self.schemas],
                total_count=len(self.schemas),
                reason="all",
            )
        selected = self._dedupe(self.schemas)
        if selected_packs:
            selected_pack_set = {str(pack) for pack in selected_packs if str(pack)}
            selected = [
                schema
                for schema in selected
                if (
                    tool_pack_for_name(self._name(schema)) in selected_pack_set
                    or self._name(schema) in ALWAYS_AVAILABLE_SCHEMA_NAMES
                )
            ]
            reason = "packs:" + ",".join(sorted(selected_pack_set))
        else:
            reason = "profile"

        return ToolMaterialization(
            schemas=selected,
            selected_names=[self._name(schema) for schema in selected],
            total_count=len(self.schemas),
            reason=reason,
        )

    @staticmethod
    def _name(schema: dict) -> str:
        fn = schema.get("function") if isinstance(schema, dict) else None
        if isinstance(fn, dict):
            return str(fn.get("name") or "")
        return ""

    @staticmethod
    def _dedupe(schemas: list[dict]) -> list[dict]:
        out: list[dict] = []
        seen: set[str] = set()
        for schema in schemas:
            name = ToolMaterializer._name(schema)
            if not name or name in seen:
                continue
            seen.add(name)
            out.append(schema)
        return out


def format_active_tool_prompt(materialization: ToolMaterialization | None) -> str:
    """Build a concise per-turn system hint for active function tools."""
    if materialization is None:
        return ""
    names = [name for name in materialization.selected_names if name]
    if not names:
        return ""
    packs: dict[str, list[str]] = {}
    for name in names:
        packs.setdefault(tool_pack_for_name(name), []).append(name)
    lines = []
    for pack in sorted(packs):
        lines.append(f"- {pack}: {', '.join(sorted(packs[pack]))}")
    return (
        "## Active Function Tools For This Agent Profile\n"
        "The provider function schemas are the authoritative tool surface for "
        "exact parameters. Do not discuss internal tool assembly or tool counts "
        "with the user.\n"
        + "\n".join(lines)
    )


def is_tool_visibility_miss(text: str) -> bool:
    """Return True when text likely reflects dynamic tool visibility confusion."""
    return bool(text and _TOOL_VISIBILITY_MISS_RE.search(text))


__all__ = [
    "ToolMaterialization",
    "ToolMaterializer",
    "format_active_tool_prompt",
    "is_tool_visibility_miss",
]
