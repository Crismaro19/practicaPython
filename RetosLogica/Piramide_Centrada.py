import math

"""
piramide con asteriscos
"""

def piramide(n):
    n *= 2 
    for i in range(1, n, 2):
        print(" "*math.floor((n-i)/2), "*"*i)


piramide(2)