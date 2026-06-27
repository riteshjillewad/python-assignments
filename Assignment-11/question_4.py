#######################################################################################
# Name:         question_4.py
# Description:  Accept number and print its reverse form
# Input:        Number
# Output:       Reversed number
# Date:         27-06-2026
# Author:       Ritesh Jillewad
#######################################################################################

def reverseNum(num):

    original = num

    if num < 0:
        num = -num

    rev = 0
    temp = num

    while temp != 0:
        rev = rev * 10 + (temp % 10)
        temp = temp // 10

    if original < 0:
        rev = -rev

    print(f"Original number: {original}, Reversed number: {rev}")


def main():

    print("Enter number: ")
    num = int(input())

    reverseNum(num)


if __name__ == "__main__":
    main()