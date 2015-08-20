import sys

def debug_print(information):
    print("DEBUG: ", information, file=sys.stderr)

# get your team & get your board
team = input()
first_row = input()
second_row = input()
third_row = input()

# print out the inputs you're getting
debug_print(team)
debug_print(first_row)
debug_print(second_row)
debug_print(third_row)

# Outputting the coordinates of your board

if second_row[1] == "_":
    print("1 1")
elif first_row[0] == "_":
    print("0 0")
elif third_row[0] == "_":
    print("2 0")
elif first_row[2] == "_":
    print("0 2")
elif second_row[0] == "_":
    print("1 0")
elif first_row[1] == "_":
    print("0 1")
elif third_row[2] == "_":
    print("2 2")
elif second_row[2] == "_":
    print("1 2")
elif third_row[1] == "_":
    print("2 1")
