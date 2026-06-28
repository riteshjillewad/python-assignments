#######################################################################################
# Name:         question_4.py
# Description:  Accept a number and print that many numbers in reverse order
# Input:        Number
# Output:       Range of numbers in reverse order
# Date:         28-06-2026
# Author:       Ritesh Jillewad
#######################################################################################

def printRangeReverse(num):

    for i in range(num, 0, -1):
        print(i)

def main():

    print("Enter number: ")
    num = int(input())

    printRangeReverse(num)

if __name__ == "__main__":
    main()
