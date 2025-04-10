"""
Imprime los primeros n números de la secuencia.
"""

def fibonacci(n):
    secuencia = [0]
    
    for i in range(0, n):
        if (i < 2):
            secuencia.append(1)

        else:
            secuencia.append(secuencia[-1] + secuencia[-2])

        print(secuencia[i])


fibonacci(6)