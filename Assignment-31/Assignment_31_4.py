##########################################################################################
# Name:        Assignment_31_4.py
# Description: Write a program that creates a new log file after every 10 minutes
#              1. The filename should contain current date and time
# Input:       Void
# Output:      Log file
# Date:        02-09-2026
# Author:      Ritesh Jillewad
##########################################################################################

import schedule
import time
from datetime import datetime

def work():
    current_time = datetime.now()
    fileName = "MarvellousLog_" + current_time.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    with open(fileName, "w") as file:
        file.write("This is a Marvellous log file.\n")
        file.write("Log file created at: " + str(current_time) + "\n")

    print("Log file created:", fileName)

def main():

    work()
    schedule.every(10).minutes.do(work)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
