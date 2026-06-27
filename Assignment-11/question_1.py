#######################################################################################
# Name:         question_1.py
# Description:  Accept number and check if it is prime or not
# Input:        Int
# Output:       Prime or non-prime
# Date:         27-06-2026
# Author:       Ritesh Jillewad
#######################################################################################

def chkPrime(num):

    if num <= 1:
        return False
    
    if num == 2:
        return True
    
    if num % 2 == 0:
        return False
    
    for i in range(3, num, 2):
        if num % i == 0:
            return False
        
    return True


def main():

    print("Enter number: ")
    num = int(input())

    ret = chkPrime(num)
    if ret == True:
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")


if __name__ == "__main__":
    main()
