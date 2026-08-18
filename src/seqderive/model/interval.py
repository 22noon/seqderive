from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Interval:
    """Half-open interval [start, end)."""
    start: int
    end: int

    def __post_init__(self) -> None:
        if self.start < 0:
            raise ValueError("Interval start cannot be negative")
        if self.end < self.start:
            raise ValueError("Interval end cannot be less than start")

    @property
    def length(self) -> int:
        return self.end - self.start
