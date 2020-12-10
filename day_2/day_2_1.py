#!/usr/bin/python3

lines = None
with open("day_2_input", "r") as f:
    lines = f.readlines()

valid_counter = 0

for line in lines:
    letter_counter = 0
    line_array = line.split(" ")
    min_max_array = line_array[0].split("-")
    letter = line_array[1].replace(":", "")
    code = line_array[2]
    minimum = int(min_max_array[0])
    maximum = int(min_max_array[1])

    for letterInCode in code:
        if letterInCode == letter:
            letter_counter += 1

    if minimum <= letter_counter <= maximum:
        valid_counter += 1

print("Number of valid Password: " + str(valid_counter))