#######################################################################################
# Name:         question_5.py
# Description:  Accept number and check if it is palindrome
# Input:        Number
# Output:       Palindrome or not
# Date:         27-06-2026
# Author:       Ritesh Jillewad
#######################################################################################

def chkPalindrome(num):

    if num < 0:
        return False

    original = num
    rev = 0
    temp = num

    while temp != 0:
        rev = rev * 10 + (temp % 10)
        temp //= 10

    return original == rev


def main():

    print("Enter number: ")
    num = int(input())

    ret = chkPalindrome(num)
    if ret == True:
        print(f"{num} is palindrome")
    else:
        print(f"{num} is not palindrome")

if __name__ == "__main__":
    main()