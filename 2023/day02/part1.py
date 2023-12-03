import sys

map_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

RED_LABEL = "red"
GREEN_LABEL = "green"
BLUE_LABEL = "blue"


def validate_cube(cube, label):
    num = int(cube.split(" ")[1])
    return num <= map_cubes[label]


def validate_game_set(game_set):
    cubes = game_set.split(",")
    for cube in cubes:
        if RED_LABEL in cube:
            if not validate_cube(cube, RED_LABEL):
                return False
        elif GREEN_LABEL in cube:
            if not validate_cube(cube, GREEN_LABEL):
                return False
        elif BLUE_LABEL in cube:
            if not validate_cube(cube, BLUE_LABEL):
                return False
    return True


total = 0
game_number = 0
for line in sys.stdin.readlines():
    game_number += 1
    game_sets = line.split(":")[1].split(";")
    game_valid = True
    for game_set in game_sets:
        if not validate_game_set(game_set):
            game_valid = False
            break
    if not game_valid:
        continue
    total += game_number
    print(f"game {game_number} is valid")

print(total)
