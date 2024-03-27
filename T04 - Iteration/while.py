"""
create a variable to get users input
create a variable for storing the addition of the numbers user inputted
create a variable to count number of times user entered something (excluding -1)
create a while loop to check if the user enters -1. else run the loop
get the users input 
if the user has not entered -1  add 1 to counter and add the user input to buffer
in the look check if the user has entered -1 to give them a good job message and print out an average
"""
num1 = 0 #variable for user input
buffNum = 0 #variable to store sum of buffNum and num1
counter =0 #counter to set number of time user entered value except -1
while num1 != -1:#check if the value is -1, if not exicutes the loop
    num1 =int(input("Please input a number: "))#user input as an integer
    
    if num1 != -1: # checks if user has entered -1. If not, runs the if statement
        buffNum += num1 #adds num1 to buffNum
        counter += 1 #adds 1 to counter
    else:
        print("Good Job!") #when user enters -1 runs the else statement and outputs ood job tot he user
        print("Average:", buffNum/counter) # prrints the average of the numbers entered
        break # exits out of the loop
