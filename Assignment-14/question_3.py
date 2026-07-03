#######################################################################################
# Name:         question_3.py
# Description:  Lambda function which accepts two number and return the maximum
# Input:        Two numbers
# Output:       Maximum number
# Date:         03-07-2026
# Author:       Ritesh Jillewad
#######################################################################################

# approach 1: using ternary operators
max_number = lambda x, y: x if x > y else y

# approach 2: max_number = lambda x, y: max(x, y)
def main():

    print("Enter number1: ")
    num1 = int(input())

    print("Enter number2: ")
    num2 = int(input())

    ret = max_number(num1, num2)
    print(f"Maximum among {num1} and {num2} is: {ret}")

if __name__ == "__main__":
    main()
