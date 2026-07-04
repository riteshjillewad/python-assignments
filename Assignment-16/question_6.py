########################################################################################
# Name:        question_6.py
# Description: Write a program to accept number from user and check if it is positive or 
#              negative or zero
# Input:       Number
# Output:      Positive or negative or zero
# Date:        04-07-2026
# Author:      Ritesh Jillewad
########################################################################################

def ChKNumber(number):

    if number > 0:
        print(f"{number}: Positive")
    elif number == 0:
        print("Zero")
    else:
        print(f"{number}: Negative")

def main():

    print("Enter number: ")
    num = int(input())

    ChKNumber(num)

if __name__ == "__main__":
    main()

