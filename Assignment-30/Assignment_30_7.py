##########################################################################################
# Name:        Assignment_30_7.py
# Description: Write a program that performs a file backup every hour
#              The program should:
#              1. Accept source file path
#              2. Accept destination directory path
#              3. Copy the source file to destination directory
#              4. Add the current date and time to backup filename
#              5. Write the backup operation details into backup_log.txt
#
#              Example backup filename:
#              Data_25_07_2026_16_30_00.txt
#
#              Example log entry:
#              Backup completed successfully at 25-07-2026 04:30:00 PM
#
#              Use the shutil module for file copying
# Input:       Source file path and destination directory path
# Output:      Backup of source file every hour
# Date:        30-08-2026
# Author:      Ritesh Jillewad
##########################################################################################

import schedule
import time
import shutil
import os
from datetime import datetime

def backup_file(source, destination):

    # Get current date and time
    current_time = datetime.now()

    # Create timestamp for backup filename
    timestamp = current_time.strftime("%d_%m_%Y_%H_%M_%S")

    # Get original filename
    file_name = os.path.basename(source)

    # Separate filename and extension
    name, extension = os.path.splitext(file_name)

    # Create backup filename
    backup_name = f"{name}_{timestamp}{extension}"

    # Create complete destination path
    destination_path = os.path.join(destination, backup_name)

    # Copy source file to destination
    shutil.copy(source, destination_path)

    # Write backup details into log file
    log_time = current_time.strftime("%d-%m-%Y %I:%M:%S %p")

    with open("backup_log.txt", "a") as fobj:
        fobj.write(f"Backup completed successfully at {log_time}\n")

    print(f"Backup completed: {destination_path}")

def main():

    # Accept source file path
    source = input("Enter source file path: ")

    # Accept destination directory path
    destination = input("Enter destination directory path: ")

    # Schedule backup every hour
    schedule.every(1).hour.do(backup_file, source, destination)

    # Perform backup immediately once
    backup_file(source, destination)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()