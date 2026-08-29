##########################################################################################
# Name:        Assignment_29_2.py
# Description: Write a program which accepts two filenames through command line arguments
#              and compares the contents of both files
#              If both files contain same content: display success, otherwise failure
# Input:       file1, file2
# Output:      Compare file contents
# Date:        29-08-2026
# Author:      Ritesh Jillewad
##########################################################################################

import os
import sys

def compareFiles(file1, file2):

    with open(file1, "r") as f1:
        with open(file2, "r") as f2:

            if f1.read() != f2.read():
                print("FAILED")
                return

    print("SUCCESS")

def main():

    if len(sys.argv) != 3:
        print("Invalid number of arguments!")
        print("TRY: file1 file2")
        return

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    if not os.path.isfile(file1):
        print(f"{file1} does not exist!")
        return

    if not os.path.isfile(file2):
        print(f"{file2} does not exist!")
        return

    compareFiles(file1, file2)

if __name__ == "__main__":
    main()