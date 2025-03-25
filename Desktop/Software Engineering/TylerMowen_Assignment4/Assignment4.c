/* Program Title: EECS 348 Assignment 4
   Description: This file reads the user's txt file, handles the text line by line using
                a maxheap priority queue, then displays either the number of emails or the content
                of the next email. User may also mark emails as read.
   Inputs: 'Assignment1_Test_File.txt'
   Outputs: Executes EMAIL, COUNT, NEXT, and READ functions
   Collaborators: ChatGPT
   Sources: ChatGPT
   Author: Tyler Mowen
   Creation Date: 10 March, 2025    */

#include <stdio.h> // Import functions from stdio such as printf()
#include <string.h> //Import function from string such as strcmp()

#define MAX_EMAILS 100 // Define maximum number of emails allowed



// MaxHeap Class converted to C from Python ===>


/* Author: Tyler Mowen */
#define BOSS_PRIORITY 5 // Define priority level of boss
#define SUBORDINATE_PRIORITY 4 // Define priority level of subordinate
#define PEER_PRIORITY 3 // Define priority level of peer
#define IMPORTANT_PERSON_PRIORITY 2 // Define priority level of important person
#define OTHER_PERSON_PRIORITY 1 // Define priority level of other person

/* Author: ChatGPT */
typedef struct { // Declare Email structure variables
    char role[100]; // Initialize empty string array role with max length 100
    char item[500]; // Initialize empty string array item with max length 500
    char date[20]; // Initialize empty string array date with max length 20
    int priority; // Initialize variable priority as integer
} Email; // Define structure as Email

/* Author: ChatGPT */
typedef struct { // Declare MaxHeap structure variables
    Email emails[MAX_EMAILS]; // Initialize array emails with max length MAX_EMAILS
    int size; // Initialize variable size as an integer
} MaxHeap; // Define structure as MaxHeap

/* Author: Tyler Mowen */
void initHeap(MaxHeap* heap) { // Define function initHeap with parameter heap
    heap->size = 0; // Initialize heap with size of 0
} // Close function initHeap

/* Author: ChatGPT */
void swap(Email* a, Email* b) { // Define function swap with parameters a and b
    Email temp = *a; // Define temp as pointer a
    *a = *b; // Declare a as pointer to pointer b
    *b = temp; // Declare b as pointer to temp
} // Close function swap()

/* Author: Tyler Mowen */
int getPriority(const char* role) { // Define function getPriority with parameter role, from the email line
    if (strcmp(role, "Boss") == 0) return BOSS_PRIORITY; // Return boss priority if strcmp returns 0
    if (strcmp(role, "Subordinate") == 0) return SUBORDINATE_PRIORITY; // Return subordinate priority if strcmp returns 0
    if (strcmp(role, "Peer") == 0) return PEER_PRIORITY; // Return peer priority if strcmp returns 0
    if (strcmp(role, "ImportantPerson") == 0) return IMPORTANT_PERSON_PRIORITY; // Return important person priority if strcmp returns 0
    return OTHER_PERSON_PRIORITY; // Otherwise, return value associated with other person
} // Close getPriority function

/* Author: ChatGPT */
int compareDate(const char* date1, const char* date2) { // Define function compareDate with parameters date1 and date2

    if (strncmp(date1 + 6, date2 + 6, 4) != 0) { // If the years compared are not equal
        return strncmp(date1 + 6, date2 + 6, 4); // Compare year section
    }

    if (strncmp(date1 + 3, date2 + 3, 2) != 0) { // If the months are not equal
        return strncmp(date1 + 3, date2 + 3, 2); // Compare month section
    }

    return strncmp(date1, date2, 2); // Compare day section; return whether it's equal or not
} // Close function

/* Author: ChatGPT */
void heapifyUp(MaxHeap* heap, int index) { // Define heapifyUp function with parameters heap and given index
    if (index > 0) { // If index value is greater than 0...
        int parentIndex = (index - 1) / 2; // Initialize parentIndex variable as (index minus one) divided by 2
        int dateComparison = compareDate(heap->emails[index].date, heap->emails[parentIndex].date); // Initialize dateComparison as value returned from 
                                                                                                    // compareDate of index and parentIndex

        if (heap->emails[index].priority > heap->emails[parentIndex].priority || 
            (heap->emails[index].priority == heap->emails[parentIndex].priority && dateComparison > 0)) { // If emails index index's priority is greater than emails index priorityIndex's priorty, 
                                                                                                            // or they are equal AND dateComparison is greater than 0...
            swap(&heap->emails[index], &heap->emails[parentIndex]); // Swap emails index index with emails inndex parentIndex
            heapifyUp(heap, parentIndex); // Recursively call heapifyUp with heap and parentIndex
        } // Close if statement
    } // Close if statement
} // Close heapifyUp function

