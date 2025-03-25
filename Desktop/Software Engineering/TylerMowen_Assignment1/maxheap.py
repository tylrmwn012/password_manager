'''Program Title: EECS 348 Assignment 1
   Description: This file simulates a MaxHeap by implementing a priority queue
   Inputs: Contents from each line of the txt file, including:
            role: The level of priority the email has
            email: The string on the current line of code
            date: The date containted within the email
   Outputs: Integer priority of corresponding role (getPriority)
            Integer index of given element's parent (parent)
            Integer index of given element's left child (leftChild)
            Integer index of given element's right child (rightChild)
            True or False depending on whether the heap is empty (isEmpty)
            Integer number of items in the heap (length)
            Formats heap when items are added (moveUp)
            Reformats heap when items have been removed (moveDown)
            Adds email's role, email, and date to heap (add)
            Removes email at top of heap and calls moveDown to reformat heap (pop)
            Returns information for email at top of heap (peek)
   Collaborators: None
   Sources: ChatGpt
   Author: Tyler Mowen
   Creation Date: 29 January, 2025'''

class MaxHeap(): # creates the class MaxHeap() which uses a Max Heap as a means of implementing a priority queue

    '''Author: Tyler Mowen, collaborated with ChatGPT'''
    PRIORITY_ORDER = {"Boss": 5, "Subordinate": 4, "Peer": 3, # dictionary PRIORITY_ORDER pairs each role with their corresponding
                      "ImportantPerson": 2, "OtherPerson": 1} # value; from highest priority to lowest priority

    '''Author: Tyler Mowen'''
    def __init__(self):  # defines function __init__()
        self.heap = [] # initializes self.heap as an empty list. this will act as the inbox for the emails; where emails are stored

    '''Author: Tyler Mowen'''
    def getPriority(self, role): # defines function with parameter role, (string priority), returns the number priority
        return self.PRIORITY_ORDER[role] # returns the integer level of priority based on the role (example returns 5 for "Boss")

    '''Author: Tyler Mowen'''
    def parent(self, index): # defines function parent() with paremeter index, (index of element who's parent we want to find)
        return (index - 1) // 2 # calculates and returns the parent element's index 

    '''Author: Tyler Mowen'''
    def leftChild(self, index):  # defines function leftChild() with parameter index, (index of element who's left child we want to find)
        return (2 * index + 1) # calculates and returns the left child's index

    '''Author: Tyler Mowen'''
    def rightChild(self, index): # defines the function rightChild() with parameter index, (index of element who's right child we want to find)
        return (2 * index + 2) # calculates and return the right child's index

    '''Author: Tyler Mowen'''
    def isEmpty(self):  # defines the function isEmpty
        return len(self.heap) == 0 # returns True if the length of self.heap is 0. False if not equal to 0

    '''Author: Tyler Mowen'''
    def length(self): # defines the function length()
        return len(self.heap) # returns the length of the heap (number of emails in the inbox)

    '''Author: Tyler Mowen, collaborated with ChatGPT'''
    def moveUp(self, index, date): # defines function moveUp() with parameters index and date (date and index of element we want to move up the heap)
        while index > 0: # while loop with the condition that the index is greater than 0
            parent_index = self.parent(index) # sets parent_index equal to the index of the parent element in the heap
            parent_date = self.heap[parent_index][2] # sets parent_date equal to the parent element's date with index [2]
            
            if date[6:] < parent_date[6:]:  # compare year: checks to see if the new year is less than the comparing year
                break # if so, leave the loop; the new element is placed
            elif date[6:] > parent_date[6:]:  # compare year: checks to see if the new year is greater than the comparing year
                pass # passes to the next section of the if statement
            elif date[:2] < parent_date[:2]:  # compare month: checks to see if the new month is less than the comparing month
                break # if so, leave the loop; the new element is placed
            elif date[:2] > parent_date[:2]:  # compare month: checks to see if the new month is greater than the comparing month
                pass # passes to the next section of the if statement
            elif date[3:5] < parent_date[3:5]:  # compare day: checks to see if the new day is less than the comparing day
                break # if so, leave the loop; the new element is placed
            elif date[3:5] > parent_date[3:5]: # compare day: checks to see if the new day is greater than the comparing day
                pass # passes to the next section of the if statement
            else:
                break # leave the loop; the new element is placed since the dates are equal

            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index] # if day, month, and year of new date are greater, swap the values
            index = parent_index # increment to the next parent and compare again with the while loop. the new date's index if the old parent index

    '''Author: ChatGPT'''
    def moveDown(self, index): # defines function moveDown() with parameter index
        size = self.length() # sets size as the length of the entire heap
        largest = index # sets largest equal to the index passed into the function
        left_child = self.leftChild(largest) # sets left_child equal to the index of the left child of the largest index
        right_child = self.rightChild(largest) # sets right_child equal to the index of the right child of the largest index

        if left_child < size: # if statement with the condition that left_child index is smaller than the size of the whole heap
            left_child_date = self.heap[left_child][2] # sets left_child_date equal to the date associated with the  left_child index
            current_date = self.heap[largest][2] # sets current_date equal to the date associated with the index largest

            if left_child_date[6:] > current_date[6:]: # if statement with condition that the year of the left child date is greater than the current index's year
                largest = left_child # sets largest equal to the index for the left child
            elif left_child_date[6:] == current_date[6:]:  # if statement with condition that the year of the left child date is equal to the current index's year
                if left_child_date[:2] > current_date[:2]:  # if statement with condition that the month of the left child date is greater than the current index's month
                    largest = left_child # sets largest equal to the index of the left child
                elif left_child_date[:2] == current_date[:2]: # if statement with condition that the month of the left child date is equal to the current index's month
                    if left_child_date[3:5] > current_date[3:5]: # if statement with the condition that the left child's day is greater than the current index's day
                        largest = left_child # sets largest equal to the index of the left child

        if right_child < size: # if statement with the condition that the right child is less than the size of the whole heap
            right_child_date = self.heap[right_child][2] # sets right_child_date equal to the date associated with the current right_child
            current_date = self.heap[largest][2] # sets current_date equal to the date associated with the index largest

            if right_child_date[6:] > current_date[6:]: # if statement with condition that the year of the right child date is greater than the current index's year
                largest = right_child # sets largest equal to the index of the right child
            elif right_child_date[6:] == current_date[6:]:  # if statement with condition that the year of the right child date is equal to the current index's year
                if right_child_date[:2] > current_date[:2]:  # if statement with condition that the month of the right child date is greater than the current index's month
                    largest = right_child # sets largest equal to the index of the right child
                elif right_child_date[:2] == current_date[:2]: # if statement with condition that the month of the right child date is equal to the current index's month
                    if right_child_date[3:5] > current_date[3:5]:  # if statement with the condition that the right child's day is greater than the current index's day
                        largest = right_child # sets largest equal to the index of the right child

        if largest != index: # if statement with the condition that the largest index is not equal to the index passed into the function
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index] # if so, swap the elements at index index with elements at index largest
            self.moveDown(largest) # pass largest into the moveDown function as the index and repeat 

    '''Author: Tyler Mowen, collaborated with ChatGPT'''
    def add(self, role, item, date): # defines function add() with parameters role, item, and date
        priority = self.getPriority(role) # sets variable priority equal to the number value of the emails sender
        self.heap.append((priority, item, date))  # adds the priority, email, and date to the end of the heap
        self.moveUp((len(self.heap) - 1), date)  # sends the actual length of the heap and the date to moveUp so the 
                                                 # email can be moved to the proper placement in the max heap

    '''Author: Tyler Mowen, collaborated with ChatGPT'''
    def pop(self): # defines function pop()
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0] # swaps the first and last elements
        self.heap.pop() # removes and retruns last item in the heap
        if self.heap: # if the heap does have elements, however,
            self.moveDown(0) # call the moveDown function to reformat the heap

    '''Author: Tyler Mowen, collaborated with ChatGPT'''
    def peek(self): # defines function peek()
        return self.heap[0][1] # if there are elements, returns the last item's email on the heap