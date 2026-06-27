#######################################################################################
# Name:         question_3.py
# Description:  Function to find the factorial of a number
# Input:        Int
# Output:       Factorial
# Date:         27-06-2026
# Author:       Ritesh Jillewad
#######################################################################################

def factorial(num):

    """
        Equivalent C code:
        
        int fact = 1;

        for(int i = 1; i <= num; i++)
        {
            fact = fact * i;
        }
    """

    fact = 1

    for i in range(num, 0, -1):
        fact = fact * i

    print(f"Factorial of {num} is: {fact}")

def main():

    print("Enter number: ")
    n = int(input())

    factorial(n)

if __name__ == "__main__":
    main()
