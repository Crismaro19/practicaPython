"""
Verifica si un número es primo.
"""

def numero_primo(numero):
    if (numero == 1):
        return "No es primo"
    
    for i in range(2, numero):
        if (numero % i == 0):
            return "No es primo"
    
    return "Es primo"

print(numero_primo(104744))