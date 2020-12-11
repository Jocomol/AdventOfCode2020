#!/usr/bin/python3

lines = None
with open("day_4_input", "r") as f:
    lines = f.readlines()

valid_counter = 0
byr = iyr = eyr = hgt = hcl = ecl = pid = False

for line in lines:
    if line == '\n':
        print("---")
        if byr == iyr == eyr == hgt == hcl == ecl == pid is True:
            valid_counter += 1
            print("VALID")
        byr = iyr = eyr = hgt = hcl = ecl = pid = False
        print("---")
    else:
        line_array = line.split(" ")
        for entry in line_array:
            key = entry.split(":")[0]
            print(key)
            if key == "byr":
                byr = True
            if key == "iyr":
                iyr = True
            if key == "eyr":
                eyr = True
            if key == "hgt":
                hgt = True
            if key == "hcl":
                hcl = True
            if key == "ecl":
                ecl = True
            if key == "pid":
                pid = True
print("valid Passports: " + str(valid_counter))
