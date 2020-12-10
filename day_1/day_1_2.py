#!/usr/bin/python3
lines = None
with open("day_1_input", "r") as f:
    lines = f.readlines()

for line in lines:
    for secondLine in lines:
        for thirdLine in lines:
            if int(line) + int(secondLine) + int(thirdLine) == 2020:
                result = int(line) * int(secondLine) * int(thirdLine)
                print(result)
