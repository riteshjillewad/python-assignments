##########################################################################################
# Name:        Assignment_31_3.py
# Description: Write a program that scans specific directory every minute. It should display
#              1. Directory name
#              2. Number of files
#              3. Number of subdirectories
#              4. Date and time of scanning
# Input:       Directory name
# Output:      Directory name, number of files, number of subdirectories, date and time of scanning
# Date:        02-09-2026
# Author:      Ritesh Jillewad
##########################################################################################

import schedule
import time
import os
from datetime import datetime

def work(dirPath):
    if not os.path.exists(dirPath):
        print(f"{dirPath} does not exist!")
        return

    if not os.path.isdir(dirPath):
        print(f"{dirPath} is not a directory!")
        return

    files = 0
    subdirectories = 0

    for item in os.listdir(dirPath):
        fullPath = os.path.join(dirPath, item)

        if os.path.isfile(fullPath):
            files += 1
        elif os.path.isdir(fullPath):
            subdirectories += 1

    print("----------------------------------------")
    print(f"Directory name          : {dirPath}")
    print(f"Total Files             : {files}")
    print(f"Total Sub-directories   : {subdirectories}")
    print(f"Date and Time           : {datetime.now()}")
    print("----------------------------------------")

def main():
    print("Enter directory path: ")
    directoryPath = input()

    work(directoryPath)
    schedule.every(1).minute.do(work, directoryPath)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()