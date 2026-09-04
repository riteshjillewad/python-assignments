##########################################################################################
# Name:        Assignment_32_4.py
# Description: Write a program that copies all .txt files from one directory to another
#              every 10 minutes.
#              The program should:
#              1. Accept source and destination directories
#              2. Validate both directories
#              3. Copy only .txt files
#              4. Maintain log of copied files
#              5. Avoid terminating if one file cannot be copied
# Input:       Source and destination directory
# Output:      Copied and log files
# Date:        04-09-2026
# Author:      Ritesh Jillewad
##########################################################################################

import schedule
import os
import time
import shutil


def work(srcDir, destDir):

    # <--- VALIDATION LOGIC --->
    if not os.path.exists(srcDir):
        print(f"{srcDir} does not exist!")
        return

    if not os.path.exists(destDir):
        print(f"{destDir} does not exist!")
        return

    if not os.path.isdir(srcDir):
        print(f"{srcDir} is not a directory!")
        return

    if not os.path.isdir(destDir):
        print(f"{destDir} is not a directory!")
        return

    # <--- COPY ONLY .TXT FILES --->
    for fileName in os.listdir(srcDir):

        if fileName.lower().endswith(".txt"):
            sourceFile = os.path.join(srcDir, fileName)
            destFile = os.path.join(destDir, fileName)

            if os.path.isfile(sourceFile):
                try:
                    shutil.copy(sourceFile, destFile)

                    # <--- MAINTAIN LOG --->
                    with open("copy_log.txt", "a") as logFile:
                        logFile.write(f"Copied: {sourceFile} -> {destFile}\n")

                    print(f"Copied: {fileName}")

                except PermissionError:
                    print(f"Permission denied: {fileName}")
                except OSError as e:
                    print(f"Unable to copy {fileName}: {e}")

    print("Copy operation completed...")

def main():
    print("Enter source directory: ")
    srcDir = input()

    print("Enter destination directory: ")
    destDir = input()

    # For testing purpose
    work(srcDir, destDir)

    # Run every 10 minutes
    schedule.every(10).minutes.do(work, srcDir, destDir)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()