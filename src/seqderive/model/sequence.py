from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Sequence:
    """Immutable nucleotide sequence."""

    id: str
    name: str
    bases: str

    @property
    def length(self) -> int:
        return len(self.bases)

    def __len__(self) -> int:
        return len(self.bases)
