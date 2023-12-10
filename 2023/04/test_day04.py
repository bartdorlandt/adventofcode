import day04part1 as day04


def test_winning_numbers():
    two_parts = ['41 48 83 86 17', '83 86  6 31 17  9 48 53']
    expected = [48, 83, 17, 86]
    output = day04.winning_numbers(two_parts)
    assert output == expected


