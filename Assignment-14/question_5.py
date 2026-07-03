#######################################################################################
# Name:         question_5.py
# Description:  Lambda function which return true if number is even, else return false
# Input:        Two numbers
# Output:       Maximum number
# Date:         03-07-2026
# Author:       Ritesh Jillewad
#######################################################################################

is_even = lambda x: True if x % 2 == 0 else False

# is_even = lamdba x: x % 2 == 0

def main():

    print("Enter number1: ")
    num = int(input())

    ret = is_even(num)
    print(f"{num}: {ret}")

if __name__ == "__main__":
    main()
