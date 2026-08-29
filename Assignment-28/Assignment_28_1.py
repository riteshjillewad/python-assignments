##########################################################################################
# Name:        Assignment_28_1.py
# Description: Write a program which accept filename from user and counts how many lines are
#              present in the file
# Input:       Filename
# Output:      Number of lines in file
# Date:        29-08-2026
# Author:      Ritesh Jillewad
##########################################################################################

import os

def countLines(fileName: str) -> int:
    '''
    Functions that takes filename as input, and returns the number of lines in the file
    Input : Filename
    Output: Lines count
    
    Algorithm:
    1. Accept the filename from user
    2. Open the file in read mode
    3. We need count of each line in the file
    4. We can either use for loop, or use readlines() -> returns as list of lines in file
    '''
    
    '''
    RAW LOGIC WITHOUT IN-BUILT
    
    lineCount = 0
    
    with open(fileName, "r") as f:
        for line in f:
            lineCount += 1

    return lineCount
    
    '''
    
    f = open(fileName, "r")
    
    lines = f.readlines()
    print(lines)
    f.close()
    
    return len(lines)
    
def main():
    print("Enter filename: ")
    fileName = input()
    
    if not os.path.isfile(fileName):
        print(f"{fileName} does not exist!")
        return
    
    ret = countLines(fileName)
    print(f"Number of lines in {fileName}: {ret}")
    
if __name__ == "__main__":
    main()