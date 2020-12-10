#!/usr/bin/python3

lines = None
with open("day_2_input", "r") as f:
    lines = f.readlines()

valid_counter = 0

for line in lines:
    letter_counter = 0
    line_array = line.split(" ")
    index_array = line_array[0].split("-")
    letter = line_array[1].replace(":", "")
    code = line_array[2]
    first_index = int(index_array[0])
    second_index = int(index_array[1])

    if len(code) >= second_index + 1:
        if code[first_index - 1] == letter and code[second_index - 1] != letter or code[first_index - 1] != letter and code[second_index - 1] == letter:
            valid_counter += 1

print("Number of valid Password: " + str(valid_counter))