from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Context:
    """Local sequence context associated with an observation."""

    left_flank: str = ""
    right_flank: str = ""
    repeat_candidates: tuple[str, ...] = ()
