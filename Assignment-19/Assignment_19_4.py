##########################################################################################
# Name:        Assignment_19_4.py
# Description: Write an application that contains a list of numbers and performs operations:
#              1. Filter out even numbers
#              2. Map calculate the square of each number
#              3. Reduce will return addition of all the numbers
# Input:       int
# Output:      int 
# Date:        09-07-2026
# Author:      Ritesh Jillewad
##########################################################################################

# _(single underscore): Indicates temporary or unused variable. Use it when syntax requires a variable, but you don't plan to use its value.

from functools import reduce

filter_even = lambda x: x % 2 == 0
square_nums = lambda x: x ** 2
add_nums = lambda x, y: x + y

def main():

    input_list = list()
    print("Enter size of list: ")

    try:
        size = int(input())

        print(f"Enter {size} elements: ")
        for _ in range(size):
            val = int(input())
            input_list.append(val) 

        print(f"Input list: {input_list}") 

        fList = list(filter(filter_even, input_list))
        print(f"List after filter: {fList}")

        mList = list(map(square_nums, fList))
        print(f"List after map: {mList}")

        rList = reduce(add_nums, mList, 0)
        print(f"List after reduce: {rList}")

    except ValueError:
        print("invalid input! enter only integers")

if __name__ == "__main__":
    main()