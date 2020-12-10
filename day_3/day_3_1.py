#!/usr/bin/python3

lines = None
with open("day_3_input", "r") as f:
    lines = f.readlines()

length = len(lines)
line_index = 0
letter_index = 0
tree_counter = 0
line_length = len(lines[0])

while True:
    letter_index += 3
    line_index += 1
    if letter_index >= line_length:
        letter_index -= line_length
    if line_index >= length:
        print("Encountered Trees: " + str(tree_counter))
        exit(0)
    try:
        if lines[line_index][letter_index] == "#":
            tree_counter += 1
    except(IndexError):
        print(length, line_index, letter_index, tree_counter, line_length)





