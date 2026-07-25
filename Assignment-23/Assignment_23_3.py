##########################################################################################
# Name:        Assignment_23_1.py
# Description: Count even numbers between 1 and N
# Input:       list
# Output:      Count of even numbers
# Date:        25-07-2026
# Author:      Ritesh Jillewad
##########################################################################################

import multiprocessing
import time
import os

def work(N):
    
    evenCount = 0
    
    for i in range(1, N + 1):
        if i % 2 == 0:
            evenCount += 1
            
    pid = os.getpid()
    
    print(f"Process ID: {pid}")
    print(f"Input Number: {N}")
    print(f"Even numbers count: {evenCount}")
            
    return evenCount
          
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
    
    start_time = time.perf_counter()
    
    with multiprocessing.Pool() as pool:
        result = pool.map(work, input_list)
        
    end_time = time.perf_counter()
        
    print(f"Result: {result}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")
        
if __name__ == "__main__":
    main()