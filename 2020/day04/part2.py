import sys
import re

data = sys.stdin.read()
raw_passports = [i.strip() for i in data.split("\n\n")]


def validate_num(raw_num, low, high):
    if len(raw_num) != 4 or not raw_num.isdigit():
        return False
    num = int(raw_num)
    return (num >= low and num <= high)


def validate_height(height):
    if not height[:-2].isdigit():
        return False
    num = int(height[:-2])
    if height[::-1][:2][::-1] == "cm":
        return num >= 150 and num <= 193
    elif height[::-1][:2][::-1] == "in":
        return num >= 59 and num <= 76
    else:
        return False


def validate_hex_color(color):
    pattern = re.compile(r"^#[a-f0-9]{6}$")
    return bool(re.fullmatch(pattern, color))


def validate_eye_color(color):
    colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return color in colors


def validate_pid(pid):
    return len(pid) == 9 and pid.isdigit()


def validate_passport(raw_passport):
    items = [item.strip() for item in re.split(r"[ |\n]", raw_passport)]
    passport = dict()
    for item in items:
        kv = item.split(":")
        passport[kv[0]] = kv[1]
    if not validate_num(passport["byr"], 1920, 2002):
        return False
    if not validate_num(passport["iyr"], 2010, 2020):
        return False
    if not validate_num(passport["eyr"], 2020, 2030):
        return False
    if not validate_height(passport["hgt"]):
        return False
    if not validate_hex_color(passport["hcl"]):
        return False
    if not validate_eye_color(passport["ecl"]):
        return False
    if not validate_pid(passport["pid"]):
        return False
    return True


valid_passports = 0
for passport in raw_passports:
    try:
        if validate_passport(passport):
            valid_passports += 1
    except Exception:
        pass

print("Number of valid passports: {}".format(valid_passports))
