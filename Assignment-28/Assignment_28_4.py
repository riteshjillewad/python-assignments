##########################################################################################
# Name:        Assignment_28_4.py
# Description: Write a program which accept two filenames from the user, and copy the file
#              contents from existing one to the new one
# Input:       Existing filename, Second one is the new file
# Output:      Display the file contents
# Date:        29-08-2026
# Author:      Ritesh Jillewad
##########################################################################################

import os

def copyFiles(file1, file2):

    with open(file1, "r") as f1:
        content = f1.read()

    print("-" * 30)
    print("COPYING FILE CONTENTS....")
    print("-" * 30)

    with open(file2, "w") as f2:
        f2.write(content)

    print(f"\n{file1} contents:")
    with open(file1, "r") as f1:
        print(f1.read())

    print(f"{file2} contents:")
    with open(file2, "r") as f2:
        print(f2.read())

def main():

    print("Enter original filename: ")
    originalFile = input()

    print("Enter new filename(copy): ")
    newFile = input()

    if not os.path.isfile(originalFile):
        print(f"{originalFile} does not exist!")
        return

    copyFiles(originalFile, newFile)

if __name__ == "__main__":
    main()
