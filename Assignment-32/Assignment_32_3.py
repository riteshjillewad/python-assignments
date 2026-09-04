##########################################################################################
# Name:        Assignment_32_2.py
# Description: Write a program that reads and displays the contents of a specified text file
#              every minute.
#              Handle the following conditions:
#              1. File does not exists
#              2. File is empty
#              3. Permission is denied
#              4. File cannot be opened
# Input:       fileName
# Output:      File contents
# Date:        04-09-2026
# Author:      Ritesh Jillewad
##########################################################################################

import os
import time

def display_file_contents(file_name):
    try:
        if not os.path.exists(file_name):
            print("Error: File does not exist.")
            return

        if not os.path.isfile(file_name):
            print("Error: Specified path is not a file.")
            return

        if os.path.getsize(file_name) == 0:
            print("Error: File is empty.")
            return

        with open(file_name, "r") as file:
            contents = file.read()

        print("\nFile Contents:")
        print(contents)

    except PermissionError:
        print("Error: Permission denied.")

    except OSError as e:
        print("Error: File cannot be opened.")
        print("Reason:", e)

def main():
    file_name = input("Enter file name: ")

    while True:
        print("\n" + "=" * 50)
        display_file_contents(file_name)
        print("=" * 50)

        print("Waiting for 1 minute...")
        time.sleep(60)

if __name__ == "__main__":
    main()