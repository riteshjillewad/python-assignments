#######################################################################################
# Name:         question_7.py
# Description:  Lambda function which return true if number is divisible by 5
# Input:        Number
# Output:       True or False
# Date:         03-07-2026
# Author:       Ritesh Jillewad
#######################################################################################

is_divisible = lambda x: x % 5 == 0

def main():

    print("Enter number: ")
    num = int(input())

    ret = is_divisible(num)
    print(f"Is {num} divisible by 5?: {ret}")

if __name__ == "__main__":
    main()
