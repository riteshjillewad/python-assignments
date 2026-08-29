##########################################################################################
# Name:        Assignment_28_2.py
# Description: Write a program which accept filename from user and counts total number of
#              words in the file
# Input:       Filename
# Output:      Total number of words
# Date:        29-08-2026
# Author:      Ritesh Jillewad
##########################################################################################

import os

def countWords(fileName):
    
    """
    wordCount = 0

    for each line:
        split line into words
        for each word:
            increase wordCount by 1
            
    return wordCount
    """
    
    with open(fileName, "r") as f:
        wordCount = 0
        
        for line in f:
            # split the line in words
            words = line.split()            # default behaviour: by whitespace
            
            # now we iterate through the words
            for word in words:
                wordCount += 1
            
        return wordCount
        

def main():
    print("Enter filename: ")
    fileName = input()
    
    if not os.path.isfile(fileName):
        print(f"{fileName} does not exist!")
        return
    
    ret = countWords(fileName)
    print(f"Number of words in {fileName}: {ret}")
    
if __name__ == "__main__":
    main()