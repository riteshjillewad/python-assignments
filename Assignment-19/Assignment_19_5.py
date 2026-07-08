##########################################################################################
# Name:        Assignment_19_5.py
# Description: Write an application that contains a list of numbers and performs operations:
#              1. Filter out prime numbers
#              2. Map will multiply each number by 2
#              3. Reduce will return max of all numbers
# Input:       int
# Output:      int 
# Date:        09-07-2026
# Author:      Ritesh Jillewad
##########################################################################################

from functools import reduce
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

map_nums = lambda x: x * 2
reduce_nums = lambda x, y: x if x > y else y

def main():
    input_list = list()
    print("Enter size of list: ")

    try:
        size = int(input())

        print(f"Enter {size} elements: ")
        for _ in range(size):
            val = int(input())
            input_list.append(val) 

        print(f"Input list: {input_list}") 

        fList = list(filter(isPrime, input_list))
        print(f"List after filter (Primes only): {fList}")

        mList = list(map(map_nums, fList))
        print(f"List after map (Multiplied by 2): {mList}")

        if mList:
            rList = reduce(reduce_nums, mList)
            print(f"Result after reduce (Maximum value): {rList}")
        else:
            print("No prime numbers were found. Cannot calculate a maximum.")

    except ValueError:
        print("Invalid input! Please enter only integers.")

if __name__ == "__main__":
    main()