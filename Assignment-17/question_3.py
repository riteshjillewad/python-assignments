########################################################################################
# Name:        question_3.py
# Description: Program that calculates and returns the factorial
# Input:       Num
# Output:      Factorial
# Date:        04-07-2026
# Author:      Ritesh Jillewad
########################################################################################

def find_factorial(num):

    if num == 0:
        return 1

    fact = 1
    for i in range(num, 0, -1):
        fact = fact * i

    return fact

def main():

    print("Enter number: ")
    num = int(input())

    if num < 0:
        print("Factorial of negative number cannot be find!")
    else:
        ret = find_factorial(num)
        print(f"Factorial of {num} is: {ret}")

if __name__ == "__main__":
    main()