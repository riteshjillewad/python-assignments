#######################################################################################
# Name:         question_2.py
# Description:  Accept one number and print it's factors
# Input:        Int
# Output:       Factors
# Date:         28-06-2026
# Author:       Ritesh Jillewad
#######################################################################################

def printFactors(num):

    ret = list()

    for i in range(1, num + 1):
        if num % i == 0:
            ret.append(i)

    return ret


def main():

    print("Enter number: ")
    num = int(input())

    factors = printFactors(num)
    print(f"Factors of {num} are: ")
    print(factors)


if __name__ == "__main__":
    main()