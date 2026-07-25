##########################################################################################
# Name:        Assignment_22_2.py
# Description: Write a program that accepts list of integers
#              1. Uses pool.map() to calculate factorial of multiple numbers simultaneously
# Input:       list
# Output:      Factorial of numbers
# Date:        25-07-2026
# Author:      Ritesh Jillewad
##########################################################################################

import multiprocessing
import time

def find_factorial(num):
    
    num = abs(num)
    
    if num == 0:
        return 1
    
    fact = 1
    for i in range(num, 0, -1):
        fact = fact * i
        
    return fact
        
def main():
    
    ##########################################################################
    # INPUT LIST PART
    ##########################################################################
    
    input_list = list()
    
    print("Enter size of list: ")
    size = int(input())
    
    print(f"Enter {size} elements: ")
    for _ in range(size):
        value = int(input())
        input_list.append(value)
        
    ##########################################################################
    # INPUT LIST VALIDATION PART
    ##########################################################################
        
    if len(input_list) == 0:
        print("Input list empty!")
        return
    else:
        print(f"Input list: {input_list}")
        
    ##########################################################################
    # MULTIPROCESSING PART
    ##########################################################################
    
    # Measuring execution time across pool worker processes
    start_time = time.perf_counter()
    
    with multiprocessing.Pool() as pool:
        result = pool.map(find_factorial, input_list)
        
    end_time = time.perf_counter()
        
    print(f"Result: {result}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")
        
if __name__ == "__main__":
    main()