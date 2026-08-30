##########################################################################################
# Name:        Assignment_31_1.py
# Description: Write a program that accepts:
#              1. A message from the user
#              2. A time interval in seconds
#              Schedule the program to display the message repeatedly after the specific interval
# Input:       Message, Time interval(seconds)
# Output:      Prints that message
# Date:        30-08-2026
# Author:      Ritesh Jillewad
##########################################################################################

import schedule
import time

def work(message):
    print(message)

def main():
    
    print("Enter message: ")
    message = input()
    
    print("Enter time interval in seconds: ")
    time_interval = int(input())
    
    if time_interval <= 0: 
        print("ERROR: Time interval must be greater than zero!") 
        return

    schedule.every(time_interval).seconds.do(work, message)  
    
    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()