import random   # Imports random module
import string   # Imports string module

strs = list(string.ascii_letters)  # Gets all english letters
num = [0,1,2,3,4,5,6,7,8,9]    # List of numbers
strs.extend(num) # Adds up numbers to list of letters

i = 0   # Initialise variable for While loop

while True:   # While loop Arg = True to make it run infinitely
   
    i = i + 1   # increment for While loop
    for j in range(1,i+1):   #  Nested loop
        print(random.choice(strs),end = " ")   # Print in line
    print()   # Makes new line

