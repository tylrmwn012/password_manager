'''Program Title: EECS 348 Assignment 2
   Description: This file reads the user's txt file and returns 
                the number of regex matches, displays the first 
                match to the user.
   Inputs: 'Assignment2_Test_File.txt'
   Outputs: Number of matches or none if no matches,    
            displays matches to user.
   Collaborators: None
   Sources: https://www.w3schools.com/python/python_regex.asp 
            (w3schools.com), ChatGPT
   Author: Tyler Mowen
   Creation Date: 1 February, 2025'''

import re # brings the re library into the program to utilize
          # the function findall, or other regex functions

# expressions is a dictionary that contains integer keys associated with
# string values of each regular expression. 
expressions = {1: ".." ,
        2: ".." ,
        3: ".." ,
        4: ".." ,
        5: "^a" ,
        6: "^a" ,
        7: "^a" ,
        8: "^ab" ,
        9: "^ab" ,
        10: "a$" ,
        11: "a$" ,
        12: "a$",
        13: "ma+n" ,
        14: "ma+n" ,
        15: "ma+n" ,
        16: "ma+n" ,
        17: "ma+n" ,
        18: "b" ,
        19: "ac" ,
        20: "^abra" ,
        21: "abra$" ,
        22: "ca." ,
        23: "r.*b" ,
        24: "ac.+a" ,
        25: "cx?a" ,
        26: "[a-fXY0-9]" ,
        27: "[^a-fXY0-9]" ,
        28: "flea|tick" ,
        29: "(My|Your) (dog|cat)" ,
        30: "\\bDogg\\b" ,
        31: "\\d" ,
        32: "\\s" ,
        33: "\\w+"}

def main(): # defines function main

    '''author: Tyler Mowen, collaborated with ChatGPT'''
    with open('Assignment2_Test_File.txt', 'r') as file: # opens the Assignment2_Test_File.txt for reading as file
        lines = file.readlines() # sets line equal to a list version of the test file with each line as an element

    key = 1 # set key equal to integer 1; starts at the first line of the file and moves through each key in expressions

    for line in lines: # for each lines in lines
        match = re.findall(expressions[key], line) # set match equal to re library's function findall, searching for each occurance of
                                                   # expressions[key] in the current line.
        match = [" ".join(m) if isinstance(m, tuple) else m for m in match] # set match equal to the list of all occurances of expressions[key]
                                                                            # in each line.

        if len(match) == 0: # if the length of match is equal to zero...
            print(f"{key}) No match found")  # then there were zero matches , so print No match found message 

        else: # else, if there were one or more matches...
            print(f"{key}) Match found:") # print Match found:
            print("  " + match[0]) # display the first match in the line from the text file
        print() # print blank line after each pass

        key += 1 # increment key buy one
        if key > len(expressions): # if key becomes greater than the length of expressions...
            break # then break the for loop

main() # close the main function
