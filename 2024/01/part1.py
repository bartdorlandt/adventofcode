#!/usr/bin/env python

from pathlib import Path


def main(input_file: Path) -> int:
    lines = input_file.read_text()

    l1, l2 = [], []
    for line in lines.splitlines():
        x, y = line.split()
        l1.append(int(x))
        l2.append(int(y))

    sorted_l1 = sorted(l1)
    sorted_l2 = sorted(l2)

    return sum(abs(x - y) for x, y in zip(sorted_l1, sorted_l2))


if __name__ == "__main__":
    cwd = Path(__file__).parent
    test_input_file = Path(cwd / "test_input.txt")
    total_test = main(test_input_file)
    assert total_test == 11

    input_file = Path(cwd / "input.txt")
    total = main(input_file)
    print("total: ", total)
