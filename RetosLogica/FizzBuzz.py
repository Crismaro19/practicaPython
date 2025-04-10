"""
Escribe un programa que imprima los números del 1 al 100.
Pero:

    Para los múltiplos de 3, imprime "Fizz" en lugar del número.

    Para los múltiplos de 5, imprime "Buzz".

    Para los múltiplos de ambos (o sea, de 3 y 5), imprime "FizzBuzz".
"""

def fizzBuzz (multiplo1, multiplo2, rango):
    rango += 1

    for i in range(1, rango):
                   
        if (i % multiplo1 == 0 and i % multiplo2 == 0 ):
            print("FizzBuzz")

        elif (i % multiplo1 == 0 ):
            print("Fizz")
            
        elif(i % multiplo2 == 0):
            print("Buzz")

        else:    
            print(i)

fizzBuzz(3, 5, 100)