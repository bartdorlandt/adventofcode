#!/usr/bin/env python
from pathlib import Path


def split_info(line):
    d = {}
    game_number, game_data = line.split(":")
    number = game_number.split()[1].strip()
    for games in game_data.strip().split(";"):
        for sets in games.split(", "):
            s, color = sets.split()
            if color in d:
                if int(s) > d[color]:
                    d[color] = int(s)
            else:
                d[color] = int(s)
    return number, d


def gen_dict(lines: list[str]) -> dict:
    d = {}
    for line in lines:
        number, data = split_info(line)
        d[number] = data
    return d


def which_games(d: dict, test_game: dict) -> int:
    games_fit = []
    for game_number, game_data in d.items():
        if (
                test_game["red"] >= game_data["red"] and
                test_game["green"] >= game_data["green"] and
                test_game["blue"] >= game_data["blue"]
        ):
            games_fit.append(int(game_number))
    with open("games_fit.txt", "w") as f:
        f.write("\n".join(map(str, games_fit)))
    return sum(games_fit)


def power_of_cubes(cubes: dict) -> int:
    return cubes["red"] * cubes["green"] * cubes["blue"]


if __name__ == "__main__":
    input_file = Path("day02.txt")
    lines = input_file.read_text().splitlines()
    d = gen_dict(lines)
    print(d)
    test_game = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    print(which_games(d, test_game))
    print(sum([power_of_cubes(d[game]) for game in d]))
