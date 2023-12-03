import sys
import math

map_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

RED_LABEL = "red"
GREEN_LABEL = "green"
BLUE_LABEL = "blue"


def get_cube_number(cube):
    return int(cube.split(" ")[1])


def find_max_game_set(game_set, game_max_cubes):
    cubes = game_set.split(",")
    for cube in cubes:
        if RED_LABEL in cube:
            game_max_cubes[RED_LABEL] = max(
                game_max_cubes[RED_LABEL], get_cube_number(cube))
        elif GREEN_LABEL in cube:
            game_max_cubes[GREEN_LABEL] = max(
                game_max_cubes[GREEN_LABEL], get_cube_number(cube))
        elif BLUE_LABEL in cube:
            game_max_cubes[BLUE_LABEL] = max(
                game_max_cubes[BLUE_LABEL], get_cube_number(cube))


total = 0
game_number = 0

for line in sys.stdin.readlines():
    game_number += 1
    game_sets = line.split(":")[1].split(";")

    game_max_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for game_set in game_sets:
        find_max_game_set(game_set, game_max_cubes)

    power_set = math.prod(game_max_cubes.values())
    total += power_set

print(total)
