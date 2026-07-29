# =========================================================================================
# Name:        Assignment_26_3.py
# Description: Implement class named Arithmetic with following characteristics
#              - Two instance varialbes: value1 and value2
#              - Constructor to initialize varialbes to 0
#              - Following instance methods:
#                - accept()         : accept value1 and value2 from user
#                - addition()       : return addition of value1 and value2
#                - subraction()     : return subraction of value1 and value2
#                - multiplication() : return multiplication of value1 and value2
#                - division()       : return division of value1 and value2
# Input:       Void
# Output:      Class design
# Date:        29-07-2026
# Author:      Ritesh Jillewad
# =========================================================================================

class Arithmetic:
    
    # constructor
    def __init__(self):
        self.value1 = 0
        self.value2 = 0
        
    # instance method to accept two numbers
    def accept(self):
        
        print("Enter first number: ")
        self.value1 = float(input())
        
        print("Enter second number: ")
        self.value2 = float(input())
        
    # instance method to return addition
    def addition(self):
        return self.value1 + self.value2
    
    # instance method to return addition
    def subtraction(self):
        return self.value1 - self.value2
    
    # instance method to return multiplication
    def multiplication(self):
        return self.value1 * self.value2
    
    # instance method to return division
    def division(self):
        try:
            return self.value1 / self.value2
            
        except ZeroDivisionError:
            return "Division by zero is not possible"
        
def main():
    
    obj = Arithmetic()
    obj.accept()

    print("\nArithmetic Operations")
    print("----------------------")
    print(f"Addition       : {obj.addition()}")
    print(f"Subtraction    : {obj.subtraction()}")
    print(f"Multiplication : {obj.multiplication()}")
    print(f"Division       : {obj.division()}")

if __name__ == "__main__":
    main()
        
        
    
    