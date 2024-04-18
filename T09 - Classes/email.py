### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

    # Declare the class variable, with default value, for emails. 
 
    # Initialise the instance variables for emails.

    # Create the method to change 'has_been_read' emails from False to True.
class email:

    
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

# --- Lists --- #
# Initialise an empty list to store the email objects.


# --- Functions --- #
# Build out the required functions for your program.
    def mark_as_read(self):
        self.has_been_read = True
inbox = []
def populate_inbox():
    
    # Create 3 sample emails and add it to the Inbox list. 

    inbox.append(["office@youroffice.com","Reset your password","Hi\nPlease reset your computer password as soon as possible!\nRegards,\nTech Support Team"])
    inbox.append(["school@yourcouncil.com","Parent and Teacher's meeting","Hi\nThe Meeting is tomorrow at 2pm. There will be tea and snacks\nKind regards\nSchool's Principle"])
    inbox.append(["wife@gmail.com","Bring chicken","Hi babes\nPlease bring chicken for dinner from KFC. The kids also want fries with 2 Oreo Icecreams\nxxxx\nWife"])
    return inbox

def list_emails():
    #i = 0
    subject_list = []
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    for buffer in inbox:
        subject_list.append(buffer[1])
        #i += i
    for count in enumerate(subject_list):
        print(count)


def read_email(index):

    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    if index < len(inbox):
        for count, buffer in enumerate(inbox):
            if count == index:
                ObClass = email(buffer[0],buffer[1],buffer[2])
                ObClass.mark_as_read()
                inbox.pop(index)
                break
        print(f"Current Email>>> [From: {ObClass.email_address}] Subject: {ObClass.subject_line}\nMessage:\n{ObClass.email_content}\n\n<--Marked as read-->")
    
    else:
        print ("Opps! Wrong input\n")
        list_emails()
        index = int(input("\nWhich email would you like to read:"))
        read_email(index)


    
    

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
menu = True
populate_inbox()
list_emails()
# Fill in the logic for the various menu operations.

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
 

    if user_choice == 1:
        # add logic here to read an email
       choice = int(input("Which email would you like to read:"))
       print(choice)
       read_email(choice)

        
    elif user_choice == 2:
        # add logic here to view unread emails
        list_emails()
            
    elif user_choice == 3:
        # add logic here to quit appplication
        print("Ending application")
        break

    else:
        print("Oops - incorrect input.")

