##########################################################################################
# Name:        Assignment_29_3.py
# Description: Write a program which accepts filename and string through command line
#              arguments and returns the frequency of that string
# Input:       filename, string
# Output:      Frequency of the string
# Date:        29-08-2026
# Author:      Ritesh Jillewad
##########################################################################################

import os
import sys

def countFrequency(file, target_string):
    counter = 0

    with open(file, "r") as f:
        for line in f:
            words = line.split()

            for word in words:
                if word == target_string:
                    counter += 1

    return counter

def main():

    if len(sys.argv) != 3:
        print("Invalid number of arguments!")
        print("TRY: filename target_string")
        return

    file = sys.argv[1]
    target_string = sys.argv[2]

    if not os.path.isfile(file):
        print(f"{file} does not exist!")
        return

    ret = countFrequency(file, target_string)
    print(f"Frequency of {target_string} in {file}: {ret}")

if __name__ == "__main__":
    main()