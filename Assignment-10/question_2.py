#######################################################################################
# Name:         question_2.py
# Description:  Function to find sum of first N natural number
# Input:        Int
# Output:       Sum
# Date:         27-06-2026
# Author:       Ritesh Jillewad
#######################################################################################

def sumN(n):

    ret = int((n*(n + 1)/2))
    print(f"Sum of {n} natural numbers is: {ret}")

def main():

    print("Enter N: ")
    n = int(input())

    sumN(n)

if __name__ == "__main__":
    main()
