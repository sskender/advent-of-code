import math
import sys

coded_seats = sys.stdin.read().split("\n")[:-1]


def get_new_range(letter, a, b):
    A = ["F", "L"]
    B = ["B", "R"]
    if letter in A:
        b = a + (b - a) // 2
    elif letter in B:
        a = math.ceil(a + (b - a) / 2)
    else:
        raise Exception("Invalid row letter")
    return (a, b)


def get_seat_number(coded_seat_number):
    row_range = (0, 2**7-1)
    for letter in coded_seat_number[:7]:
        row_range = get_new_range(letter, row_range[0], row_range[1])

    column_range = (0, 2**3-1)
    for letter in coded_seat_number[7:]:
        column_range = get_new_range(letter, column_range[0], column_range[1])

    return row_range[0] * 8 + column_range[0]


decoded_seats = list()
for coded_seat in coded_seats:
    decoded_seats.append(get_seat_number(coded_seat))

print("Max seat ID: {}".format(max(decoded_seats)))
