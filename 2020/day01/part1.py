import sys
from math import prod

data = sys.stdin.read()
numbers = [int(i) for i in data.split("\n")[:-1]]


# Complexity: O(n)
def find_pair(numbers, value):
    remainders = {}
    for n in numbers:
        remainder = value - n
        if remainder in remainders:
            return (n, remainder)
        else:
            remainders[n] = n
    raise ValueError("Pair not found")


pair = find_pair(numbers, 2020)

print(pair)
print(prod(pair))
