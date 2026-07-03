#######################################################################################
# Name:         question_9.py
# Description:  Lambda function which accept three number and return max
# Input:        Three numbers
# Output:       Max number
# Date:         03-07-2026
# Author:       Ritesh Jillewad
#######################################################################################

max_number = lambda a, b, c: a if (a > b and a > c) else (b if b > c else c)

def main():

    print("Enter number1: ")
    num1 = int(input())

    print("Enter number2: ")
    num2 = int(input())

    print("Enter number3: ")
    num3 = int(input())

    ret = max_number(num1, num2, num3)
    print(f"Maximum among {num1}, {num2}, {num3}: {ret}")

if __name__ == "__main__":
    main()
