def ingresar_matriz():
    matriz = []
    print("Introduce los valores de la matriz de 3x3")
    for i in range(3):
        fila = []
        for j in range(3):
            valor = float(input("Elemento: [{i+1}] [{j+1}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def sumar_matriz(matriz1, matriz2):
    matriz_suma = []
    for i in range(3):
        fila = []
        for j in range(3):
            fila.append(matriz1[i][j] + matriz2[i][j])
        matriz_suma.append(fila)
    return matriz_suma

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

print("Matriz 1: ")
matriz1 = ingresar_matriz()

print("Matriz 2: ")
matriz2 = ingresar_matriz()

matriz_Resultado = sumar_matriz(matriz1, matriz2)

print("El resultado es: ")
imprimir_matriz(matriz_Resultado)