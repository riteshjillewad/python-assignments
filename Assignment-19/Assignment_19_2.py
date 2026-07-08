##########################################################################################
# Name:        Assignment_19_2.py
# Description: Write a lambda function that accepts two parameters and return multiplication
# Input:       int
# Output:      Multiplication
# Date:        09-07-2026
# Author:      Ritesh Jillewad
##########################################################################################

multiplication = lambda x, y: x * y

def main():

    try:
        num1 = int(input("Enter number1: "))
        num2 = int(input("Enter number2: "))

        ret = multiplication(num1, num2)
        print(f"Multiplication of {num1} and {num2}: {ret}")

    except ValueError:
        print("Invalid input!")

if __name__ == "__main__":
    main()