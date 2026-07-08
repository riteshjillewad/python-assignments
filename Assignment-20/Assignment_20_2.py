##########################################################################################
# Name:        Assignment_20_2.py
# Description: Write an application that creates two separate threads: EvenFactor and OddFactor
#              1. Both threads should accept one integer number as parameter
#              2. The EvenFactor thread should:
#               - Identify all even factors of given number
#               - Calculate and display sum of even factors
#              3. The OddFactor thread should:
#               - Identify all odd factors of given number
#               - Calculate and display sum of odd factors
#              4. After both threads, the main thread should display: Exit from main 
# Input:       None
# Output:      int 
# Date:        09-07-2026
# Author:      Ritesh Jillewad
##########################################################################################

import threading
import time

def even_factor(num):

    even_sum = 0
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 == 0:
            print(f"Even Factor thread found: {i}")
            even_sum += i
            time.sleep(0.1)
    print(f"Sum of Even Factors: {even_sum}")

def odd_factor(num):

    odd_sum = 0
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 != 0:
            print(f"Odd Factor thread found: {i}")
            odd_sum += i
            time.sleep(0.1)
    print(f"Sum of Odd Factors: {odd_sum}")
            
def main():
    try:
        num = int(input("Enter number: "))

        evenfactorthread = threading.Thread(target=even_factor, args=(num, ))
        oddfactorthread = threading.Thread(target=odd_factor, args=(num, ))

        evenfactorthread.start()
        oddfactorthread.start()

        evenfactorthread.join()
        oddfactorthread.join()
        
        print("Exit from main")

    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    main()