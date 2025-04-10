
lista_choco = ["choco1","choco2","choco3","choco4","choco5"]
lista_gansito = ["gansito1", "gansito2", "gansito3"]

lista_galletas = ["galleta1", "galleta2", "galleta3"]
lista_bombom = ["bombom1", "bombom2", "bombom3"]

fila_1 = [lista_choco, lista_gansito]
fila_2 = [lista_galletas, lista_bombom]

maquina = [fila_1, fila_2]


def tomar_producto(fila_P , columna_P):
    rest = maquina[fila_P][columna_P][0]
    del maquina[fila_P][columna_P][0]
    return rest

print(tomar_producto(0,0))
print(lista_choco)
