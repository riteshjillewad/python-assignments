########################################################################################
# Name:        question_8.py
# Description: Write a program to accept number from user and print that many * on screen
# Input:       Number
# Output:      Number of starts
# Date:        04-07-2026
# Author:      Ritesh Jillewad
########################################################################################

def print_pattern(number):

    print("*" * number, end=" ")

def main():

    print("Enter number: ")
    num = int(input())

    print_pattern(num)

if __name__ == "__main__":
    main()

