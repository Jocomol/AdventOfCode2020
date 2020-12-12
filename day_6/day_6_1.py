#!/usr/bin/python3

lines = None
with open("day_6_input", "r") as f:
    lines = f.readlines()

current_set = set()
total_score = 0

for line in lines:
    if line != "\n":
        line = line.strip("\n")
        if len(line) == 1:
            current_set.add(line)
        else:
            for element in line:
                current_set.add(element)
    else:
        total_score += len(current_set)
        current_set = set()

total_score += len(current_set)
print(total_score)
