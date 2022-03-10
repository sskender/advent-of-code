import sys

data = list(map(int, sys.stdin.read().split("\n")[:-1]))

# preamble_size = 5
preamble_size = 25

def validate_number(preamble, n):
    for i in preamble:
        if (n - i) in preamble:
            return True
    return False

for i in range(len(data)-preamble_size):
    preamble = data[i:i+preamble_size]
    n = data[preamble_size+i]
    if not validate_number(preamble, n):
        print(f"Invalid number: {n}")
        break
