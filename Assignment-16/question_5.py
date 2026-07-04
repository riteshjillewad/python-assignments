########################################################################################
# Name:        question_5.py
# Description: Write a program to display 10 to 1 on screen
# Input:       void
# Output:      10 9 8 7 6 5 4 3 2 1
# Date:        04-07-2026
# Author:      Ritesh Jillewad
########################################################################################

def display():
    
    for i in range(10, 0, -1):
        print(i, end=" ")

def main():

    display()

if __name__ == "__main__":
    main()

