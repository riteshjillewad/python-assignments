########################################################################################
# Name:        question_2.py
# Description: Program that display the following pattern
# Input:       Num
# Output:      Pattern
# Date:        04-07-2026
# Author:      Ritesh Jillewad
########################################################################################

def print_pattern(num):

    for i in range(num):
        for j in range(num):
            print("*", end=" ")
        print()

def main():

    print("Enter number: ")
    num = int(input())

    print_pattern(num)

if __name__ == "__main__":
    main()