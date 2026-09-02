##########################################################################################
# Name:        Assignment_31_4.py
# Description: Write a program that accepts a directory name from the user and counts the
#              number of files inside it every five minutes
# Input:       Directory name
# Output:      Log file
# Date:        02-09-2026
# Author:      Ritesh Jillewad
##########################################################################################

import schedule
import os
import time

from datetime import datetime

def work(dirName):
    fileName = "DirectoryCountLog.txt"
    
    if not os.path.exists(dirName):
        print(f"{dirName} does not exist!")
        return
    
    if not os.path.isdir(dirName):
        print(f"{dirName} is not a directory!")
        return
    
    fileCount = 0

    # We list all the files using os.listdir()
    for file in os.listdir(dirName):
        
        # Join the directory path with the current file name
        fullPath = os.path.join(dirName, file)
        
        # Check if the item is a file
        if os.path.isfile(fullPath):
            fileCount += 1
    
    with open(fileName, 'a') as f:
        
        f.write("=" * 55 + "\n")
        f.write("MARVELLOUS DIRECTORY COUNT LOG".center(55) + "\n")
        f.write("=" * 55 + "\n")
        
        f.write(f"Directory name : {dirName}\n")
        f.write(f"Number of files: {fileCount}\n")
        f.write(f"Date and time  : {datetime.now()}\n")
        
        f.write("=" * 55 + "\n\n")
        
    print("Log updated successfully...")

def main():
    print("Enter directory name(path): ")
    dirName = input()
    
    work(dirName)
    schedule.every(5).minutes.do(work, dirName)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()