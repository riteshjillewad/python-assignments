##########################################################################################
# Name:        Assignment_21_4.py
# Description: Design a Python application that creates two threads
#              1. Thread1 should compute sum of elements from list
#              2. Thread2 should computer product of elements from same list
#              3. Return the result to main thread, and display it
# Input:       None
# Output:      int 
# Date:        09-07-2026
# Author:      Ritesh Jillewad
##########################################################################################

import threading

def compute_sum(nums: list, results: dict) -> None:
    total_sum = 0
    for num in nums:
        total_sum += num
        
    results['sum_result'] = total_sum

def compute_product(nums: list, results: dict) -> None:
    total_product = 1
    if not nums:
        total_product = 0
    else:
        for num in nums:
            total_product *= num
            
    results['prod_result'] = total_product

def main():
    input_list = list()
    thread_results = {}

    try:
        size = int(input("Enter list size: "))

        print(f"Enter {size} elements: ")
        for _ in range(size):
            val = int(input())
            input_list.append(val)
            
        print(f"\nInput list: {input_list}\n")

        sum_thread = threading.Thread(target=compute_sum, args=(input_list, thread_results))
        prod_thread = threading.Thread(target=compute_product, args=(input_list, thread_results))

        sum_thread.start()
        prod_thread.start()

        sum_thread.join()
        prod_thread.join()

        print("--- Results Displayed by MAIN Thread ---")
        print(f"Sum of elements:     {thread_results.get('sum_result')}")
        print(f"Product of elements: {thread_results.get('prod_result')}")

    except ValueError:
        print("Invalid input! Please enter only integers.")

if __name__ == "__main__":
    main()