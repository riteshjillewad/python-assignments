##########################################################################################
# Name:        Assignment_30_5.py
# Description: Schedule a task that executes every five minutes:
#              1. The task should write the current date and time into a file: Marvellous.txt
#              2. New entries should be appended without removing previous entries
# Input:       None
# Output:      Task that executes every 5 minutes
# Date:        30-08-2026
# Author:      Ritesh Jillewad
##########################################################################################

import schedule
import time
from datetime import datetime

def work(fobj):

    current_time = datetime.now()
    fobj.write(f"Task executed at: {current_time}\n")
    fobj.flush()

def main():
    fileName = "Marvellous.txt"

    with open(fileName, "a") as fobj:
        fobj.write("=" * 45 + "\n")
        fobj.write("TASK EXECUTION DETAILS".center(45) + "\n")
        fobj.write("=" * 45 + "\n")

        schedule.every(5).minutes.do(work, fobj)

        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    main()
