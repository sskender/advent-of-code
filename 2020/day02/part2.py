import sys

data = sys.stdin.read()
database = data.split("\n")[:-1]

valid_passwords = 0
for item in database:
    parts = item.split(" ")
    rules = parts[0].split("-")
    positions = (int(rules[0]) - 1, int(rules[1]) - 1)
    char = parts[1][0]
    password = parts[2]
    if (password[positions[0]] == char) ^ (password[positions[1]] == char):
        valid_passwords += 1

print("Valid passwords: ", valid_passwords)
