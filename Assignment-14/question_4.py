#######################################################################################
# Name:         question_4.py
# Description:  Lambda function which accepts two number and return the minimum
# Input:        Two numbers
# Output:       Minimum number
# Date:         03-07-2026
# Author:       Ritesh Jillewad
#######################################################################################

# approach 1: using ternary operators
min_number = lambda x, y: x if x < y else y

# approach 2: min_number = lambda x, y: min(x, y)
def main():

    print("Enter number1: ")
    num1 = int(input())

    print("Enter number2: ")
    num2 = int(input())

    ret = min_number(num1, num2)
    print(f"Minimum among {num1} and {num2} is: {ret}")

if __name__ == "__main__":
    main()
