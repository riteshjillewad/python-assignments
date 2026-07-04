########################################################################################
# Name:        question_4.py
# Description: Accept number from user and return addition of it's factors
# Input:       Num
# Output:      Addition of factors
# Date:        04-07-2026
# Author:      Ritesh Jillewad
########################################################################################

def addition_factors(num):

    factors_sum = 0
    
    for i in range(1, num):
        if num % i == 0:
            factors_sum += i

    return factors_sum

def main():

    print("Enter number: ")
    num = int(input())

    if num < 0:
        print("Negative numbers not allowed!")
    else:
        ret = addition_factors(num)
        print(f"Addition of factorials of {num}: {ret}")

if __name__ == "__main__":
    main()