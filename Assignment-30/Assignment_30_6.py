##########################################################################################
# Name:        Assignment_30_6.py
# Description: Write a script that schedules the following tasks:
#              1. Print LUNCH TIME! every day at 1.00 PM
#              2. Print WRAP UP WORK every day at 6.00 PM
#              Both tasks should be handled by seperate functions
# Input:       None
# Output:      Schedule the tasks every day at mentioned time
# Date:        30-08-2026
# Author:      Ritesh Jillewad
##########################################################################################

import schedule
import time

def lunch_time():
    print("LUNCH TIME!")

def wrap_up_work():
    print("WRAP UP WORK")

def main():
    schedule.every().day.at("13:00").do(lunch_time)
    schedule.every().day.at("18:00").do(wrap_up_work)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()