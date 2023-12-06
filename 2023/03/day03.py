#!/usr/bin/env python
from pathlib import Path

lines_dict = {}
# lines_dict {
#   line_no: {
#     indexes: number
#   }
# }


def lookup_numbers(line_no: int, line: str, index: int) -> set[int]:
    if index == 0:
        index_numbers = [0, 1]
    elif index == len(line):
        index_numbers = [index - 1, index]
    else:
        index_numbers = [index - 1, index, index + 1]

    set_numbers = set()
    _get_tool_number(index_numbers, line_no + 1, set_numbers)  # post current line
    if line_no != 0:
        _get_tool_number(index_numbers, line_no - 1, set_numbers)
    _get_tool_number(index_numbers, line_no, set_numbers)
    # print()
    return set_numbers


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
            numbers = lookup_numbers(line_no, line, index)
            number_list.extend([x for x in numbers])
    return number_list


if __name__ == "__main__":
    # input_file = Path("test_input.txt")
    input_file = Path("day03.txt")
    lines = input_file.read_text().splitlines()
    d = find_part(lines)
    print(sum(map(int, d)))

