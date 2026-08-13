from seqderive import (
    Context,
    Difference,
    DifferenceType,
    Interval,
)


def test_insertion_difference():
    difference = Difference(
        type=DifferenceType.INSERTION,
        reference=Interval(3, 3),
        observed=Interval(3, 6),
        reference_sequence="",
        observed_sequence="ABC",
        context=Context(
            left_flank="XYZ",
            right_flank="DEF",
        ),
    )

    assert difference.type is DifferenceType.INSERTION
    assert difference.reference.length == 0
    assert difference.observed.length == 3
    assert difference.observed_sequence == "ABC"
