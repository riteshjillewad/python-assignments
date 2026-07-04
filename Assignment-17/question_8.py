########################################################################################
# Name:        question_8.py
# Description: Print the following pattern
# Input:       Num
# Output:      Numbers pattern
# Date:        04-07-2026
# Author:      Ritesh Jillewad
########################################################################################

def print_pattern(num) -> None:

    """
    for(int i = 1; i <= 5; i++)
    {
        for(int j = 1; j <= i; j++)
        {
            printf("%d\t", j);
        }
        printf("\n");
    }
    """

    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(j, end="  ")
        print()

def main():

    print("Enter number: ")
    num = int(input())

    print_pattern(num)

if __name__ == "__main__":
    main()