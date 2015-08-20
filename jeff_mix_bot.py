import sys
import random


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



def rand_choice():
    choice = [0, 1, 2]
    rand1 = random.choice(choice)
    rand2 = random.choice(choice)
    if rand1 == 0:
        if first_row[rand2] == "_":
            print(str(rand1)+" "+str(rand2))
        else:
            rand_choice()
    elif rand1 == 1:
        if second_row[rand2] == "_":
            print(str(rand1)+" "+str(rand2))
        else:
            rand_choice()
    elif rand1 == 2:
        if third_row[rand2] == "_":
            print(str(rand1)+" "+str(rand2))
        else:
            rand_choice()
    else:
        rand_choice()



if second_row[1] == "_":
    print("1 1")
elif third_row[2] == "_":
    print("2 2")
else:
    rand_choice()

