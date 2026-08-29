##########################################################################################
# Name:        Assignment_28_6.py
# Description: Write a program which accepts filename from user and checks whether the
#              file exists in the current directory or not
# Input:       Filename
# Output:      Check if file exists or not
# Date:        29-08-2026
# Author:      Ritesh Jillewad
##########################################################################################

import os

def main():

    print("Enter filename: ")
    fileName = input()

    if os.path.isfile(fileName):
        print(f"{fileName} exists in current directory.")
    else:
        print(f"{fileName} does not exist in current directory.")

if __name__ == "__main__":
    main()