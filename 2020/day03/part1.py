import sys

data = sys.stdin.read()
trajectory = [list(i) for i in data.split("\n")[:-1]]


def print_trajectory(trajectory):
    for item in trajectory:
        print("".join(item))


def count_trees(trajectory):
    number_of_trees = 0
    command_right = 3
    command_down = 1
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


print("Number of trees: {}".format(count_trees(trajectory)))
