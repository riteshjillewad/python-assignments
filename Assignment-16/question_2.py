########################################################################################
# Name:        question_2.py
# Description: Write a function ChkNum(). If number is even, it should display "even number"
#              otherwise display "odd number" on console
# Input:       Number
# Output:      Even or odd number
# Date:        04-07-2026
# Author:      Ritesh Jillewad
########################################################################################

def ChkNum(number):

    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

def main():

    print("Enter number: ")
    num = int(input())

    ChkNum(num)

if __name__ == "__main__":
    main()
