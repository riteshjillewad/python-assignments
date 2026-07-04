########################################################################################
# Name:        question_9.py
# Description: Function to return the number of digits in number
# Input:       Num
# Output:      Number of digits
# Date:        04-07-2026
# Author:      Ritesh Jillewad
########################################################################################

def count_digits(number: int) -> int:

    if number == 0:
        return 1

    digits_count = 0
    number = abs(number)

    while number != 0:
        digits_count += 1
        number = number // 10

    return digits_count

def main():

    print("Enter number: ")
    num = int(input())

    ret = count_digits(num)
    print(f"Number of digits in {num} are: {ret}")

if __name__ == "__main__":
    main()