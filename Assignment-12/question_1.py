#######################################################################################
# Name:         question_1.py
# Description:  Accept one character and check if it is a vowel or consonant
# Input:        Character
# Output:       Vowel or Consonant
# Date:         28-06-2026
# Author:       Ritesh Jillewad
#######################################################################################

def chkCharacter(data):

    if len(data) != 1:
        print("Please enter only one character.")
        return

    if(data == 'a' or data == 'e' or data == 'i' or data == 'o' or data == 'u' or
        data == 'A' or data == 'E' or data == 'I' or data == 'O' or data == 'U'):
        print(f"{data} is a vowel")

    elif((data >= 'a' and data <= 'z') or (data >= 'A' and data <= 'Z')):
        print(f"{data} is a consonant")

    else:
        print("Invalid character")


def main():

    print("Enter one character: ")
    char = input()

    chkCharacter(char)


if __name__ == "__main__":
    main()