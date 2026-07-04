########################################################################################
# Name:        question_9.py
# Description: Write a program to display first 10 even numbers on screen
# Input:       void
# Output:      First 10 even numbers
# Date:        04-07-2026
# Author:      Ritesh Jillewad
########################################################################################

def print_even():

    for i in range(2, 21, 2):
        print(i, end=" ")

def main():

    print("First 10 even numbers are: ")
    print_even()

if __name__ == "__main__":
    main()