/* Author: ChatGPT */
void heapifyDown(MaxHeap* heap, int index) { // Define function heapifyDown with parameters heap and index
    int left = 2 * index + 1; // Initialize left as double index plus 1
    int right = 2 * index + 2; // Initialize right as double index plus 2
    int largest = index; // Initialize largest as index

    if (left < heap->size) { // If left is less than the heap's size...
        int dateComparison = compareDate(heap->emails[left].date, heap->emails[largest].date); // Set dateComparison equal to the value returned from compareDate left and largest

        if (heap->emails[left].priority > heap->emails[largest].priority ||
            (heap->emails[left].priority == heap->emails[largest].priority && dateComparison > 0)) {   // If emails index left's priority is greater than emails index largest's priorty, 
                                                                                                            // or they are equal AND dateComparison is greater than 0...
            largest = left; // Set largest equal to left
        } // Close if statement
    } // Close if statement

    if (right < heap->size) { // If right is less than the heap's size...
        int dateComparison = compareDate(heap->emails[right].date, heap->emails[largest].date); // Set dateComparison equal to the value returned from compareDate right and largest

        if (heap->emails[right].priority > heap->emails[largest].priority ||
            (heap->emails[right].priority == heap->emails[largest].priority && dateComparison > 0)) {   // If emails index right's priority is greater than emails index largest's priorty, 
                                                                                                            // or they are equal AND dateComparison is greater than 0...
            largest = right; // Set largest equal to right
        } // CLose if statement
    } // Close if statement

    if (largest != index) { // If largest is not equal to index...
        swap(&heap->emails[index], &heap->emails[largest]); // Swap emails index index with emails index largest
        heapifyDown(heap, largest); // Recursively call heapifyDOwn with largest as index
    } // Close if statement
} // Close heapifyDown function

/* Author: ChatGPT */
void addEmail(MaxHeap* heap, const char* role, const char* item, const char* date) { // Define function addEmail with parameters heap, role, item, and date
    if (heap->size >= MAX_EMAILS) { // If the size of the heap is greater than or equal to MAX_EMAILS...
        printf("Heap is full!\n"); // Display that the heap is full
        return; // Return nothing
    } // CLose if statement

    int priority = getPriority(role); // Initialize priority as the returned value from getPriority with parameter role

    strcpy(heap->emails[heap->size].role, role); // copy emails index size's role and store in role
    strcpy(heap->emails[heap->size].item, item); // copy emails index size's item and store in item
    strcpy(heap->emails[heap->size].date, date); // copy emails index size's date and store in date
    heap->emails[heap->size].priority = priority; // set emails index size's priority equal to priority

    heapifyUp(heap, heap->size); // Call heapifyUp with parameters heap and size of heap
    heap->size++; // Increment the size of the heap by one
}

/* Author: Tyler Mowen */
Email peekEmail(MaxHeap* heap) { // Define function peekEmail with parameter heap
    if (heap->size > 0) { // If heap's size is greater than 0
        return heap->emails[0]; // Return emails index 0
    } // Close if statement
    Email empty = {"", "", "", 0}; // Set empty equal to the set of empty strings
    return empty; // Return empty 
} // Close function

/* Author: Tyler Mowen */
void popEmail(MaxHeap* heap) { // Define function popEmail with parameter heap
    if (heap->size == 0) { // If the size of the heap is equal to zero...
        return; // Return nothing
    } // Close if statement

    heap->emails[0] = heap->emails[heap->size - 1]; // set emails index 0 as emails index size of the heap minus 1
    heap->size--; // Decrement the heap's size
    heapifyDown(heap, 0); // call heapifyDOwn with parameters heap and index 0
} // Close function

/* Author: Tyler Mowen */
int isEmpty(MaxHeap* heap) { // Define function isEmpty with parameter heap
    return heap->size == 0; // Return True or False whether the heap's size is zero (empty)
} // Close function

