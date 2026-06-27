#######################################################################################
# Name:         question_2.py
# Description:  Function to accept two numbers and find greatest
# Input:        Accept two number
# Output:       Print greatest number
# Date:         27-06-2026
# Author:       Ritesh Jillewad
#######################################################################################

def chkGreater(no1, no2):

    if no1 > no2:
        print(no1, "is greater")
    else:
        print(no2, "is greater")

def main():
    
    print("Enter first number: ")
    no1 = int(input())

    print("Enter second number: ")
    no2 = int(input())

    chkGreater(no1, no2)
    
if __name__ == "__main__":
    main()