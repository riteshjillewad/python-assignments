##########################################################################################
# Name:        Assignment_30_1.py
# Description: Write a program that prints "jay ganesh" every 2 seconds
# Input:       None
# Output:      Prints jay ganesh every 2 seconds
# Date:        30-08-2026
# Author:      Ritesh Jillewad
##########################################################################################

import schedule
import time

def work():
    print("Jay ganesh...")

def main():
    schedule.every(2).seconds.do(work)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()