import copy
import math
import sys

data = sys.stdin.read()
trajectory = [list(i) for i in data.split("\n")[:-1]]


def print_trajectory(trajectory):
    for item in trajectory:
        print("".join(item))


def count_trees(trajectory, command_right=3, command_down=1):
    trajectory = copy.deepcopy(trajectory)
    number_of_trees = 0
    tree_symbol = "#"
    j = command_right
    for i in range(command_down, len(trajectory), command_down):
        if trajectory[i][j] == tree_symbol:
            number_of_trees += 1
            trajectory[i][j] = "X"
        else:
            trajectory[i][j] = "O"
        j += command_right
        if j >= len(trajectory[0]):
            j = j % len(trajectory[0])
    print_trajectory(trajectory)
    return number_of_trees


number_of_trees_on_slopes = [
    count_trees(trajectory, 1, 1),
    count_trees(trajectory, 3, 1),
    count_trees(trajectory, 5, 1),
    count_trees(trajectory, 7, 1),
    count_trees(trajectory, 1, 2)
]

print(math.prod(number_of_trees_on_slopes))