/* Author: Tyler Mowen */
int heapSize(MaxHeap* heap) { // Define function heapSize with parameter heap
    return heap->size; // Return the size of the heap as an integer
} // CLose function



// EmailFunc Class convered to C from Python ===>



/* Author: ChatGPT */
typedef struct { // Declare EmailFunc structure variables 
    MaxHeap heap; // Define heap as array
} EmailFunc; // Define structure as EmailFunc

/* Author: Tyler Mowen */
void initEmailFunc(EmailFunc* emailFunc) { // Define function initEmailFunc with parameter emailFunc
    initHeap(&emailFunc->heap); // Initialize heap with initheap with parameter heap
} // Close function

/* Author: Tyler Mowen */
void countEmails(EmailFunc* emailFunc) { // Define function countEmails with parameter emailFunc
    printf("There are %d emails to read.\n", heapSize(&emailFunc->heap)); // Display that there are N amount of emails to read
    printf("\n") ; // PRint blank line
} // CLose function

/* Author: ChatGPT */
void nextEmail(EmailFunc* emailFunc) { // Define function nextEmail with parameter emailFunc...
    if (isEmpty(&emailFunc->heap)) { // If the heap of emails has nothing...
        printf("Inbox is empty.\n"); // Display that the inbox has no emails
        return; // Return nothing
    } // CLose if statement

    Email next = peekEmail(&emailFunc->heap); // Set next equal to peekEmail function with parameter heap
    printf("Next email:\n   Sender: %s\n   Subject: %s\n   Date: %s\n", next.role, next.item, next.date); // Display the next email's sender, subject, and date
    printf("\n") ; // Print blank line
} // Close function nextEmail

/* Author: Tyler Mowen */
void readEmail(EmailFunc* emailFunc) { // Define readEmail function with parameter emailFunc (the heap)
    if (!isEmpty(&emailFunc->heap)) { // If the line is not empty
        popEmail(&emailFunc->heap); // Remove the email from the heap
    } // Close if statement
} // Close readEmail function

/* Author: ChatGPT */
void email(EmailFunc* emailFunc, const char* line) { // 
    if (strncmp(line, "EMAIL", 5) == 0) { // If line begins with EMAIL...
        char role[100], item[500], date[20]; // Define string arrays role, item, and date

        sscanf(line + 6, "%[^,],%[^,],%s", role, item, date); // Take inputs of role, item, and date from the line seperated by commas

        addEmail(&emailFunc->heap, role, item, date); // Add email's role, item, and date to the heap
    } // Close if statement
} // Close function email



/* Author: Tyler Mowen */
#define MAX_LINE_LENGTH 1024 // Define the maximum length of each line in the text file

/* Author: Tyler Mowen */
int main() { // Define the main function which takes in the text file and executes the four main email functions
    EmailFunc emailFunc; // Define emailFunc with structure from EmailFunc
    initEmailFunc(&emailFunc); // Call function initEmailFunc with parameter emailFunc

    FILE *file = fopen("Assignment1_Test_File.txt", "r"); // Open file for reading 
    if (file == NULL) { // If file is empty or cannot be opened
        printf("Could not open file: Assignment1_Test_File.txt\n"); // Display error message to user
        return 1; // Return 1 
    } // Close if statement

    char line[MAX_LINE_LENGTH]; // Define string array line with size MAX_LINE_LENGTH
    while (fgets(line, sizeof(line), file)) { // While there is content on the current line of code...

        line[strcspn(line, "\n")] = 0;  // Sets line index strcspn(line, "\n") equal to zero

        if (strncmp(line, "EMAIL", 5) == 0) { // Checks that the line begins with EMAIL
            email(&emailFunc, line); // Call email function with parameters emailFunc and line
        } else if (strncmp(line, "COUNT", 5) == 0) { // Checks that the line begins with COUNT
            countEmails(&emailFunc); // Calls the countEmails function to return the number of emails left in the inbox
        } else if (strncmp(line, "NEXT", 4) == 0) { // Checks that the line begins with NEXT
            nextEmail(&emailFunc); // Call the nextEmail function to display the next email in the heap
        } else if (strncmp(line, "READ", 4) == 0) { // Checks that the line begins with READ
            readEmail(&emailFunc); // Call readEmail to remove the email from the heap
        } // Close else if
    } // Close while loop

    fclose(file); // Close the file since we're finished reading each line
    return 0; // Return 0
} // Close int main
