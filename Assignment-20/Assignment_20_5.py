##########################################################################################
# Name:        Assignment_20_5.py
# Description: Write an application that creates two threads: Thread1 and Thread2
#              1. Thread1 should display numbers from 1 to 50
#              2. Thread2 should display numbers from 50 to 1 in reverse order
#              3. Ensure that Thread2 starts only after Thread1 has completed
# Input:       None
# Output:      int 
# Date:        09-07-2026
# Author:      Ritesh Jillewad
##########################################################################################

import threading

def print_nums():

    for i in range(1, 51):
        print(f"Thread 1: {i}")
    print("------------------------------------------")

def print_nums_reverse():
    
    for i in range(50, 0, -1):
        print(f"Thread 2: {i}")
    print("------------------------------------------")

def main():

    thread1 = threading.Thread(target=print_nums)
    thread2 = threading.Thread(target=print_nums_reverse)

    thread1.start()
    thread1.join()                          # We wait until first thread completes

    thread2.start()
    thread2.join()                          # We wait until second thread completes

if __name__ == "__main__":
    main()