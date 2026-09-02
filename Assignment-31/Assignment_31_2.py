##########################################################################################
# Name:        Assignment_31_2.py
# Description: Write a program that accepts:
#              1. Create a function named: displayMessage(message)
#              2. Schedule the function using scheduler
# Input:       Message
# Output:      Prints that message
# Date:        30-08-2026
# Author:      Ritesh Jillewad
##########################################################################################

import schedule
import time

def displayMessage(message):
    print(message)

def main():
    
    print("Enter message: ")
    message = input()
    
    print("Enter time interval in seconds: ")
    time_interval = int(input())
    
    if time_interval <= 0: 
        print("ERROR: Time interval must be greater than zero!") 
        return

    schedule.every(time_interval).seconds.do(displayMessage, message)  
    
    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()