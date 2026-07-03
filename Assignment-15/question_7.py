#######################################################################################
# Name:         question)7.py
# Description:  Write a lambda function using filter which accepts a list of strings 
#               and returns a list of strings having length greater than 5
# Input:        List of strings
# Output:       List of strings with length > 5
# Date:         03-07-2026
# Author:       Ritesh Jillewad
#######################################################################################

string_len = lambda x: len(x) > 5

def main():

    names = ["Ritesh", "HelloWorld", "Demo"]
    print(f"Original list: {names}")

    ret = list(filter(string_len, names))
    print(f"Filtered list: {ret}")

if __name__ == "__main__":
    main()
