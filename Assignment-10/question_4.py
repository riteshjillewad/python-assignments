#######################################################################################
# Name:         question_4.py
# Description:  Accept number and print even numbers till that number
# Input:        Int
# Output:       List of even numbers
# Date:         27-06-2026
# Author:       Ritesh Jillewad
#######################################################################################

def printEven(no):

    for i in range(1, no):
        if i % 2 == 0:
            print(i)


def main():

    print("Enter number: ")
    num = int(input())

    printEven(num)

if __name__ == "__main__":
    main()