import sys
from math import prod

data = sys.stdin.read()
numbers = [int(i) for i in data.split("\n")[:-1]]


# Complexity: O(n^2)
def find_pair(numbers, value):
    remainders = {}
    for n in numbers:
        for m in numbers:
            remainder = value - n - m
            if remainder in remainders:
                return (n, m, remainder)
            else:
                remainders[n] = n
    raise ValueError("Pair not found")


pair = find_pair(numbers, 2020)

print(pair)
print(prod(pair))
