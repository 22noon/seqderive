from dataclasses import dataclass
from enum import Enum
from .context import Context
from .interval import Interval

class DifferenceType(Enum):
    """Primitive sequence differences reported by a tokenizer."""
    SNP = "SNP"
    INSERTION = "INSERTION"
    DELETION = "DELETION"

@dataclass(frozen=True, slots=True)
class Difference:
    """An observable sequence difference, without biological interpretation."""
    type: DifferenceType
    reference: Interval
    observed: Interval
    reference_sequence: str
    observed_sequence: str
    context: Context
