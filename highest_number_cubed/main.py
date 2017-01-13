"""This is the entry point of the program."""


def highest_number_cubed(limit):
    for x in range(0, limit):
        cube = x **3
        if (cube < limit):
            y = x
            x += 1
        else:
            return y