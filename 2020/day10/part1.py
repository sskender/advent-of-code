import sys

data = list(map(int, sys.stdin.read().split("\n")[:-1]))

data.append(0)  # charging outlet
data.append(max(data) + 3)  # my device
data.sort()

count_1_jolt = 0
count_3_jolt = 0

for i in range(len(data) - 1):
    if data[i+1] - data[i] == 1:
        count_1_jolt += 1
    elif data[i+1] - data[i] == 3:
        count_3_jolt += 1

print(f"1 jolt: {count_1_jolt}")
print(f"3 jolt: {count_3_jolt}")
print(f"Total: {count_1_jolt * count_3_jolt}")
