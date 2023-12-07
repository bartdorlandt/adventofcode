#!/usr/bin/env python
from pathlib import Path

gears = 0
lines_dict = {}
# lines_dict {
#   line_no: {
#     indexes: number
#   }
# }


def lookup_numbers(line_no: int, line: str, index: int, char: str) -> set[int]:
    global gears
    if index == 0:
        index_numbers = [0, 1]
    elif index == len(line):
        index_numbers = [index - 1, index]
    else:
        index_numbers = [index - 1, index, index + 1]

    set_numbers = set()
    # _get_tool_number(index_numbers, line_no + 1, set_numbers)  # post current line
    # if line_no != 0:
    #     _get_tool_number(index_numbers, line_no - 1, set_numbers)
    # _get_tool_number(index_numbers, line_no, set_numbers)
    gears += _get_tool_number2(index_numbers, line_no, set_numbers, char)
    # print()
    return set_numbers


def _get_tool_number2(index_numbers, line_no, set_numbers, char):
    prev_line = line_no - 1 if line_no > 0 else line_no
    post_line = min(line_no + 1, len(lines_dict))

    numbers_found = set()
    for index in index_numbers:
        for line in {prev_line, line_no, post_line}:
            for key, number in lines_dict[line].items():
                if str(index) in key.split(","):
                    numbers_found.add(number)
                    set_numbers.add(number)
    if char == "*" and len(numbers_found) == 2:
        x, y = numbers_found
        return int(x) * int(y)
    return 0


def _get_tool_number(index_numbers, line_no, set_numbers):
    try:
        lines_dict[line_no]
    except IndexError:
        return

    for key, number in lines_dict[line_no].items():
        for index in index_numbers:
            if str(index) in key.split(","):
                set_numbers.add(number)


def numbers_index_finder(line: str) -> dict:
    indexer = []
    numbers = []
    d = {}

    def save_state(d: dict, indexer: list[str], numbers: list[str]) -> tuple[list, list]:
        if indexer and numbers:
            d[",".join(indexer)] = "".join(numbers)
        return [], []

    for index, char in enumerate(line):
        if index == 0:
            indexer, numbers = save_state(d, indexer, numbers)
        if char == ".":
            indexer, numbers = save_state(d, indexer, numbers)
        elif char.isdigit():
            numbers.append(char)
            indexer.append(str(index))
        else:
            indexer, numbers = save_state(d, indexer, numbers)
    if index == len(line) - 1:
        _, _ = save_state(d, indexer, numbers)
    return d


def find_part(lines: list[str]) -> list[int]:
    for line_no, line in enumerate(lines):
        lines_dict[line_no] = numbers_index_finder(line)

    number_list = []
    for line_no, line in enumerate(lines):
        for index, char in enumerate(line):
            if char.isdigit() or char == ".":
                continue
            numbers = lookup_numbers(line_no, line, index, char)
            number_list.extend([x for x in numbers])
    return number_list


if __name__ == "__main__":
    # input_file = Path("test_input.txt")
    input_file = Path("day03.txt")
    lines = input_file.read_text().splitlines()
    d = find_part(lines)
    print("part numbers total:", sum(map(int, d)))
    print("*** part 2 ***")
    print("gears total:", gears)

