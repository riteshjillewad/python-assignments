########################################################################################
# Name:        question_6.py
# Description: Print the following pattern
# Input:       Num
# Output:      Right triangle pattern
# Date:        04-07-2026
# Author:      Ritesh Jillewad
########################################################################################

def print_pattern(num) -> None:

    for i in range(num, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

def main():

    print("Enter number: ")
    num = int(input())

    print_pattern(num)

if __name__ == "__main__":
    main()