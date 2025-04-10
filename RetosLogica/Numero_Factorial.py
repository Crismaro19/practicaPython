"""
Calcula el factorial de un número n.
"""
import math

def factorial_math(n):
    return math.prod([i for i in range(1, n+1)])

print("Factorial con math",factorial_math(10))



def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

print("Factorial ", factorial(10))
