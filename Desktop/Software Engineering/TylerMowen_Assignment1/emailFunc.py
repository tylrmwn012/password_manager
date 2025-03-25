'''Program Title: EECS 348 Assignment 1
   Description: This file performs four functions regarding the user's emails by implementing MaxHeap functions
   Inputs: Each line from assignment txt file
   Outputs: String containing number of emails in the inbox (COUNT)
            String containing the next emails sender, subject, and date
                or Inbox is empty message
   Collaborators: None
   Sources: ChatGPT
   Author: Tyler Mowen
   Creation Date: 29 January, 2025'''

from maxheap import MaxHeap # imports the class MaxHeap from the file maxheap.py

class EmailFunc(): # defines the class EmailFunc() which contains the EMAIL, COUNT, NEXT, and READ functions 

    '''Author: Tyler Mowen'''
    def __init__(self): # function initializes the member variables of the function (only needs to initialize one)
        self.heap = MaxHeap() # initializes the member variable for the class MaxHeap() as self.heap

    '''Author: Tyler Mowen'''
    def COUNT(self): # function COUNT() takes no parameters and returns a string for a message including the number of emails in the inbox (heap)
        return f"There are {self.heap.length()} emails to read." # f-string returns a message using the length of the heap, 
                                                                 # telling the ceo the number of emails left to read.

    '''Author: Tyler Mowen'''
    def NEXT(self): # NEXT() function takes no parameters and returns the next email as a string
        
        try: # 
            email = self.heap.peek() # sets "email" as the next email in the heap (inbox) using the MaxHeap's peek() function 
            parts = email.split(",", 2) # splits the email into three parts based on the comma placement in the line in the txt file
            sender, subject, date = parts # defines the three parts of the email as sender, subject, and date in that order
            return f"Next email:\n   Sender: {sender}  \n   Subject: {subject}  \n   Date: {date}" # returns f-string displaying the next email's
                                                                                                    # sender, subject, and date
        except: #
            return "Inbox is empty" # displays this message if there are no more emails in the CEO's inbox.

    '''Author: Tyler Mowen, collaborated with ChatGPT'''
    def READ(self): # READ() function takes no paremeters and marks the next email to read as read (deletes the biggest priority email from the heap)

        if self.heap.isEmpty(): # if statement with the condition that the heap is empty
            return # no return; heap remains uncahnged since there's nothing to mark as "read"
        self.heap.pop() # if there are emails, however, the pop function returns and removes the email from the heap 

    '''Author: Tyler Mowen, collaborated with ChatGPT'''
    def EMAIL(self, line) : # EMAIL() function takes parameter line (the line being read in the txt file) and adds the email to the heap, without
                            # the "EMAIL " portion of the line
        if line.startswith("EMAIL"): # if statement with the contidion that the line begins with "EMAIL"
            item = line[len("EMAIL "):].strip() # if so, variable item is the line stripped of the "EMAIL " portion of the line
            parts = item.split(",", 2) # variable parts is item split into three parts, which are divided by the two commas
            if len(parts) == 3: # if statement with the condition that there are three parts
                role = parts[0].strip() # variable role is set equal to the first part of variable parts. role refers to the 
                                        # role the email has in the priority value
                date = parts[2].strip() # variable date is set equal to the last of the three sections of item, (the dat ein the form "**-**-****")

                self.heap.add(role, item, date) # this line uses the add function from MaxHeap() to add the email to the proper location in the heap
                                          # based on its role and date