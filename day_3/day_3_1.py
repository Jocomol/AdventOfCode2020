#!/usr/bin/python3

lines = None
with open("day_3_input", "r") as f:
    lines = f.readlines()

length = len(lines)
line_index = 0
letter_index = 0
tree_counter = 0

while line_index < len(lines):
    if lines[line_index][letter_index % 31] == "#":
        tree_counter += 1
    letter_index += 3
    line_index += 1


print("Encountered Trees: " + str(tree_counter))



