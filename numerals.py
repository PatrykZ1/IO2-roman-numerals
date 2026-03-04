# repozytorium: https://github.com/PatrykZ1/IO2-roman-numerals
from typing import List, Tuple

numeral_map: List[Tuple[int, str]] = [
    (1000,"M"),
    (900,"CM"),
    (500,"D"),
    (400,"CD"),
    (100,"C"),
    (90,"XC"),
    (50,"L"),
    (40,"XL"),
    (10,"X"),
    (9,"IX"),
    (5,"V"),
    (4,"IV"),
    (1,"I"),
]

def convert(number: int) -> str:
    if number <= 0 or number > 3999:
        raise ValueError("number must be in range 1..3999")
    if not isinstance(number, int):
        raise TypeError("number must be an int")
    n = number
    parts: List[str] = []
    for value, symbol in numeral_map:
        if n == 0:
            break
        count = n // value
        if count:
            parts.append(symbol * count)
            n -= value * count

    return "".join(parts)
