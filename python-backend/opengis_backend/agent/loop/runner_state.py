"""Shared mutable runner state for loop policies.

This keeps per-turn counters and one-shot control flags in a single place so
AgentLoop and WorkflowLoop do not each grow their own slightly different
state machines.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class RunnerTerminationKind(str, Enum):
    RUNNING = "running"
    COMPLETED = "completed"
    INTERRUPTED = "interrupted"
    FORCED_FINAL = "forced_final"
    FAILED = "failed"
    BUDGET_EXCEEDED = "budget_exceeded"
    HALTED = "halted"


@dataclass(frozen=True)
class RunnerTermination:
    kind: RunnerTerminationKind = RunnerTerminationKind.RUNNING
    reason: str = ""
    detail: str = ""

    def to_dict(self) -> dict[str, str]:
        return {
            "kind": self.kind.value,
            "reason": self.reason,
            "detail": self.detail,
        }


@dataclass
class RunnerState:
    iteration: int = 0
    code_steps: int = 0
    tool_steps: int = 0
    force_all_tools_once: bool = False
    force_final_reason: str | None = None
    nudged: bool = False
    tool_visibility_retried: bool = False
    terminal: RunnerTermination = field(default_factory=RunnerTermination)

    def next_iteration(self) -> int:
        current = self.iteration
        self.iteration += 1
        return current

    def add_steps(self, *, code_delta: int = 0, tool_delta: int = 0) -> None:
        self.code_steps += max(0, int(code_delta))
        self.tool_steps += max(0, int(tool_delta))

    def set_force_final(self, reason: str | None) -> None:
        if reason:
            self.force_final_reason = reason

    def reset_force_all_tools(self) -> None:
        self.force_all_tools_once = False

    def request_full_tool_surface(self) -> None:
        self.force_all_tools_once = True

    def mark_terminal(
        self,
        kind: RunnerTerminationKind,
        *,
        reason: str = "",
        detail: str = "",
    ) -> None:
        self.terminal = RunnerTermination(kind=kind, reason=reason, detail=detail)


__all__ = ["RunnerState", "RunnerTermination", "RunnerTerminationKind"]
