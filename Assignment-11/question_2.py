#######################################################################################
# Name:         question_2.py
# Description:  Accept number and count the digits
# Input:        Int
# Output:       Prime or non-prime
# Date:         27-06-2026
# Author:       Ritesh Jillewad
#######################################################################################

def countDigits(num):

    count = 0
    temp = 0

    if num == 0:
        print("Number of digits in 0 is: 1")
        return
    
    if num < 0:
        num = -num

    temp = num
    while temp != 0:
        digit = temp % 10
        count = count + 1
        temp = temp // 10

    print(f"Number of digits in {num}: {count}")

def main():

    print("Enter number: ")
    num = int(input())

    countDigits(num)

if __name__ == "__main__":
    main()