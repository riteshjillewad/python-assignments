##########################################################################################
# Name:        Assignment_20_4.py
# Description: Write an application that creates three separate threads: small, capital, digits
#              1. All the threads should accept string as input
#              2. The small thread should count and display the number of lowercase characters
#              3. The capital thread should count and display the number of uppercase characters
#              4. The digits thread should count and display number of numeric digits
#              5. Each thread should display its threadID and threadName also
# Input:       None
# Output:      int 
# Date:        09-07-2026
# Author:      Ritesh Jillewad
##########################################################################################

import threading

def count_small(data: str) -> None:
    count = 0

    for ch in data:
        if ch.islower(): 
            count += 1

    t_name = threading.current_thread().name
    t_id = threading.get_ident()
    
    print(f"THREAD NAME: {t_name}\nTHREAD ID: {t_id}\nTASK: Lowercase letters in '{data}': {count}\n")

def count_capital(data: str) -> None:
    count = 0

    for ch in data:
        if ch.isupper(): 
            count += 1

    t_name = threading.current_thread().name
    t_id = threading.get_ident()

    print(f"THREAD NAME: {t_name}\nTHREAD ID: {t_id}\nTASK: Uppercase letters in '{data}': {count}\n")

def count_digits(data: str) -> None:
    count = 0

    for ch in data:
        if ch.isdigit(): 
            count += 1

    t_name = threading.current_thread().name
    t_id = threading.get_ident()

    print(f"THREAD NAME: {t_name}\nTHREAD ID: {t_id}\nTASK: Numeric digits in '{data}': {count}\n")

def main():
    
    print("Enter input data: ")
    data = input()

    small_thread   = threading.Thread(target=count_small,   args=(data, ), name="Small_Thread")
    capital_thread = threading.Thread(target=count_capital, args=(data, ), name="Capital_Thread")
    digit_thread   = threading.Thread(target=count_digits,  args=(data, ), name="Digit_Thread")

    small_thread.start()
    capital_thread.start()
    digit_thread.start()

    small_thread.join()
    capital_thread.join()
    digit_thread.join()

if __name__ == "__main__":
    main()