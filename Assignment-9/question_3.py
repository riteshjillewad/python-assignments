#######################################################################################
# Name:         question_3.py
# Description:  Accept number and print it's square
# Input:        Number
# Output:       Square of number
# Date:         27-06-2026
# Author:       Ritesh Jillewad
#######################################################################################

def displaySquare(no):
    
    ret = no * no
    print("Square:", ret)

def main():
    
    print("Enter a number: ")
    no = int(input())

    displaySquare(no)
    
if __name__ == "__main__":
    main()