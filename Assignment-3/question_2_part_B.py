######################################################################################
# Name:         question_2_part_B.py
# Description:  Function with parameters
# Input:        void
# Output:       void
# Author:       Ritesh Jillewad
######################################################################################

def addition(num1, num2):

    return num1 + num2


def main():

    print("Enter first number: ")
    num1 = int(input())

    print("Enter second number: ")
    num2 = int(input())

    ret = addition(num1, num2)
    print("Addition is: ", ret)

if __name__ == "__main__":
    main()
