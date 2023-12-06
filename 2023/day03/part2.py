import sys

data = sys.stdin.read().split("\n")

numbers_good = []
total = 0


def get_number(matrix_row, x, chars):
    numbers = []
    start_pos = None

    for i, c in enumerate(chars):
        if c.isdigit():
            start_pos = i
            break

    if start_pos is None:
        return numbers

    j = x - 1 + start_pos
    while j >= 0 and matrix_row[j].isdigit():
        j -= 1

    start_idx = j+1
    end_idx = start_idx
    while end_idx < len(matrix_row) and matrix_row[end_idx].isdigit():
        end_idx += 1

    num_str = matrix_row[start_idx:end_idx]
    numbers.append(int(num_str))

    if chars[0].isdigit() and chars[1] == "." and chars[2].isdigit():
        start_idx = x+1
        end_idx = start_idx
        while end_idx < len(matrix_row) and matrix_row[end_idx].isdigit():
            end_idx += 1

        num_str = matrix_row[start_idx:end_idx]
        numbers.append(int(num_str))

    return numbers


def find_pair(matrix, pos):
    pair = []
    y, x = pos

    # diag top diag
    if y > 0:
        l_range = max(0, x-1)
        r_range = min(len(matrix[0]), x+1+1)
        top_chars = matrix[y-1][l_range:r_range]
        print(f"top: {top_chars}")
        nums = get_number(matrix[y-1], x, top_chars)
        for n in nums:
            pair.append(n)

    # left
    if x > 0:
        print(f"left: {matrix[y][x-1]}")
        j = 1
        while x-j >= 0 and matrix[y][x-j].isdigit():
            j += 1
        num_str = matrix[y][x-j+1:x-1+1]
        if num_str:
            pair.append(int(num_str))

    # right
    if x < len(matrix[0]) - 1:
        print(f"right: {matrix[y][x+1]}")
        j = 1
        while x+j < len(matrix[0]) and matrix[y][x+j].isdigit():
            j += 1
        num_str = matrix[y][x+1:x+j]
        if num_str:
            pair.append(int(num_str))

    # diag bottom diag
    if y < len(matrix) - 1:
        l_range = max(0, x-1)
        r_range = min(len(matrix[0]), x+1+1)
        bottom_chars = matrix[y+1][l_range:r_range]
        print(f"bottom: {bottom_chars}")
        nums = get_number(matrix[y+1], x, bottom_chars)
        for n in nums:
            pair.append(n)

    if len(pair) == 2:
        return sorted(pair)
    else:
        return []


for i in range(0, len(data)):
    row = data[i]
    pos = [-1, -1]
    j = 0
    while j < len(row):
        if row[j] == "*":
            pos[0] = i
            pos[1] = j
            pair = find_pair(data, pos)
            print(f"FOUND PAIR: {pair}")
            if pair and pair not in numbers_good:
                numbers_good.append(pair)
                total += pair[0] * pair[-1]
        j += 1

print(total)
