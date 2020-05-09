import os
import sys
import threading
import time
import getopt


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////// C O D E   _   S P A C E   _  1 ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

inputs = [0, 20, 40, 60, 80, 100, 120] # The numbers that are only applicable for for inputs 

print ("//////////////////// Welcome Fellow Teacher! ////////////////////")
print ("")

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



def teachsec() :

    print ("")

    try:
        pass_grade = int(input("Please enter your Pass score: "))
        while not pass_grade in inputs:  
            print ("")
            print ("Range Error")
            pass_grade = int(input("Please enter your Pass score: "))

        defer = int(input("Please enter your Defer score: "))
        while not defer in inputs:
            print ("")
            print ("Range Error")
            defer = int(input("Please enter your Defer score: "))

        fail = int(input("Please enter your Fail score: "))
        while not fail in inputs:
            print ("")
            print ("Range Error")
            fail = int(input("Please enter your Fail score: "))

        # Credit Total Validation Checks
        if pass_grade + defer + fail != 120:
            print("")
            print ("Total Incorrect")
            
            pass_grade = int(input("Please enter your Pass score: "))
            while not pass_grade in inputs:
                print ("")
                print ("Range Error")
                pass_grade = int(input("Please enter your Pass score: "))

            defer = int(input("Please enter your Defer score: "))
            while not defer in inputs: 
                print ("")
                print ("Range Error")
                defer = int (input ("Please enter your Defer score: "))

            fail = int(input("Please enter your fail score: "))
            while not fail in inputs: 
                print ("")
                print ("Range Error")
                fail = int(input("Please enter your fail score: "))
                            

        #print (outcome(pass_grade, defer, fail))  # Links with the outcome function and provides a result
    except ValueError:
        return False
    return pass_grade, defer, fail


#teachsec()  irrelevant function call

leave = 'running'
progress = 0
trailer = 0
retriever = 0
excluded = 0

while not leave == 'q':
    returned_value = teachsec()

    if returned_value == False:
        print ("Integers Required")

    else:
        pass_grade, defer, fail = returned_value
        answer = outcome(pass_grade, defer, fail)

        if answer == "Exclude":
            excluded += 1

        elif answer == "Retriever":
            retriever += 1

        elif answer == "Trailer":
            trailer += 1

        elif answer == "Progress":
            progress += 1
    leave = (input('''To quit, press 'Q' (In lower case) and view a histogram of the total results list
    To continue entering values, press ENTER key'''))

print ("------------------ F I N A L     R E S U L T ------------------")
print ("")
print (f"Progress {progress}: ", '*' * progress)
print (f"Trailing {trailer}: ", '*' * trailer)
print (f"Retreiver {retriever}: ", '*' * retriever)
print (f"Retreiver {excluded}: ", '*' * excluded)
print ("")
print ("")
print (f"{excluded + retriever + trailer + progress} is the outcomes in total")
print ("~~~~~~~~~~~~~~~~~~ Thank you for using our services! ~~~~~~~~~~~~~~~~~~")

# Application exits here 

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////// C O D E   _   S P A C E   _  1 ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

