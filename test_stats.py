import pytest

from stats import median


def test_odd() -> None:
    assert median([3.0, 1.0, 2.0]) == 2.0


def test_even() -> None:
    assert median([1.0, 2.0, 3.0, 4.0]) == 2.5


def test_empty() -> None:
    with pytest.raises(ValueError):
        median([])
