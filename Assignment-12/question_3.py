#######################################################################################
# Name:         question_3.py
# Description:  Write a program to print addition, multiplication, division, subtraction
# Input:        Int
# Output:       Arithmetic operations
# Date:         28-06-2026
# Author:       Ritesh Jillewad
#######################################################################################

def calculator(num1, num2):

    print("-" * 40)
    addition = num1 + num2
    print(f"Addition of {num1} and {num2} is: {addition}")

    print("-" * 40)
    subtraction = num1 - num2
    print(f"Subtraction of {num1} and {num2} is: {subtraction}")

    print("-" * 40)
    multiplication = num1 * num2
    print(f"Multiplication of {num1} and {num2} is: {multiplication}")

    print("-" * 40)
    if num2 != 0:
        division = num1 / num2
        print(f"Division of {num1} and {num2} are: {division}")
    else:
        print("Division by 0 not allowed!")
    print("-" * 40)


def main():

    print("Enter first number: ")
    num1 = int(input())

    print("Enter second number: ")
    num2 = int(input())

    calculator(num1, num2)

if __name__ == "__main__":
    main()
