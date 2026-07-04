########################################################################################
# Name:        question_1.py
# Description: Accept N numbers from user store it in list, and return it's addition
# Input:       N numbers
# Output:      Addition
# Date:        04-07-2026
# Author:      Ritesh Jillewad
########################################################################################

def add_list(nums: list[int]) -> int:

    return sum(nums)

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

    ret = add_list(nums_list)
    print(f"Addition of list is: {ret}")

if __name__ == "__main__":
    main()