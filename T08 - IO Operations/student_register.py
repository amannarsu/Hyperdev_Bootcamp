"""
Write a program that allows a user to register students for an exam venue.
● First, ask the user how many students are registering.
● Create a for loop that runs for that number of students.
● Each time the loop runs the program should ask the user to enter the
next student ID number.
● Write each of the ID numbers to a text file called reg_form.txt
● Include a dotted line after each student ID because this document will be
used as an attendance register, which the students will sign when they
arrive at the exam venue.
"""
#Request an input from the user to chech how many users need to register and stored it in numStudents to itherate the loop
numStudents = int(input("Please enter the number of students to reguster for the exam:"))
#container to store the ids of the new reistration students
idNumbers = ""
#counter for the loop
i = 0

#Opens the file if it exists to read/wright to it
with open('reg_form.txt','r+') as file:

#THis loop with prompt the user for the users Id number based on the user input for number of users above
#This loop stores the data from the user and formats it as requested for the task then stores it to the file
    while i < numStudents:
        #print(f"Num student {i}")
        i += 1
        idNumbers = int(input("Please enter the students id number:"))
        file.write(f"Student-Id: {idNumbers}  Sign: ..........................\n")

#closes the file        
file.close()