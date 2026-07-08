##########################################################################################
# Name:        Assignment_21_2.py
# Description: Design a Python application where multiple threads update a shared variable.
#              - Use a Lock to avoid race conditions.
#              - Each thread should increment the shared counter multiple times.
#              - Display the final value of the counter after all threads complete.
# Input:       None
# Output:      int 
# Date:        09-07-2026
# Author:      Ritesh Jillewad
##########################################################################################

import threading

shared_counter = 0
counter_lock = threading.Lock()

INCREMENTS_PER_THREAD = 100000

def update_counter():
    global shared_counter
    
    for _ in range(INCREMENTS_PER_THREAD):
        with counter_lock:
            shared_counter += 1

def main():
    
    threads = list()
    number_of_threads = 5
    
    print(f"Starting value: {shared_counter}")
    print(f"Starting {number_of_threads} threads. Each will increment {INCREMENTS_PER_THREAD} times...")

    for _ in range(number_of_threads):
        t = threading.Thread(target=update_counter)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    expected_value = number_of_threads * INCREMENTS_PER_THREAD
    
    print("\n--- Execution Complete ---")
    print(f"Expected final value: {expected_value}")
    print(f"Actual final value:   {shared_counter}")

if __name__ == "__main__":
    main()