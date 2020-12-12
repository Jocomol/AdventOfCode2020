#!/usr/bin/python3

import math

lines = None
with open("day_5_input", "r") as f:
    lines = f.readlines()

highest_id = 0


def get_middle(big_number, small_number):
    return math.floor((big_number - small_number) / 2)


def id_from_string(id_string, upper_limit):
    lower_limit = 0
    for i in range(len(id_string) - 1):
        if id_string[i] == "F" or id_string[i] == "L":
            upper_limit -= get_middle(upper_limit, lower_limit)
        elif id_string[i] == "B" or id_string[i] == "R":
            lower_limit += get_middle(upper_limit, lower_limit)

    if lower_limit == upper_limit:
        return lower_limit
    elif id_string[len(id_string) - 1] == "L" or id_string[len(id_string) - 1] == "F":
        return lower_limit
    elif id_string[len(id_string) - 1] == "R" or id_string[len(id_string) - 1] == "B":
        return upper_limit
    else:
        return False


for boarding_id in lines:
    boarding_id = boarding_id.strip("\n")
    row = id_from_string(boarding_id[: 7], 127)
    seat = id_from_string(boarding_id[-3:], 7)
    if seat and row:
        print("row:", row)
        print("seat:", seat)
        seat_id = row * 8 + seat
        print("seat_id:", seat_id)
        print("---")

        if seat_id > highest_id:
            highest_id = seat_id

print("Highest ID: " + str(highest_id))
