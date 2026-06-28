#######################################################################################
# Name:         question_1.py
# Description:  Accept width and length of rectangle and print it's area
# Input:        Number
# Output:       Area
# Date:         28-06-2026
# Author:       Ritesh Jillewad
#######################################################################################

def rectangleArea(width, length):

    area = 0
    area = width * length

    return area

def main():

    print("Enter width: ")
    width = int(input())

    print("Enter length: ")
    length = int(input())

    ret = rectangleArea(width, length)
    print(f"The area of rectangle is: {ret}")

if __name__ == "__main__":
    main()
