
#Create a variable to store the users input
str_manip = input("Please enter a sentence of your liking:")
#Length of the variable str_manip
print("Length of the string is:", len(str_manip))

#Find the last letter of variable str_manipand replaced with @
print("The last letter of the string is:",str_manip[-1])

# stores the last character of the string
lastLetter = str_manip[-1]
#Replace the last character of the string with @ and stored it in newString
newString = str_manip.replace(lastLetter, "@")
#prints the date stored in the variable newString
print("Replaced the last letter with @: ",newString)

#Prints the last 3 letters backwords for the variable str_manip
print("The last 3 characters from the string backwords:",str_manip[-1:-4:-1])

#stores first 3 and last 2 characters from the string as a word in variable endsComi
endsComi = str_manip[0:3] + str_manip[-1:-3:-1]
#prints first 3 and last 2 characters from the string as a word
print ("Printing the first 3 and last 2 char from the string:",endsComi)
