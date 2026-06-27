#######################################################################################
# Name:         question_3.py
# Description:  Accept number and print sum of digits
# Input:        Int
# Output:       Sum of digits
# Date:         27-06-2026
# Author:       Ritesh Jillewad
#######################################################################################

def sumDigits(num):

    if num < 0:
        num = -num

    Sum = 0
    temp = 0

    temp = num
    while temp != 0:
        digit = temp % 10
        Sum = Sum + digit
        temp = temp // 10

    print(f"Sum of digits of {num}: {Sum}")

def main():

    print("Enter number: ")
    num = int(input())

    sumDigits(num)

if __name__ == "__main__":
    main()