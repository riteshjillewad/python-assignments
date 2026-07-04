# Our module file for problems based on arrays/n-numbers

def ChkPrime(num: int) -> bool:

    if num <= 1:
        return False
    
    if num == 2:
        return True
    
    if num % 2 == 0:
        return False
    
    for i in range(3, num, 2):
        if num % i == 0:
            return False
        
    return True