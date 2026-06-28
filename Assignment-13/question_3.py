#######################################################################################
# Name:         question_3.py
# Description:  Accept number and check if it is perfect number or not
# Input:        Int
# Output:       Perfect or non-perfect
# Date:         28-06-2026
# Author:       Ritesh Jillewad
#######################################################################################

def chkPerfect(num):

    sumFactors = 0

    if num <= 0:
        return False

    for i in range(1, num):
        if num % i == 0:
            sumFactors = sumFactors + i
        
    return (num == sumFactors)


def main():

    print("Enter a number: ")
    num = int(input())

    ret = chkPerfect(num)
    if ret == True:
        print(f"{num} is perfect number")
    else:
        print(f"{num} is not a perfect number")


if __name__ == "__main__":
    main()
