#!/usr/bin/python3

lines = None
with open("day_6_input", "r") as f:
    lines = f.readlines()

answer_list = []
current_string = ""
total_score = 0
questions = ["a", "b", "c", "y", "x", "z"]

for i in range(len(lines)):
    if lines[i] != "\n":
        line = lines[i].strip("\n")
        current_string += line
    else:
        answer_list.append(current_string)
        current_string = ""

if current_string != "":
    answer_list.append(current_string)

for entry in answer_list:
    score = 0
    for question in questions:
        if question in entry:
            score += 1
    total_score += score

print(total_score)
