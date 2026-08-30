##########################################################################################
# Name:        Assignment_30_4.py
# Description: Create a task that runs every day at 9.00 AM and prints Namskar
# Input:       None
# Output:      Task that executes every day at 9.00 AM
# Date:        30-08-2026
# Author:      Ritesh Jillewad
##########################################################################################

import schedule
import time

def work():
    print("Namskar")

def main():
    job = schedule.every().day.at("09:00").do(work)
    # .run() is used so that we can force run it first time
    # job.run()
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()