##########################################################################################
# Name:        Assignment_21_1.py
# Description: Write an application that creates two threads: Prime and NonPrime
#              1. Both threads should accept list of integers
#              2. The Prime thread should display all prime numbers from list
#              3. The NonPrime thread should display all non-prime numbers from list
# Input:       None
# Output:      int 
# Date:        09-07-2026
# Author:      Ritesh Jillewad
##########################################################################################

import threading
import math

def isPrime(num: int) -> bool:
    if num <= 1:
        return False
    
    if num == 2:
        return True
    
    if num % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
        
    return True

def prime(nums: list[int]) -> None:
    primes_list = list()

    for no in nums:
        if isPrime(no):
            primes_list.append(no)

    print(f"Prime thread found: {primes_list}")

def non_prime(nums: list[int]) -> None:
    non_primes_list = list()

    for no in nums:
        if not isPrime(no):
            non_primes_list.append(no)

    print(f"Non-prime thread found: {non_primes_list}")

def main():

    input_list = list()
    print("Enter size of list: ")
    try:
        size = int(input())

        print(f"Enter {size} elements: ")
        for _ in range(size):
            val = int(input())
            input_list.append(val)

        prime_thread = threading.Thread(target=prime, args=(input_list, ))
        non_prime_thread = threading.Thread(target=non_prime, args=(input_list, ))

        prime_thread.start()
        non_prime_thread.start()

        prime_thread.join()
        non_prime_thread.join()

    except ValueError:
        print("Invalid input!")

if __name__ == "__main__":
    main()
