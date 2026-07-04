########################################################################################
# Name:        question_2.py
# Description: Accept N numbers from user store it in list, and return max element
# Input:       N numbers
# Output:      Max element
# Date:        04-07-2026
# Author:      Ritesh Jillewad
########################################################################################

def max_element(nums: list[int]) -> int:

    max_number = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > max_number:
            max_number = nums[i]

    return max_number


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

    ret = max_element(nums_list)
    print(f"Maximum of list is: {ret}")

if __name__ == "__main__":
    main()