########################################################################################
# Name:        question_7.py
# Description: Write a program to accept number from user and return True if number is
#              divisible by 5, otherwise return False
# Input:       Number
# Output:      True or False
# Date:        04-07-2026
# Author:      Ritesh Jillewad
########################################################################################

def ChKNumber(number):

    return number % 5 == 0

def main():

    print("Enter number: ")
    num = int(input())

    ret = ChKNumber(num)
    if(ret == True):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()

