from seqderive import Sequence


def test_sequence_length():
    sequence = Sequence(
        id="ref",
        name="reference",
        bases="ACTG",
    )

    assert sequence.length == 4
    assert len(sequence) == 4


def test_sequence_is_immutable():
    sequence = Sequence(
        id="ref",
        name="reference",
        bases="ACTG",
    )

    try:
        sequence.bases = "AAAA"
    except AttributeError:
        pass
    else:
        raise AssertionError("Sequence should be immutable")
