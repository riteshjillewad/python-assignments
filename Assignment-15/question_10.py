#######################################################################################
# Name:         question_9.py
# Description:  Write a lambda function using filter which accepts a list of numbers 
#               and returns the count of even numbers
# Input:        List of numbers
# Output:       Count of even numbers
# Date:         03-07-2026
# Author:       Ritesh Jillewad
#######################################################################################

even_number_check = lambda x: x % 2 == 0

def main():
    
    nums = [1, 2, 3, 4, 6, 8]
    print(f"Original list: {nums}")

    even_list = list(filter(even_number_check, nums))

    count_even_list = len(even_list)

    print(f"Filtered list (even numbers): {even_list}")
    print(f"Count of even numbers: {count_even_list}")

if __name__ == "__main__":
    main()