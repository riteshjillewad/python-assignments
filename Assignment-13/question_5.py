#######################################################################################
# Name:         question_5.py
# Description:  Accept marks and display grade
# Input:        Marks
# Output:       Grades
# Date:         28-06-2026
# Author:       Ritesh Jillewad
#######################################################################################

def displayMarks(marks):

    if marks < 0 or marks > 100:
        print("Invalid marks!")
    elif marks >= 75:
        print("Distinction")
    elif marks >= 60:
        print("First Class")
    elif marks >= 50:
        print("Second Class")
    else:
        print("Fail")

def main():

    print("Enter marks: ")
    marks = int(input())

    displayMarks(marks)

if __name__ == "__main__":
    main()