import math

cantidad_estrellas = 2 * int(input("Ingrese la altura de la piramide:"))

for i in range(1, cantidad_estrellas, 2):
    print(" "*math.floor((cantidad_estrellas-i)/2), "*"*i)
