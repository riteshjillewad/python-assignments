##########################################################################################
# Name:        Assignment_20_3.py
# Description: Write an application that creates two separate threads: EvenList and OddList
#              1. Both threads should accept list of integers as input
#              2. The EvenList thread should:
#               - Extract all even elements from list
#               - Calculate and display their sum
#              3. The OddList thread should:
#               - Extract all odd elements from list
#               - Calculate and display their sum
#              4. Threads should run concurrently
# Input:       None
# Output:      int 
# Date:        09-07-2026
# Author:      Ritesh Jillewad
##########################################################################################

import threading

def even_list(nums):
    even_sum = 0
    
    for num in nums:
        if num % 2 == 0:
            even_sum += num
            
    print(f"Even thread calculation (Sum of evens): {even_sum}")

def odd_list(nums):
    odd_sum = 0
    
    for num in nums:
        if num % 2 != 0:
            odd_sum += num

    print(f"Odd thread calculation (Sum of odds): {odd_sum}")

def main():
    input_list = list()
    print("Enter list size: ")
    
    try:
        size = int(input())

        print(f"Enter {size} elements: ")
        for _ in range(size):
            var = int(input())
            input_list.append(var)
            
        print(f"Input list: {input_list}\n")

        even_list_thread = threading.Thread(target=even_list, args=(input_list, ))
        odd_list_thread = threading.Thread(target=odd_list, args=(input_list, )) 

        even_list_thread.start()
        odd_list_thread.start()

        even_list_thread.join()
        odd_list_thread.join()

    except ValueError:
        print("Invalid input! Please enter only integers.")

if __name__ == "__main__":
    main()