#######################################################################################
# Name:         question_1.py
# Description:  Write a lambda function using map which accept list of numbers and 
#               returns list of squares of each number
# Input:        List of numbers
# Output:       List of squares of numbers
# Date:         03-07-2026
# Author:       Ritesh Jillewad
#######################################################################################

square_num = lambda x: x **2

def main():

    nums = [1, 2, 3, 4, 5, 6, 7]

    map_nums = list(map(square_num, nums))
    print(f"Mapped list: {map_nums}")

if __name__ == "__main__":
    main()
