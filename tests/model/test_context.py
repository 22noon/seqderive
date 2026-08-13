from seqderive import Context


def test_empty_context():
    context = Context()

    assert context.left_flank == ""
    assert context.right_flank == ""
    assert context.repeat_candidates == ()


def test_context():
    context = Context(
        left_flank="AAA",
        right_flank="GGG",
        repeat_candidates=("AC", "ACAC"),
    )

    assert context.left_flank == "AAA"
    assert context.right_flank == "GGG"
    assert context.repeat_candidates == ("AC", "ACAC")
