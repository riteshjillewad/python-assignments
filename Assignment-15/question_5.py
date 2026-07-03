#######################################################################################
# Name:         question_5.py
# Description:  Write a lambda function using reduce which accept list of numbers and 
#               returns maximum element
# Input:        List of numbers
# Output:       Maximum element
# Date:         03-07-2026
# Author:       Ritesh Jillewad
#######################################################################################

from functools import reduce

max_nums = lambda x, y: x if x > y else y

def main():

    nums = [1, 2, 3, 4, 5]
    print(f"Original list: {nums}")

    ret = reduce(max_nums, nums)
    print(f"Maximum of list: {ret}")

if __name__ == "__main__":
    main()
