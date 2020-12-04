# --- Day 4: Passport Processing ---
# https://adventofcode.com/2020/day/4
import re


def between(str, min, max):

    if int(str) >= min and int(str) <= max:
        return True
    else:
        return False


def is_valid_height(hgt):

    m = re.match(r"([0-9]+)(cm|in)$", hgt)
    if m.group(2) == ("cm") and between(int(m.group(1)), 150, 193):
        return True
    elif m.group(2) == ("in") and between(int(m.group(1)), 59, 76):
        return True
    elif hgt.endswith("in") and between(filter(str.isdigit, hgt), 59, 76):
        return True
    else:
        return False


def is_valid_hair_color(hcl):

    if len(re.match(r"\#([0-9a-z]+)$", hcl).group(1)) == 6:
        return True
    else:
        return False


def is_valid_eye_color(ecl):

    if re.match(r"[amb|blu|brn|gry|grn|hzl|oth]", ecl):
        return True
    else:
        return False


def is_valid_passport_id(pid):

    if re.match(r"[0-9]{9}$", pid):
        return True
    else:
        return False


passport = {}
passports = []
part1 = 0
part2 = 0
with open('input.txt', 'r') as reader:
    input = [i.strip() for i in reader.readlines()]
for line in input:
    m = re.findall(r"([a-zA-Z]+):(\S+)", line)
    for field in m:
        passport[field[0]] = field[1]
    if not m:
        passports.append(passport.copy())
        passport.clear()
if passport:  # last passport on buffer
    passports.append(passport.copy())
for p in passports:
    if p.get('byr') and p.get('iyr') and p.get('eyr') and \
       p.get('hgt') and p.get('hcl') and p.get('ecl') and p.get('pid'):
        part1 = part1 + 1
    try:
        if between(p.get('byr'), 1920, 2002) and \
           between(p.get('iyr'), 2010, 2020) and \
           between(p.get('eyr'), 2020, 2030) and \
           is_valid_height(p.get('hgt')) and \
           is_valid_hair_color(p.get('hcl')) and \
           is_valid_eye_color(p.get('ecl')) and \
           is_valid_passport_id(p.get('pid')):
            part2 = part2 + 1
    except:  # noqa: E722
        pass

print(part1)
print(part2)
