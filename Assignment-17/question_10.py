########################################################################################
# Name:        question_10.py
# Description: Function to return the addition of digits in number
# Input:       Num
# Output:      Addition of digits
# Date:        04-07-2026
# Author:      Ritesh Jillewad
########################################################################################

def add_digits(number: int) -> int:

    if number == 0:
        return 0

    digit_sum = 0
    number = abs(number)

    while number != 0:
        digit_sum = digit_sum + number % 10
        number = number // 10

    return digit_sum

def main():

    print("Enter number: ")
    num = int(input())

    ret = add_digits(num)
    print(f"Addition of digits in {num} are: {ret}")

if __name__ == "__main__":
    main()