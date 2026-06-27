######################################################################################
# Name:         problem.py
# Description:  Accept two numbers and return their multiplication
# Input:        Two numbers
# Output:       Multiplication
# Author:       Ritesh Jillewad
######################################################################################

def multiplication(no1, no2):
    return no1 * no2

def main():

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = multiplication(num1, num2)
    print("Multiplication =", result)

if __name__ == "__main__":
    main()