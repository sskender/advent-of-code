import sys

data = sys.stdin.read()
database = data.split("\n")[:-1]

valid_passwords = 0
for item in database:
    parts = item.split(" ")
    rules = parts[0].split("-")
    limits = (int(rules[0]), int(rules[1]))
    char = parts[1][0]
    password = parts[2]
    occurances = password.count(char)
    if occurances >= limits[0] and occurances <= limits[1]:
        valid_passwords += 1

print("Valid passwords: ", valid_passwords)
