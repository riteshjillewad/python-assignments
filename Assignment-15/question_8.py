#######################################################################################
# Name:         question_8.py
# Description:  Write a lambda function using filter which accepts a list of numbers 
#               and returns a list of numbers divisible by both 3 and 5
# Input:        List of numbers
# Output:       List of numbers divisible by both 3 and 5
# Date:         03-07-2026
# Author:       Ritesh Jillewad
#######################################################################################

nums_divisible = lambda x: x % 3 == 0 and x % 5 == 0

def main():
    nums = [1, 2, 3, 4, 5, 15, 30]
    print(f"Original list: {nums}")

    ret = list(filter(nums_divisible, nums))
    print(f"Filtered list: {ret}")

if __name__ == "__main__":
    main()