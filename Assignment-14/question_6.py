#######################################################################################
# Name:         question_6.py
# Description:  Lambda function which return true if number is odd, else return false
# Input:        Number
# Output:       True or False
# Date:         03-07-2026
# Author:       Ritesh Jillewad
#######################################################################################

is_odd = lambda x: True if x % 2 != 0 else False

# is_odd = lamdba x: x % 2 != 0

def main():

    print("Enter number1: ")
    num = int(input())

    ret = is_odd(num)
    print(f"{num}: {ret}")

if __name__ == "__main__":
    main()
