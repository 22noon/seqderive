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
    """A primitive sequence difference reported by a tokenizer.

    A Difference describes an observable sequence change. It does not
    represent a biological interpretation of that change.
    """

    type: DifferenceType
    reference: Interval
    observed: Interval
    reference_sequence: str
    observed_sequence: str
    context: Context
