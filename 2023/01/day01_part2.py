#!/usr/bin/env python
import re
from pathlib import Path

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def first_and_last(line: str) -> int:
    # using positive lookahead to find all matches
    re_str = rf"(?=(\d|{'|'.join(numbers.keys())}))"
    found = re.findall(re_str, line)
    first = numbers.get(found[0], found[0])
    last = numbers.get(found[-1], found[-1])
    first_last = f"{first}{last}"
    return int(first_last)


if __name__ == "__main__":
    input_file = Path("input.txt")
    lines = input_file.read_text().splitlines()
    total = sum(first_and_last(line) for line in lines)
    print(total)
