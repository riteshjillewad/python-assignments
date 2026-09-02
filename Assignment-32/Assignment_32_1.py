##########################################################################################
# Name:        Assignment_32_1.py
# Description: Write a program that creates a new text file every minute. The filename should
#              contain the current timestamp
#              The file should contains the following information:
#              1. Filename
#              2. Creation date
#              3. Creation time
# Input:       Void
# Output:      Creates a message
# Date:        02-09-2026
# Author:      Ritesh Jillewad
##########################################################################################
import schedule
import time

def work():
    fileName = "File_" + time.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"
    
    creationDate = time.strftime("%d-%m-%Y")
    creationTime = time.strftime("%H:%M:%S")
    
    with open(fileName, 'w') as f:
        
        f.write("=" * 45 + "\n")
        f.write("FILE CONTENTS".center(45) + "\n")
        f.write("=" * 45 + "\n")
        
        f.write(f"Filename      : {fileName}\n")
        f.write(f"Creation date : {creationDate}\n")
        f.write(f"Creation time : {creationTime}\n")

        f.write("=" * 45 + "\n")
    
    print(f"File created successfully: {fileName}")

def main():
    
    work()
    schedule.every(1).minute.do(work)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
