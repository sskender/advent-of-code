import sys
import re

total = 0

for line in sys.stdin.readlines():
    found = re.findall("\d", line)
    total += int(found[0] + found[-1])

print(total)
