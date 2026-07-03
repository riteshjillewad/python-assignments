#######################################################################################
# Name:         question_2.py
# Description:  Lambda function which accepts one number and return the cube
# Input:        Marks
# Output:       Grades
# Date:         28-06-2026
# Author:       Ritesh Jillewad
#######################################################################################

square = lambda x: x ** 3

def main():

    print("Enter number: ")
    num = int(input())

    ret = square(num)
    print(f"Cube of {num}: {ret}")

if __name__ == "__main__":
    main()
