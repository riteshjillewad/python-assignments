########################################################################################
# Name:        question_5.py
# Description: Accept number from user and check if it is prime number or not
# Input:       Num
# Output:      Prime or non-prime
# Date:        04-07-2026
# Author:      Ritesh Jillewad
########################################################################################

def ChK_Prime(num: int) -> bool:

    if num <= 0:
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

    ret = ChK_Prime(num)
    if ret == True:
        print(f"{num} is prime number")
    else:
        print(f"{num} is not prime number")

if __name__ == "__main__":
    main()
