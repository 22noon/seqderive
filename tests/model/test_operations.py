from seqderive import Deletion, Insertion, Match, OperationType, RepeatContraction, RepeatExpansion, SNP, Sequence

def test_match():
    s = Sequence("ref", "reference", "ACTG")
    op = Match(0, 4)
    assert op.type is OperationType.MATCH
    assert op.apply(s) == s

def test_snp():
    s = Sequence("ref", "reference", "ACTG")
    result = SNP(2, "T", "A").apply(s)
    assert result.bases == "ACAG"

def test_insertion():
    s = Sequence("ref", "reference", "ABCDEF")
    result = Insertion(3, "XYZ").apply(s)
    assert result.bases == "ABCXYZDEF"

def test_deletion():
    s = Sequence("ref", "reference", "ABCXYZDEF")
    result = Deletion(3, "XYZ").apply(s)
    assert result.bases == "ABCDEF"

def test_repeat_expansion():
    s = Sequence("ref", "reference", "ABCABCDEF")
    result = RepeatExpansion(0, "ABC", 2, 3).apply(s)
    assert result.bases == "ABCABCABCDEF"

def test_repeat_contraction():
    s = Sequence("ref", "reference", "ABCABCABCDEF")
    result = RepeatContraction(0, "ABC", 3, 2).apply(s)
    assert result.bases == "ABCABCDEF"
