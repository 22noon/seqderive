from dataclasses import dataclass
from enum import Enum
from typing import Protocol
from .sequence import Sequence

class OperationType(Enum):
    MATCH = "MATCH"
    SNP = "SNP"
    INSERTION = "INSERTION"
    DELETION = "DELETION"
    REPEAT_EXPANSION = "REPEAT_EXPANSION"
    REPEAT_CONTRACTION = "REPEAT_CONTRACTION"

class Operation(Protocol):
    @property
    def type(self) -> OperationType: ...
    def apply(self, sequence: Sequence) -> Sequence: ...
    def describe(self) -> str: ...

@dataclass(frozen=True, slots=True)
class Match:
    position: int
    length: int
    @property
    def type(self) -> OperationType:
        return OperationType.MATCH
    def apply(self, sequence: Sequence) -> Sequence:
        return sequence
    def describe(self) -> str:
        return f"Match ({self.length} bp)"

@dataclass(frozen=True, slots=True)
class SNP:
    position: int
    reference_base: str
    alternate_base: str
    @property
    def type(self) -> OperationType:
        return OperationType.SNP
    def apply(self, sequence: Sequence) -> Sequence:
        if not 0 <= self.position < len(sequence):
            raise ValueError("SNP position is outside the sequence")
        if sequence.bases[self.position] != self.reference_base:
            raise ValueError("Reference base does not match sequence")
        bases = sequence.bases[:self.position] + self.alternate_base + sequence.bases[self.position + 1:]
        return Sequence(sequence.id, sequence.name, bases)
    def describe(self) -> str:
        return f"SNP at {self.position}: {self.reference_base}>{self.alternate_base}"

@dataclass(frozen=True, slots=True)
class Insertion:
    position: int
    sequence: str
    @property
    def type(self) -> OperationType:
        return OperationType.INSERTION
    def apply(self, sequence: Sequence) -> Sequence:
        if not 0 <= self.position <= len(sequence):
            raise ValueError("Insertion position is outside the sequence")
        bases = sequence.bases[:self.position] + self.sequence + sequence.bases[self.position:]
        return Sequence(sequence.id, sequence.name, bases)
    def describe(self) -> str:
        return f"Insert {self.sequence!r} at {self.position}"

@dataclass(frozen=True, slots=True)
class Deletion:
    position: int
    sequence: str
    @property
    def type(self) -> OperationType:
        return OperationType.DELETION
    def apply(self, sequence: Sequence) -> Sequence:
        end = self.position + len(self.sequence)
        if sequence.bases[self.position:end] != self.sequence:
            raise ValueError("Sequence at deletion position does not match")
        return Sequence(sequence.id, sequence.name, sequence.bases[:self.position] + sequence.bases[end:])
    def describe(self) -> str:
        return f"Delete {self.sequence!r} at {self.position}"

@dataclass(frozen=True, slots=True)
class RepeatExpansion:
    position: int
    motif: str
    copies_before: int
    copies_after: int
    @property
    def type(self) -> OperationType:
        return OperationType.REPEAT_EXPANSION
    def apply(self, sequence: Sequence) -> Sequence:
        if not self.motif:
            raise ValueError("Repeat motif cannot be empty")
        if self.copies_after <= self.copies_before:
            raise ValueError("Expansion requires copies_after > copies_before")
        repeat = self.motif * self.copies_before
        end = self.position + len(repeat)
        if sequence.bases[self.position:end] != repeat:
            raise ValueError("Expected repeat not found at position")
        expanded = self.motif * self.copies_after
        return Sequence(sequence.id, sequence.name, sequence.bases[:self.position] + expanded + sequence.bases[end:])
    def describe(self) -> str:
        return f"Expand tandem repeat {self.motif!r} from {self.copies_before} to {self.copies_after} copies at {self.position}"

@dataclass(frozen=True, slots=True)
class RepeatContraction:
    position: int
    motif: str
    copies_before: int
    copies_after: int
    @property
    def type(self) -> OperationType:
        return OperationType.REPEAT_CONTRACTION
    def apply(self, sequence: Sequence) -> Sequence:
        if not self.motif:
            raise ValueError("Repeat motif cannot be empty")
        if self.copies_after >= self.copies_before:
            raise ValueError("Contraction requires copies_after < copies_before")
        repeat = self.motif * self.copies_before
        end = self.position + len(repeat)
        if sequence.bases[self.position:end] != repeat:
            raise ValueError("Expected repeat not found at position")
        contracted = self.motif * self.copies_after
        return Sequence(sequence.id, sequence.name, sequence.bases[:self.position] + contracted + sequence.bases[end:])
    def describe(self) -> str:
        return f"Contract tandem repeat {self.motif!r} from {self.copies_before} to {self.copies_after} copies at {self.position}"
