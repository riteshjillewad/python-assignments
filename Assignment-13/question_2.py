#######################################################################################
# Name:         question_2.py
# Description:  Accept radius of circle and print area of it
# Input:        Radius
# Output:       Area
# Date:         28-06-2026
# Author:       Ritesh Jillewad
#######################################################################################

def circleArea(radius, PI=3.14):

    return PI * radius * radius

def main():

    print("Enter radius: ")
    radius = float(input())

    ret = circleArea(radius)
    print(f"The area of circle is: {ret}")

if __name__ == "__main__":
    main()
