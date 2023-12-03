import sys
import re

mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

pattern = "\d"
pattern2 = "\d"
for i in mapping:
    pattern += f"|{i}"
    pattern2 += f"|{i[::-1]}"


total = 0

for line in sys.stdin.readlines():
    num_str = ""

    found = re.findall(pattern, line)
    if found[0] in mapping:
        num_str += mapping[found[0]]
    else:
        num_str += found[0]

    found = [i[::-1] for i in re.findall(pattern2, line[::-1])]
    if found[0] in mapping:
        num_str += mapping[found[0]]
    else:
        num_str += found[0]

    total += int(num_str)

print(total)
