from typing import List, Tuple

numeral_map: List[Tuple[int, str]] = [
    (1000,"M"),
    (500,"D"),
    (100,"C"),
    (50,"L"),
    (10,"X"),
    (5,"V"),
    (1,"I"),
]

def convert(number: int) -> str:

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
