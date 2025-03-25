'''Program Title: EECS 348 Assignment 3
   Description: This program takes a user's file and their chosen regex pattern, verifies that
                the file can be opened and that the regex pattern is valid, then returns 
                whether there were no matches found and if therre were matches found, displays all of the matches 
                found on the individual line.
   Inputs: Takes user's file as filename, and the regex they want to search for
           in the format /.../
   Outputs: Returns whether there are no matches, or the line where the matches were found;
            displays the matches found on current line.
   Collaborators: None
   Sources: https://www.w3schools.com/python/python_regex.asp 
            (w3schools.com), ChatGPT
   Author: Tyler Mowen
   Creation Date: 18 February, 2025'''

import re # Imports the re library bringing in its functions for handling regex patterns

'''Program Authored by Tyler Mowen; Changed to class format by ChatGPT'''
class RegexReader: # Defines the class RegexReader

    ''' Author: Tyler Mowen'''
    def __init__(self): # Defines the function __init__ with parameter self
        self.filename = "" # Initialize self.filename as an empty string
        self.pattern = "" # Initialize self.pattern as an empty string

    '''Author: Tyler Mowen'''
    def get_filename(self): # Defines the function get_filename with parameter self
        self.filename = input("Please enter the filename: ") # Sets self.filename equal to the users string input; should be the name of a file

    '''Author: Tyler Mowen'''
    def read_file(self): # Defines function read_file with parameter self
        try: # Try to open the user's file to read as file
            with open(self.filename, 'r') as file: # Opens the user's file at filename to read as file
                return file.readlines() # Returns a list of each line in the file as a list item
        except FileNotFoundError: # Raises exception if the file cannot be opened 
            print("Error: Unable to open file.") # Displays message that the file couldn't be opened
            return None # Returns None

    '''Author: ChatGPT'''
    def get_pattern(self): # defines the function get_pattern with parameter self
        regexpattern = input("Please enter a regular expression with the format /../: ") # Set regexpattern equal to the user's input in the format /.../
        if not (regexpattern.startswith("/") and regexpattern.endswith("/")): # Checks if the input is in the correct format. If not...
            print("Error: Invalid regex pattern.") # Display the error that the regex pattern was invalid
            return None # Returns none
        self.pattern = regexpattern[1:-1] # Sets self.pattern equal to the regexpattern without the // if it's in the correct format
        
        try: # Try compiling self.pattern into a regex object
            return re.compile(self.pattern) # Return the compiled regex option
        except re.error: # If it cannot be compiled into a valid regex pattern
            print("Error: Invalid regex pattern.") # Print that the regex pattern is invalid
            return None # Return None

    '''Author: ChatGPT'''
    def search_pattern(self, lines, compiled_pattern):
        match_found = False  # Set match_found equal to False
        for line_number, line_content in enumerate(lines, start=1):  # Unpack the tuple properly
            matches = compiled_pattern.findall(line_content)  # Pass only the line content to findall()
            if matches:  # If there are matches
                match_found = True  # Set match_found equal to True
                print(f"Line {line_number}: Match found:")  # Display that a match was found on the current line
                for match in matches:  # For each match in the list of matches
                    print(f"  {match} \n")  # Display the matches from the current line
            else:
                print(f"Line {line_number}: No match found \n")

        if not match_found:  # If match_found still equals False
            print("No matches found in the file.")  # Display that no matches were found

    ''' Author: Tyler Mowen'''
    def run(self): # Defines function run with parameter self
        self.get_filename() # Call the function get_filename()
        lines = self.read_file() # set lines equal to the function read_file()
        if lines is None: # If lines is none...
            return # Return nothing
        
        compiled_pattern = self.get_pattern() # Set compiled_pattern equal to the functuon get_pattern()
        if compiled_pattern is None: # If compiled_pattern is None...
            return # Return nothing
        
        self.search_pattern(lines, compiled_pattern) # Call the function search_pattern with parameters lines and compiled_pattern

reader = RegexReader() # Sets variable reader equal to the function RegexReader (calls the funciton)
reader.run() # Runs the called function for the user