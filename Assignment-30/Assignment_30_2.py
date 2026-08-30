##########################################################################################
# Name:        Assignment_30_1.py
# Description: Write a program that displays current date and time after every 1 minute
# Input:       None
# Output:      Prints current date and time after every 1 minute
# Date:        30-08-2026
# Author:      Ritesh Jillewad
##########################################################################################

import schedule
import time

def work():
    
    # current_time = datetime.now()
    current_time = time.ctime()
    print(f"Current time: {current_time}")

def main():
    schedule.every(1).minute.do(work)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()