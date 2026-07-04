########################################################################################
# Name:        question_5.py
# Description: Accept N numbers from user and store it in list.
#              1. Return addition of all prime numbers from that list
#              2. ChkPrime() will check prime numbers from the list
#              3. Sum of those prime numbers
# Input:       N numbers
# Output:      Sum of prime numbers
# Date:        04-07-2026
# Author:      Ritesh Jillewad
########################################################################################

from MarvellousNum import ChkPrime

def list_prime_sum(nums: list[int]) -> int:

    sum_primes = 0

    for num in nums:
        if ChkPrime(num):
            sum_primes += num

    return sum_primes

def main():

    print("Enter size: ")
    n = int(input())

    if n <= 0:
        print("Please enter correct size!")

    nums_list = list()

    print(f"Enter {n} elements: ")
    for i in range(n):
        val = int(input())
        nums_list.append(val)

    ret = list_prime_sum(nums_list)
    print(f"Sum of prime numbers from list: {ret}")

if __name__ == "__main__":
    main()
