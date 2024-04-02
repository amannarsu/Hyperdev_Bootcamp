"""
Write a program that reads in a string and makes each alternate
character into an upper case character and each other alternate character
a lower case character.
e.g. The string “Hello World” would become “HeLlO WoRlD”
"""
string1= "Hello World" #string to convert ever other charater to capital
str1Length = len(string1) #checks the length of the string
newString1 =""

i = 0
while i < str1Length: # converts ever other charater to capital 
    if i % 2 == 0:
        newString1 += string1[i].upper()      
    else:
        newString1 += string1[i]
    i += 1
print (f"<--- Original string: '{string1}' with char lenght of {str1Length}") # prints original string and its length       
print (f"Formatted string results: {newString1} --->") #prints the new string



""" 
Now, try starting with the same string but making each alternative word
lower and upper case.
e.g. The string: “I am learning to code” would become “i AM learning
TO code”.
Tip: Using the split() and join() functions will help.
"""

string2= "I am learning to code"
newString2 =""
x = string2.split() #splits each word based using the whitespace
str2Length = len(x) #checks the length of the string  and stored the value in this string

i = 0
while i < str2Length:#converts each word alternatively as Upper case or Lower case
    if i % 2 == 0:
        newString2 += x[i].lower()      
    else:
       newString2 += x[i].upper()
    i += 1
    newString2 += " "
print (f"<--- Original string: '{string2}' with char lenght of {str2Length}") # prints original string and its length               
print (f"Formatted string results: {newString2} --->")  #prints the new string