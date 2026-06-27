#######################################################################################
# Name:         question_4.py
# Description:  Accept number and print it's cube
# Input:        Number
# Output:       Cube of number
# Date:         27-06-2026
# Author:       Ritesh Jillewad
#######################################################################################

def displayCube(no):
    
    ret = no * no * no
    print("Cube:", ret)

def main():
    
    print("Enter a number: ")
    no = int(input())

    displayCube(no)
    
if __name__ == "__main__":
    main()