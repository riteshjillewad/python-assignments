##########################################################################################
# Name:        Assignment_30_3.py
# Description: Write a program that schedules a function to print: coding kar every 30 minutes
# Input:       None
# Output:      Schedules a function and prints every 30 minute
# Date:        30-08-2026
# Author:      Ritesh Jillewad
##########################################################################################

import schedule
import time

def work():
    print("CODING KAR!")

def main():
    job = schedule.every(30).minutes.do(work)
    
    # .run() is used so that we can force run it first time
    job.run()
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()