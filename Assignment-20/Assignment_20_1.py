##########################################################################################
# Name:        Assignment_20_1.py
# Description: Write an application that creates two separate threads: Even and Odd
#              1. The even thread should display first 10 even numbers
#              2. The odd thread should display first 10 odd numbers
#              3. Both threads should execute independently using threading module
#              4. Ensure proper thread creation and execution
# Input:       None
# Output:      int 
# Date:        09-07-2026
# Author:      Ritesh Jillewad
##########################################################################################

import threading
import time

# The even thread will use this function to display the first 10 even numbers
def even_nums():
    for i in range(2, 21, 2):
        print(f"Even Thread: {i}")
        time.sleep(0.1)  

# The odd thread will use this function to display the first 10 odd numbers
def odd_nums():
    for i in range(1, 20, 2):
        print(f"Odd Thread: {i}")
        time.sleep(0.1) 

def main():
    
    eventhread = threading.Thread(target=even_nums)
    oddthread = threading.Thread(target=odd_nums)

    eventhread.start()
    oddthread.start()

    eventhread.join()
    oddthread.join()
    
    print("Main thread finished execution.")

if __name__ == "__main__":
    main()