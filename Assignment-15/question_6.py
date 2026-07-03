#######################################################################################
# Name:         question_6.py
# Description:  Write a lambda function using reduce which accept list of numbers and 
#               returns minimum element
# Input:        List of numbers
# Output:       Minimum element
# Date:         03-07-2026
# Author:       Ritesh Jillewad
#######################################################################################

from functools import reduce

min_nums = lambda x, y: x if x < y else y

def main():

    nums = [1, 2, 3, 4, 5]
    print(f"Original list: {nums}")

    ret = reduce(min_nums, nums)
    print(f"Minimum of list: {ret}")

if __name__ == "__main__":
    main()
