##########################################################################################
# Name:        Assignment_28_3.py
# Description: Write a program which accept filename from user and display the contents
#              of file line by line on the screen
# Input:       Filename
# Output:      Display the file line by line
# Date:        29-08-2026
# Author:      Ritesh Jillewad
##########################################################################################

import os

def displayFile(fileName):
    """
    1. Accept filename from user
    2. Open the file in read mode
    3. Read the file line by line
    4. Display each line on the screen
    """

    print("File contents: ")
    with open(fileName, "r") as f:
        for line in f:
            print(line, end="")

def main():
    print("Enter filename: ")
    fileName = input()

    if not os.path.isfile(fileName):
        print(f"{fileName} does not exist!")
        return

    displayFile(fileName)

if __name__ == "__main__":
    main()