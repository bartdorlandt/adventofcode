#!/usr/bin/env python
from pathlib import Path


def winning_numbers(parts: list[str]) -> list[int]:
    part1 = list(map(int, parts[0].split()))
    part2 = list(map(int, parts[1].split()))
    return [int(x) for x in part2 if x in part1]


def total_counter(lines: list[str]) -> int:
    total = 0
    for line_no, line in enumerate(lines):
        new_line = line.split(": ")[1]
        two_parts = new_line.split(" | ")
        win_numbers = winning_numbers(two_parts)
        total += 2**(len(win_numbers)-1) if win_numbers else 0
        print(line_no, win_numbers, total)
    return total


if __name__ == "__main__":
    # input_file = Path("test_input.txt")
    input_file = Path("day04.txt")
    lines = input_file.read_text().splitlines()
    d = total_counter(lines)
    print("part numbers total:", d)
    # print("*** part 2 ***")
    # print("gears total:", gears)

