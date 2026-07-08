##########################################################################################
# Name:        Assignment_19_3.py
# Description: Write an application that contains a list of numbers and performs operations:
#              1. Filter numbers >= 70 and <= 90
#              2. Map will increase each number by 10
#              3. Reduce will return product of all those numbers
# Input:       int
# Output:      int 
# Date:        09-07-2026
# Author:      Ritesh Jillewad
##########################################################################################

from functools import reduce

filter_num = lambda x: 70 <= x <= 90
map_num = lambda x: x + 10
reduce_num = lambda x, y: x * y 

def main():

    input_list = list()
    print("Enter list size: ")

    try:
        size = int(input())

        print(f"Enter {size} elements: ")
        for i in range(size):
            val = int(input())
            input_list.append(val)

        print(f"Input list: {input_list}")

        fList = list(filter(filter_num, input_list))
        print(f"List after filtering: {fList}")

        mList = list(map(map_num, fList))
        print(f"List after mapping: {mList}")

        
        if mList:
            rList = reduce(reduce_num, mList)
            print(f"List after reducing: {rList}")
        else:
            print("No elements passed the filter. Cannot calculate a product.")
        
    except ValueError:
        print("Invalid input! Please enter valid integers.")

if __name__ == "__main__":
    main()