##########################################################################################
# Name:        Assignment_32_5.py
# Description: Write a program that deletes all empty files from a specified directory every hour
#              1. Scan the directory continuously
#              2. Detect files whose size is 0 bytes
#              3. Detect empty files
#              4. Store deleted file paths in a log file
#              5. Handle permission errors
# Input:       Directory name
# Output:      Log of empty files and deleted files
# Date:        04-09-2026
# Author:      Ritesh Jillewad
##########################################################################################

import schedule
import os
import time

LOG_FILE = "EmptyFilesLog.txt"

def log_message(message):
    """
    Write a message into the log file.
    """
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")


def delete_empty_files(dirname):
    """
    Scan the specified directory and delete all empty files.
    """

    print("Scanning directory:", dirname)

    try:
        for filename in os.listdir(dirname):
            filepath = os.path.join(dirname, filename)

            # Check whether it is a file
            if os.path.isfile(filepath):
                try:
                    # Check file size
                    if os.path.getsize(filepath) == 0:
                        try:
                            os.remove(filepath)

                            message = "Deleted empty file: " + filepath
                            print(message)
                            log_message(message)

                        except PermissionError:
                            message = "Permission denied while deleting: " + filepath
                            print(message)
                            log_message(message)

                except PermissionError:
                    message = "Permission denied while accessing: " + filepath
                    print(message)
                    log_message(message)

    except PermissionError:
        message = "Permission denied for directory: " + dirname
        print(message)
        log_message(message)

    except FileNotFoundError:
        message = "Directory not found: " + dirname
        print(message)
        log_message(message)

    except Exception as e:
        message = "Error: " + str(e)
        print(message)
        log_message(message)


def main():
    print("Enter directory name: ")
    dirname = input()

    if not os.path.exists(dirname):
        print("Directory does not exist.")
        return

    if not os.path.isdir(dirname):
        print("Specified path is not a directory.")
        return

    # Run immediately once
    delete_empty_files(dirname)

    # Schedule the task every hour
    schedule.every(1).hour.do(delete_empty_files, dirname)

    print("\nProgram is running continuously...")
    print("Empty files will be checked every hour.")
    print("Press Ctrl+C to stop the program.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()