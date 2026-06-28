#######################################################################################
# Name:         question_4.py
# Description:  Accept a number and print that many numbers starting from 1
# Input:        Number
# Output:       Range of numbers
# Date:         28-06-2026
# Author:       Ritesh Jillewad
#######################################################################################

def printRange(num):

    for i in range(1, num + 1):
        print(i)

def main():

    print("Enter number: ")
    num = int(input())

    printRange(num)

if __name__ == "__main__":
    main()
