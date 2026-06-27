#######################################################################################
# Name:         question_5.py
# Description:  Accept number and check if divisible by 3 and 5
# Input:        Number
# Output:       True or false
# Date:         27-06-2026
# Author:       Ritesh Jillewad
#######################################################################################

def chkDivisible(no):
    
    if no % 3 == 0 and no % 5 == 0:
        print(no, "divisible by 3 and 5")
    else:
        print(no, "not divisible by 3 and 5")

def main():
    
    print("Enter a number: ")
    no = int(input())

    chkDivisible(no)
    
if __name__ == "__main__":
    main()