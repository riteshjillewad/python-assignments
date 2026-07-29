# =========================================================================================
# Name:        Assignment_26_1.py
# Description: Implement a class named Circle with following requirements:
#              - Three instance variables: radius, area, circumference
#              - One class variable named PI = 3.14
#              - Constructor to initialize variables
#              - Implement the following method:
#                - accept():                 accept radius of circle from user
#                - calculateArea():          calculate area of circle and store it in area variable
#                - calculateCircumference(): calculate circumference of circle
#                - display()               : display radius, area and circumference
# Input:       Void
# Output:      Class design
# Date:        29-07-2026
# Author:      Ritesh Jillewad
# =========================================================================================

class Circle:
    # class variable
    PI = 3.14
    
    # constructor to initialize instance variables
    def __init__(self):
        # instance variable
        self.radius = 0.0
        self.area = 0.0
        circumference = 0.0
        
    # instance method
    def accept(self):
        
        print("\nEnter radius of circle: ")
        self.radius = float(input())
        
    # instance method
    def calculateArea(self):
        self.area = Circle.PI * self.radius * self.radius
        
    # instance method
    def calculateCircumference(self):
        self.circumference = 2 * Circle.PI * self.radius
        
    # instance method
    def display(self):
        print("\nCircle Details")
        print("------------------------")
        print(f"Radius         : {self.radius}")
        print(f"Area           : {self.area}")
        print(f"Circumference  : {self.circumference}")
        print("------------------------")
        
def main():
    
    obj1 = Circle()
    obj2 = Circle()
    
    obj1.accept()
    obj1.calculateArea()
    obj1.calculateCircumference()
    obj1.display()
    
    obj2.accept()
    obj2.calculateArea()
    obj2.calculateCircumference()
    obj2.display()

if __name__ == "__main__":
    main()
        
        
        
        