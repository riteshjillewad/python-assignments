##########################################################################################
# Name:        Assignment_28_5.py
# Description: Write a program which accepts filename from user and checks if that word
#              is present in the file or not
# Input:       filename word to find
# Output:      Check if word present or not
# Date:        29-08-2026
# Author:      Ritesh Jillewad
##########################################################################################

import os
import sys

# THE INPUT WILL BE TAKEN THROUGH COMMAND LINE:
# ex: python Assignment_28_5.py demo.txt word_to_find

def checkWord(fileName, target_word):

    with open(fileName, "r") as f:
        for line in f:
            words = line.split()

            for word in words:
                if word == target_word:
                    return True

    return False

def main():

    if len(sys.argv) != 3:
        print("Invalid number of arguments!")
        print("Please try: filename target_word")
        return

    fileName = sys.argv[1]
    target_word = sys.argv[2]

    if not os.path.exists(fileName):
        print(f"{fileName} does not exist!")
        return

    ret = checkWord(fileName, target_word)

    if ret == True:
        print(f"{target_word} present in {fileName}")
    else:
        print(f"{target_word} not present in {fileName}")

if __name__ == "__main__":
    main()