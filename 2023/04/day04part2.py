#!/usr/bin/env python
from pathlib import Path


def winning_numbers(parts: list[str]) -> list[int]:
    part1 = list(map(int, parts[0].split()))
    part2 = list(map(int, parts[1].split()))
    return [int(x) for x in part2 if x in part1]


def add_numbers(counter: dict, numbers: list[int]):
    for number in numbers:
        if number in counter:
            counter[number] += 1
        else:
            counter[number] = 1


def count_cards(lines: list[str]) -> int:
    counter_lines = {}
    total_cards = 0
    for line_no, line in enumerate(lines, start=1):
        for _ in range(counter_lines.get(line_no, 0) + 1):
            new_line = line.split(": ")[1]
            two_parts = new_line.split(" | ")
            win_numbers = winning_numbers(two_parts)
            add_numbers(counter_lines, list(range(line_no + 1, len(win_numbers) + line_no + 1)))
            total_cards += 1
            # print(line_no, win_numbers, total_cards)
    return total_cards


if __name__ == "__main__":
    # input_file = Path("test_input.txt")
    input_file = Path("day04.txt")
    lines = input_file.read_text().splitlines()
    total_lines = len(lines)
    d = count_cards(lines)
    print("Total numbers of cards:", d)

