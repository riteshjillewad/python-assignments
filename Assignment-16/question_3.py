########################################################################################
# Name:        question_3.py
# Description: Write a function named Add(), which accept two numbers from user and return
#              addition of two numbers
# Input:       Two numbers
# Output:      Addition
# Date:        04-07-2026
# Author:      Ritesh Jillewad
########################################################################################

def Add(number1, number2):
    
    return number1 + number2

def main():

    print("Enter number1: ")
    num1 = int(input())

    print("Enter number2: ")
    num2 = int(input())

    ret = Add(num1, num2)
    print(f"Addition of {num1} and {num2} is: {ret}")

if __name__ == "__main__":
    main()
