########################################################################################
# Name:        question_1.py
# Description: Program that will use functions from our module
# Input:       void
# Output:      Arithmetic functions
# Date:        04-07-2026
# Author:      Ritesh Jillewad
########################################################################################

from Arithmetic import *

def main():

    print("Enter first number: ")
    num1 = int(input())

    print("Enter second number: ")
    num2 = int(input())

    ret = Add(num1, num2)
    print(f"Addition of {num1} and {num2}: {ret}")

    ret = Sub(num1, num2)
    print(f"Substraction of {num1} and {num2}: {ret}")

    ret = Mult(num1, num2)
    print(f"Multiplication of {num1} and {num2}: {ret}")

    if num2 == 0:
        print("Division by 0 not allowed!")
    else:
        ret = Div(num1, num2)
        print(f"Division of {num1} and {num2}: {ret}")

if __name__ == "__main__":
    main()