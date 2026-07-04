########################################################################################
# Name:        question_4.py
# Description: Accept N numbers from user store it in list, and return frequency of target
#              element from list
# Input:       N numbers, target
# Output:      Frequency of target element
# Date:        04-07-2026
# Author:      Ritesh Jillewad
########################################################################################

def freq_element(nums: list[int], target: int) -> int:

    target_count = 0

    for num in nums:
        if num == target:
            target_count += 1
    
    return target_count

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

    print("Enter target element: ")
    target = int(input())

    ret = freq_element(nums_list, target)
    print(f"{target} occurs {ret} times in list")

if __name__ == "__main__":
    main()