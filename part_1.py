import os
import sys
import threading
import time
import getopt

print ("//////////////////// Welcome to Syrus University Systems ////////////////////")
print ("")  # purpose is to skip a line
print ("")

print ('''Are you a student? If not please exit the system by pressing 3! 
Please press for the relevant input of your choice

1. Student
2. EXIT''')  # ''' to take multiple line print values

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////// C O D E   _   S P A C E   _  1 ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////


inputs = [0, 20, 40, 60, 80, 100, 120]  # The only allowed numbers for the input values the credit scores
sel3 = [1, 2, 3]  # For the main 3 selections


def outcome(pass_grade, defer, fail):  # Outcome list
    three_list = [80, 100, 120]

    if fail in three_list:
        print ("")
        print ("Your Outcome is: Exclude")
        return "Exclude"

    elif 120 >= fail + defer >= 40:
        print ("")
        print ("Your Outcome is: Do not Progress = Module Retriever")
        return "Retriever"

    elif pass_grade == 100:
        print ("")
        print ("Your Outcome is: Progress = Module Trailer")
        return "Trailer"

    else:
        print ("")
        print ("Your Outcome is: Progress")
        return "Progress"


def studentsec():  # Student Section code

    print ("//////////////////// Welcome Fellow Student! ////////////////////")
    print ("")

    try:
        x = int(input("Please enter your Pass score: "))
        while not x in inputs:  # Inputs is the range array above
            print ("")
            print ("Range Error")
            x = int(input("Please enter your Pass score: "))

        y = int(input("Please enter your Defer score: "))
        while not y in inputs:
            print ("")
            print ("Range Error")
            y = int(input("Please enter your Defer score: "))

        z = int(input("Please enter your Fail score: "))
        while not z in inputs:
            print ("")
            print ("Range Error")
            z = int(input("Please enter your Fail score: "))

        # Credit Total Validation Checks
        if x + y + z != 120:
            print("")
            print ("Total Incorrect")
            exit()

        print (outcome(x, y, z))  # Links with the outcome function and provides a result

        print ("")
        print ("~~~~~~~~ Thank you for using our services! ~~~~~~~~")
    except ValueError:
        print ("Character Values are not permitted!")  # CHECK THIS!!!!


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////// C O D E   _   S P A C E   _  1 ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////


a = int(input())  # First Input for selection set
while not a in sel3:
    print ("")
    a = int(input('''Selection numbers have to be between 1 - 2 - 3! 
Please Try Again:

1. Student
2. EXIT
'''))

if a == 1:
    os.system('cls')
    studentsec()  # Calls student section function in Code_Space_1


if a == 2:
    os.system('cls')
    print ("~~~~~~~~~~~~~~~~~~~ Have a Nice Day! ~~~~~~~~~~~~~~~~~~~~~~")
    os._exit  # Exits the code