#######################################################################################
# Name:         question_4.py
# Description:  Print the binary equivalent of a number
# Input:        Int
# Output:       Binary equivalent
# Date:         28-06-2026
# Author:       Ritesh Jillewad
#######################################################################################

def printBinary(num):

    return bin(num)


def main():

    print("Enter a number: ")
    num = int(input())

    ret = printBinary(num)
    print(f"Binary equivalent of {num} is: {ret}")


if __name__ == "__main__":
    main()
