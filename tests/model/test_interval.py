import pytest

from seqderive import Interval


def test_interval_length():
    interval = Interval(10, 15)

    assert interval.length == 5


def test_interval_is_half_open():
    interval = Interval(10, 15)

    assert interval.start == 10
    assert interval.end == 15


def test_negative_start_is_rejected():
    with pytest.raises(ValueError):
        Interval(-1, 5)


def test_reversed_interval_is_rejected():
    with pytest.raises(ValueError):
        Interval(10, 5)
