"""
Create an variable to store the astrix symbol
Create a variable for to increment the symbol
Create a variable for to decrement the symbol
Create a for loop with the range of 10 since we have 10 iterations
Create an if statement to increase the number of symbols
Create an else to decrease the number of symbols
"""

i= "*" # the symbol we need to replicate
incNum = 0 #variable that will et incremented for printing i
decNum = 5 #variable that will et decremented for printing i
for x in range (10): #for loop to iteherate the if statement nested in here

    if incNum < 5:
        incNum += 1 #increments
        print(incNum * i) # replicates the atrix symbol
    else:
        decNum -= 1 #decrements
        print(decNum * i) # replicates the atrix symbol

        



