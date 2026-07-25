##########################################################################################
# Name:        Assignment_22_2.py
# Description: For every number in list, count how many prime numbers exist between 1 and
#              N using multiprocessing pool
# Input:       list
# Output:      Count of prime numbers from 1 to N for each element
# Date:        25-07-2026
# Author:      Ritesh Jillewad
##########################################################################################

import multiprocessing
import time
import math

def is_prime(N):
    # Primes are integers strictly greater than 1
    if N <= 1:
        return False
    
    if N == 2:
        return True
    
    # Even numbers greater than 2 are not prime
    if N % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(N)
    for i in range(3, int(math.sqrt(N)) + 1, 2):
        if N % i == 0:
            return False
        
    return True

def count_primes(N):
    
    cnt = 0
    for i in range(1, N + 1):
        if is_prime(i):
            cnt += 1
    
    return cnt
          
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
        result = pool.map(count_primes, input_list)
        
    end_time = time.perf_counter()
        
    print(f"Result: {result}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")
        
if __name__ == "__main__":
    main()