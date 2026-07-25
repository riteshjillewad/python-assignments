##########################################################################################
# Name:        Assignment_22_1.py
# Description: Write a program that accepts list of integers
#              1. Uses pool.map() to perform sum of squares from 1 to N for every element
# Input:       list
# Output:      Sum of square of numbers of from list
# Date:        25-07-2026
# Author:      Ritesh Jillewad
##########################################################################################

import multiprocessing
import time

def sum_of_squares(n):
    result = n * (n + 1) * (2 * n + 1) // 6
    return result
    
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
        result = pool.map(sum_of_squares, input_list)
        
    end_time = time.perf_counter()
        
    print(f"Result: {result}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")
        
if __name__ == "__main__":
    main()