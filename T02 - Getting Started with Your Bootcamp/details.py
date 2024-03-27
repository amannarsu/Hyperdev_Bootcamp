"""
--------------pseudocode code------------------
ask the user for their name.
ask for their age.
ask the user their house number
ask the user their House's Street name
print out everything in one line

***Example: This is John Smith. He is 28 years old and lives at house number 42 on Hamilton Street.****
"""
#request user for their name and store it in variable surName
usrName = input("Please enter your name: ")
#request user for their age and store it in variable usrAge
usrAge = input("How old are you? ")
#request user for their house number and store it in variable hsNum
hsNum = input("Enter your House number: ")
#request user for their Street Name and store it in variable stName
stName = input("What is the Street name? ")

#Use the data gathered previously and display the details on the screen in a single sentence
print("Hello", usrName,"thank you for sharing your details!", "You are", usrAge, "years old, and you live at house no.", hsNum, "on", stName, "street.")

