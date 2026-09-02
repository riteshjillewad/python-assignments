##########################################################################################
# Name:        Assignment_31_5.py
# Description: Write a program that schedules the following messages:
#              1. Monday at 9.00 AM: Start your weekly goals
#              2. Wednesday at 5:00 PM: Review your weekly progress
#              3. Friday at 6:00 PM: Weekly work completed
# Input:       Void
# Output:      Display scheduled messages
# Date:        02-09-2026
# Author:      Ritesh Jillewad
##########################################################################################

import schedule
import time

def monday_task():
    print("Start your weekly goals")

def wednesday_task():
    print("Review your weekly progress")

def friday_task():
    print("Weekly work completed")

def main():
    schedule.every().monday.at("09:00").do(monday_task)
    schedule.every().wednesday.at("17:00").do(wednesday_task)
    schedule.every().friday.at("18:00").do(friday_task)
    
    print("Weekly tasks scheduled successfully...")
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()