##########################################################################################
# Name:        Assignment_26_1.py
# Description: Implement a class named demo with following specifications:
#              - The class should contain two instance variables no1 and no2
#              - The class should contain one class variable named Value
#              - Define a constructor that accepts two parameters and initialize the instance variable
#              - Implement two instance methods:
#                - fun() -> display value of instance variables no1 and no2
#                - gun() -> same
# Input:       Void
# Output:      Class design
# Date:        29-07-2026
# Author:      Ritesh Jillewad
##########################################################################################

class Demo:
    # Class variable
    value = 100
    
    # Constructor
    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2
        
    # Instance method
    def fun(self):
        print(f"Inside fun()")
        print(f"No1 : {self.no1}")
        print(f"No2 : {self.no2}")
        
    # Instance method
    def gun(self):
        print(f"Inside gun()")
        print(f"No1: {self.no1}")
        print(f"No2: {self.no2}")
        
def main():
    
    obj1 = Demo(11, 21)
    obj2 = Demo(51, 101)
    
    obj1.fun()
    obj2.fun()
    
    obj1.gun()
    obj2.gun()
    
if __name__ == "__main__":
    main()
