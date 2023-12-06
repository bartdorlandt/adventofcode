#!/usr/bin/env python

from pathlib import Path


def first_and_last(line: str) -> int:
    nums = [i for i in line if i.isdigit()]
    first_last = f"{nums[0]}{nums[-1]}"
    return int(first_last)


input_file = Path("input.txt")
lines = input_file.read_text().splitlines()
total = sum(first_and_last(line) for line in lines)
print(total)
