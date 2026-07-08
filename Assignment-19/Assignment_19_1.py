##########################################################################################
# Name:        Assignment_19_1.py
# Description: Write a lambda function that accepts one parameter and return power of two
# Input:       int
# Output:      int
# Date:        09-07-2026
# Author:      Ritesh Jillewad
##########################################################################################

import sys

power_2 = lambda x: x ** 2

def main():
    
    print("Enter number: ")

    try:
        num = int(sys.stdin.readline())
        ret = power_2(num)
        sys.stdout.write(f"Square of {num}: {ret}") 
    except ValueError:
        print("Invalid input!, Please enter an integer.")

if __name__ == "__main__":
    main()