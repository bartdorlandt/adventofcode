#!/usr/bin/env python

from pathlib import Path


def main(input_file: Path) -> int:
    lines = input_file.read_text()

    t = 0
    l1, l2 = [], []
    for line in lines.splitlines():
        x, y = line.split()
        l1.append(int(x))
        l2.append(int(y))

    for x in l1:
        if (v := l2.count(x)) > 0:
            t += x * v
    return t


if __name__ == "__main__":
    cwd = Path(__file__).parent
    test_input_file = Path(cwd / "test_input2.txt")
    total_test = main(test_input_file)
    print("total_test: ", total_test)
    assert total_test == 31

    input_file = Path(cwd / "input.txt")
    total = main(input_file)
    print("total: ", total)
