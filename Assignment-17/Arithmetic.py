# Module for our arithmetic functions that contains 4 functions:
# 1) Add(no1, no2)
# 2) Sub(no1, no2)
# 3) Mult(no1, no2)
# 4) Div(no1, no2)

def Add(no1: int, no2: int) -> int:
    """
    Returns the addition of two numbers

    Parameters:
    --------------------------
    no1: int
    no2: int

    Return value:
    --------------------------
    int:
        Addition of two numbers
    """

    return no1 + no2

def Sub(no1: int, no2: int) -> int:
    """
    Returns the substraction of two numbers

    Parameters:
    --------------------------
    no1: int
    no2: int

    Return value:
    --------------------------
    int:
        Substraction of two numbers
    """

    return no1 - no2

def Mult(no1: int, no2: int) -> int:
    """
    Returns the multiplication of two numbers

    Parameters:
    --------------------------
    no1: int
    no2: int

    Return value:
    --------------------------
    int:
        Multiplication of two numbers
    """

    return no1 * no2

def Div(no1: int, no2: int) -> int:
    """
    Returns the division of two numbers

    Parameters:
    --------------------------
    no1: int
    no2: int

    Return value:
    --------------------------
    int:
        Division of two numbers
    """

    return no1 // no2