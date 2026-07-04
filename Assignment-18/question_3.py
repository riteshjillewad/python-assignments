########################################################################################
# Name:        question_3.py
# Description: Accept N numbers from user store it in list, and return min element
# Input:       N numbers
# Output:      Min element
# Date:        04-07-2026
# Author:      Ritesh Jillewad
########################################################################################

def min_element(nums: list[int]) -> int:

    min_number = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < min_number:
            min_number = nums[i]

    return min_number


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

    ret = min_element(nums_list)
    print(f"Minimum of list is: {ret}")

if __name__ == "__main__":
    main()