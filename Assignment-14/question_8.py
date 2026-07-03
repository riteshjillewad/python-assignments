#######################################################################################
# Name:         question_8.py
# Description:  Lambda function which accept two number and return addition
# Input:        Two numbers
# Output:       Addition
# Date:         03-07-2026
# Author:       Ritesh Jillewad
#######################################################################################

addition = lambda x, y: x + y

def main():

    print("Enter number1: ")
    num1 = int(input())

    print("Enter number2: ")
    num2 = int(input())

    ret = addition(num1, num2)
    print(f"Addition of {num1} and {num2}: {ret}")

if __name__ == "__main__":
    main()
