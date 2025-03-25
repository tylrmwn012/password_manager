'''Program Title: EECS 348 Assignment 1
   Description: This file reads the user's txt file and calls the email functions to handle the emails for the user
   Inputs: 'Assignment1_Test_File.txt'
   Outputs: Executes EMAIL, COUNT, NEXT, and READ functions
   Collaborators: None
   Sources: ChatGPT
   Author: Tyler Mowen
   Creation Date: 29 January, 2025'''

from emailFunc import EmailFunc # imports the class EmailFunc() from the file emailFunc.py

'''Author: Tyler Mowen'''
def main(): # function main() reads the test file and handles it based on the first word of each line 
    email = EmailFunc() # sets class EmailFunc() equal to the variable email for future use

    '''Author: Tyler Mowen, collaborated with ChatGPT'''
    with open('Assignment1_Test_File.txt', 'r') as file: # opens the file 'Assignment1_Test_File.txt' to read each line ('r') as a file 
            for line in file : # for loop which reads each line in the file (line is equal to each line)

                if line.startswith("EMAIL"): # if statement for if the line begins with "EMAIL"
                    email.EMAIL(line) # reaches into class EmailFunc to uses the function EMAIL(), which takes parameter line, in order to add the email to the inbox (heap)
                
                elif line.startswith("COUNT"): # if statement for if the line begins with "COUNT"
                    print(email.COUNT()) # reaches into the EmailFunc class and prints the function COUNT() to print number of emails in inbox (heap)
                    print() # prints blank line after displaying the number of emails in the inbox
                
                elif line.startswith("NEXT"): # if statement for if the line begins with "NEXT"
                    print(email.NEXT()) # reaches into the EmailFunc class and displays the next email in the heap to the user (sender, subject, date)
                    print() # prints a blank line after displaying the next email to the user
                
                elif line.startswith("READ"): # if statement for if the line begins with "READ"
                    email.READ() # reaches into the class EmailFunc and marks the current email as read, removing it from the heap and formatting the heap without it
                
main() # closes the function main() 