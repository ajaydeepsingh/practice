"""
You're given three integers, a, b and c. It is guaranteed that two of these 
integers are equal to each other. What is the value of the third integer?
"""

def extraNumber(a, b, c):

    if a / b == 1:
        return c
    if a / c == 1:
        return b
    if b / c == 1:
        return a

