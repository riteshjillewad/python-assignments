##########################################################################################
# Name:        Assignment_21_2.py
# Description: Write an application that creates two threads:
#              1. Thread1 should calculate and find maximum number
#              2. Thread2 should calculate and find minimum number
#              3. List should be taken as input
# Input:       None
# Output:      int 
# Date:        09-07-2026
# Author:      Ritesh Jillewad
##########################################################################################

import threading

def find_max(nums: list[int]) -> int:
    maxnum = 0

    for i in range(len(nums)):
        if nums[i] > maxnum:
            maxnum = nums[i]

    print(f"Max thread: {maxnum}")

def find_min(nums: list[int]) -> int:
    minnum = 0

    for i in range(len(nums)):
        if nums[i] < minnum:
            minnum = nums[i]

    print(f"Min thread: {minnum}")

def main():

    input_list = list()
    print("Enter size of list: ")
    try:
        size = int(input())

        print(f"Enter {size} elements: ")
        for _ in range(size):
            val = int(input())
            input_list.append(val)

        max_thread = threading.Thread(target=find_max, args=(input_list, ))
        min_thread = threading.Thread(target=find_min, args=(input_list, ))

        max_thread.start()
        min_thread.start()

        max_thread.join()
        min_thread.join()

    except ValueError:
        print("Invalid input!")

if __name__ == "__main__":
    main()
