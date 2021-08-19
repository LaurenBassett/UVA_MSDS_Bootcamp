from random import randint
from datetime import *
import time
import re
import enchant 

def validate_string(x):
    #got the idea for this function from https://pynative.com/python-check-user-input-is-number-or-string/
    
    try:
        valx = int(x)
        return("You entered the number " + x + ", not a word.")
    except ValueError:
        try:
            valx = float(x)
            return("You entered the number " + x + ", not a word")
        except ValueError:
            if bool(re.search(r"\s", x)):
                #command from https://www.geeksforgeeks.org/python-check-for-spaces-in-string/
                return("You entered multiple words, not a single word.")
            else:
                d = enchant.Dict("en_US")
                if d.check(x):
                    return("Your word is " + x)
                else:
                    suggestions = d.suggest(x)
                    return("That's not a word. Did you mean: " + suggestions[0] + "?")
def main():
   
    now = datetime.now()
    start = time.time()

    print("Current Time", now.time())
    randomNum = randint(0,1000)
    print("Random Number:" ,randomNum)
    print("Hello World")

    inputStr = str(input("Enter a word: "))
    valString = validate_string(inputStr)
    print(valString)
    
    
    print("\n Now, Input as many things as you would like. Enter an empty line to quit. \n")
    listInput = str(input("> "))
    #Needed a refresher on lists: https://www.w3schools.com/python/python_lists_add.asp
    listOfInputs = []
    while listInput != "":
        listOfInputs.append(listInput)
        listInput = str(input("> "))
    print("\nNow printing your list.......")
    for x in listOfInputs:
        print(x)
    print( "\nTime to run: %s seconds" % (time.time() - start))
main()