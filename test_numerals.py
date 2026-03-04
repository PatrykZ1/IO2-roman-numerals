import pytest
import numerals


@pytest.mark.parametrize("n, expected", [
    (1, "I"),
    (4, "IV"),
    (5, "V"),
    (9, "IX"),
    (10, "X"),
    (40, "XL"),
    (50, "L"),
    (90, "XC"),
    (100, "C"),
    (400, "CD"),
    (500, "D"),
    (900, "CM"),
    (1000, "M"),
    (1984, "MCMLXXXIV"),
    (3999, "MMMCMXCIX"),
    (2024, "MMXXIV"),
])

def test_convert_basic(n, expected):
    assert numerals.convert(n) == expected

@pytest.mark.parametrize("wrong", [0, -1, 4000, 5000])
def test_convert_invalid_range(wrong):
    with pytest.raises(ValueError):
        numerals.convert(wrong)