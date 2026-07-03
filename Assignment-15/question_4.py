#######################################################################################
# Name:         question_4.py
# Description:  Write a lambda function using reduce which accept list of numbers and 
#               returns addition of all elements
# Input:        List of numbers
# Output:       Addition of all list numbers
# Date:         03-07-2026
# Author:       Ritesh Jillewad
#######################################################################################

from functools import reduce

add_nums = lambda x, y: x + y

def main():

    nums = [1, 2, 3, 4, 5]
    print(f"Original list: {nums}")

    ret = reduce(add_nums, nums, 0)
    print(f"Addition of list: {ret}")

if __name__ == "__main__":
    main()
