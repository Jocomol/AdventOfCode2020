#!/usr/bin/python3

lines = None
with open("day_3_input", "r") as f:
    lines = f.readlines()

def countTrees(right, down):
    line_index = 0
    letter_index = 0
    tree_counter = 0

    while line_index < len(lines):
        if lines[line_index][letter_index % 31] == "#":
            tree_counter += 1
        letter_index += right
        line_index += down
    return tree_counter

print(countTrees(1,1) * countTrees(3,1) * countTrees(5,1) * countTrees(7,1) * countTrees(1,2))