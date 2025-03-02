# Programa 2: Ordenación de una fila específica en la matriz 3x3

def ordenar_fila(matriz, fila):
    matriz[fila].sort()
    return matriz

# Definir una matriz 3x3
matriz2 = [
    [30, 10, 25],
    [40, 35, 15],
    [50, 20, 45]
]

fila_ordenar = int(input("Ingrese la fila a ordenar (0, 1 o 2): "))
print("Matriz original:")
for fila in matriz2:
    print(fila)

matriz_ordenada = ordenar_fila(matriz2, fila_ordenar)

print("Matriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)
