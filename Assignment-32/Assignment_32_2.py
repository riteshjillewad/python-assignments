##########################################################################################
# Name:        Assignment_32_2.py
# Description: Write a program that monitors the size of speicified file every 30 seconds
#              1) Writes the following details into: FileSizeLog.txt
#              2) File path
#              3) File size in bytes
#              4) Date and time
#              Handle the situation where the file does not exists
# Input:       Void
# Output:      Log file
# Date:        02-09-2026
# Author:      Ritesh Jillewad
##########################################################################################

import schedule
import os
import time

def work(target_file):
    fileName = "FileSizeLog.txt"
    
    if not os.path.exists(target_file):
        print(f"{target_file} does not exists!")
        return
    
    # similar to our linux stat() function
    fileStats = os.stat(target_file)    
    
    with open(fileName, 'w') as f:
        
        f.write("=" * 55 + "\n")
        f.write("FILE METADATA".center(55) + "\n")
        f.write("=" * 55 + "\n")
        
        f.write(f"Filename               : {target_file}" + "\n")
        f.write(f"File size              : {fileStats.st_size} bytes" + "\n")
        f.write(f"File mode              : {fileStats.st_mode}" + "\n")
        f.write(f"Creation time          : {fileStats.st_ctime}" + "\n")
        f.write(f"Last modification time : {fileStats.st_mtime}" + "\n")
        f.write(f"Last access time       : {fileStats.st_atime}" + "\n")
        
        f.write("=" * 55 + "\n")

def main():
    print("Enter filename to monitor: ")
    targetFile = input()
    
    work(targetFile)
    schedule.every(30).seconds.do(work, targetFile)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()