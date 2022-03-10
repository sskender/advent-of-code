import sys

data = list(map(int, sys.stdin.read().split("\n")[:-1]))

# preamble_size = 5
preamble_size = 25

def validate_number(preamble, n):
    for i in preamble:
        if (n - i) in preamble:
            return True
    return False

invalid_number = 0
for i in range(len(data)-preamble_size):
    preamble = data[i:i+preamble_size]
    n = data[preamble_size+i]
    if not validate_number(preamble, n):
        invalid_number = n
        print(f"Invalid number: {n}")
        break

contiguous_set = list()
first_element_index = 0
i = 0

while True:
    # out of range
    if i >= len(data):
        break
    # print(f"sum: {sum(contiguous_set)} : {contiguous_set}")
    if sum(contiguous_set) > invalid_number:
        first_element_index += 1
        i = first_element_index
        contiguous_set = [data[first_element_index]]
    elif sum(contiguous_set) == invalid_number:
        print("DONE")
        print(contiguous_set)
        assert(sum(contiguous_set) == invalid_number)
        break
    else:
        contiguous_set.append(data[i])
    i += 1

def encryption_weakness(contiguous_set):
    contiguous_set.sort()
    return contiguous_set[0] + contiguous_set[-1]

print(f"Encryption weakness: {encryption_weakness(contiguous_set)}")
