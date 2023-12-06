import sys

data = sys.stdin.read().split("\n")

numbers_good = []
numbers_bad = []


def good_char_surround(s):
    for char in s:
        if char != "." and not char.isdigit():
            return True
    return False


def validate_pos(matrix, pos):
    a, b, c = pos
    # diag top diag
    if a > 0:
        l_range = max(0, b - 1)
        r_range = min(len(matrix[0]), c+1+1)
        top_chars = matrix[a-1][l_range:r_range]
        if good_char_surround(top_chars):
            return True
    # left
    if b > 0:
        left_char = matrix[a][b-1]
        if good_char_surround(left_char):
            return True
    # right
    if c < len(matrix[0]) - 1:
        right_char = matrix[a][c+1]
        if good_char_surround(right_char):
            return True
    # diag bottom diag
    if a < len(matrix) - 1:
        l_range = max(0, b - 1)
        r_range = min(len(matrix[0]), c+1+1)
        bottom_chars = matrix[a+1][l_range:r_range]
        if good_char_surround(bottom_chars):
            return True

    return False


for i in range(0, len(data)):
    row = data[i]
    pos = [-1, -1, -1]
    j = 0
    while j < len(row):
        if row[j].isdigit():
            pos[0] = i
            pos[1] = j
            num = ""
            while j < len(row) and row[j].isdigit():
                num += row[j]
                j += 1

            pos[2] = j - 1
            result = validate_pos(data, pos)
            if result:
                numbers_good.append(int(num))
            else:
                numbers_bad.append(int(num))
        j += 1

print(numbers_good)
print(numbers_bad)

print(sum(numbers_good))
