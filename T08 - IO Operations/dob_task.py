"""
Create a new Python file in the Dropbox folder for this task, and call it
dob_task.py.

In your Python file, write a program that reads the data from the text file
provided (DOB.txt) and prints it out in two different sections.

"""
#Variable that will hold the name field from the txt file
nameField = ""

#Variable that will hold the date of birth field from the txt file
dobField = ""

#Variable that will hold the name field thats been sliced and then joined (first and last name)
ft_NameField = ""

#Variable that will hold the Date of birth thats been sliced and then joined (date, month and year)
ft_DobField = ""

#Opens the file Dob.txt in read only mode with encoding utf-8 and stores it in a variable holder 'file'
with open('DOB.txt', 'r', encoding = 'utf-8') as file:

#for loop that reads the data from file line by line, splits the data by spaces and stores them into nameField(first 2 words) and dobField variables(last 3 fields)
# this is then joined and add line breaks to match format from the task as requested and stored in ft_NameField and ft_DOBField    
    for line in file:
       nameField = line.split()[:2]
       ft_NameField += "\n" + " ".join(nameField)
       dobField = line.split()[2:]
       ft_DobField += "\n" + " ".join(dobField)

#Prints the formatted names on the screen      
print (f"\nName\n{ft_NameField}\n")
#Prints the formatted DOBs on the screen
print (f"\nBirthdate\n{ft_DobField}\n")
