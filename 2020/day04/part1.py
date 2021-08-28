import sys

data = sys.stdin.read()
raw_passports = [i.strip() for i in data.split("\n\n")]


def validate_passport(raw_passport):
    if "byr" not in raw_passport:
        raise Exception("Invalid birth year")
    if "iyr" not in raw_passport:
        raise Exception("Invalid issue year")
    if "eyr" not in raw_passport:
        raise Exception("Invalid expiration year")
    if "hgt" not in raw_passport:
        raise Exception("Invalid height")
    if "hcl" not in raw_passport:
        raise Exception("Invalid hair color")
    if "ecl" not in raw_passport:
        raise Exception("Invalid eye color")
    if "pid" not in raw_passport:
        raise Exception("Invalid passport id")
    # if "cid" not in raw_passport:
    #     raise Exception("Invalid country id")
    return True


valid_passports = 0
for passport in raw_passports:
    try:
        if validate_passport(passport):
            valid_passports += 1
    except Exception:
        pass

print("Number of valid passports: {}".format(valid_passports))
