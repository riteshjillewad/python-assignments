#######################################################################################
# Name:         question_5.py
# Description:  Accept number and print odd numbers till that number
# Input:        Int
# Output:       List of odd numbers
# Date:         27-06-2026
# Author:       Ritesh Jillewad
#######################################################################################

def printOdd(no):

    for i in range(1, no):
        if i % 2 != 0:
            print(i)


def main():

    print("Enter number: ")
    num = int(input())

    printOdd(num)

if __name__ == "__main__":
    main()