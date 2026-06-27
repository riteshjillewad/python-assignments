######################################################################################
# Name:         question_6.py
# Description:  Function to display: data type, memory address, size of datatype
# Input:        void
# Output:       void
# Author:       Ritesh Jillewad
######################################################################################

import sys

def display(value):

    print(value)
    print(type(value))
    print(id(value))
    print(sys.getsizeof(value))

def main():

    ret = display(22)
    print(ret)
    print(type(ret))

if __name__ == "__main__":
    main()
