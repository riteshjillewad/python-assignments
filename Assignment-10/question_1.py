#######################################################################################
# Name:         question_1.py
# Description:  Function to accept number and print mulltiplication table
# Input:        Int
# Output:       Multiplication table
# Date:         27-06-2026
# Author:       Ritesh Jillewad
#######################################################################################

def printTable(no):

    for i in range(1, 21, 1):
        # print(no,"X",i, "=","",no * i)
        print(f"{no} X {i} = {no * i}")



def main():

    print("Enter number: ")
    no = int(input())

    printTable(no)

if __name__ == "__main__":
    main()

