#######################################################################################
# Name:         question_9.py
# Description:  Write a lambda function using reduce which accepts a list of numbers 
#               and returns the product of all the numbers
# Input:        List of numbers
# Output:       Product of all the numbers
# Date:         03-07-2026
# Author:       Ritesh Jillewad
#######################################################################################

from functools import reduce

product_nums = lambda x, y: x * y

def main():
    nums = [1, 2, 3]
    print(f"Original list: {nums}")

    ret = reduce(product_nums, nums, 1)
    print(f"Reduced list: {ret}")

if __name__ == "__main__":
    main()