import pytest
import numerals


@pytest.mark.parametrize("n, expected", [
    (1, "I"),
    (5, "V"),
    (10, "X"),
    (50, "L"),
    (100, "C"),
    (500, "D"),
    (1000, "M"),
])

def test_convert_basic(n, expected):
    assert numerals.convert(n) == expected
