#######################################################################################
# Name:         question_2.py
# Description:  Write a lambda function using filter which accept list of numbers and 
#               returns list of even numbers
# Input:        List of numbers
# Output:       List of even numbers
# Date:         03-07-2026
# Author:       Ritesh Jillewad
#######################################################################################

even_nums = lambda x: x % 2 == 0

def main():

    nums = [1, 2, 3, 4, 5, 6, 7]
    print(f"Original list: {nums}")

    ret = list(filter(even_nums, nums))
    print(f"Filtered list: {ret}")

if __name__ == "__main__":
    main()
