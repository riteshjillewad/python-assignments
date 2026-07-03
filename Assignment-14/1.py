#######################################################################################
# Name:         question_1.py
# Description:  Lambda function which accepts one number and return the square
# Input:        Marks
# Output:       Grades
# Date:         28-06-2026
# Author:       Ritesh Jillewad
#######################################################################################

square = lambda x: x * x

def main():

    print("Enter number: ")
    num = int(input())

    ret = square(num)
    print(f"Square of {num}: {ret}")

if __name__ == "__main__":
    main()
