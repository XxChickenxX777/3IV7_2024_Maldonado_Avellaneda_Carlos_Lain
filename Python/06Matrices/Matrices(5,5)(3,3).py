print("A Matriz de 3x3")
print("B Matriz de 5x5")
opción = input("Eliga una opción: ").upper()

if opción =="A":
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

    def im():
        matriz = []
        for i in range(3):
            fila = []
            for j in range(3):
                valor = float(input("Ingrese los mismos datos de las otras 2 matrices: "))
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
    
    def t_matriz(matriz1, matriz2):
        matriz_t = []
        for j in range(3):
            fila = []
            for i in range(3):
                fila.append(matriz1[i][j] + matriz2[i][j])
            matriz_t.append(fila)
        return matriz_t
    
    def imprimir_matriz(matriz):
        for i in matriz:
            print(i)

    def imprimir_matrizt(matriz_t):
        for j in matriz_t:
            print(j)

    print("Matriz 1: ")
    matriz1 = ingresar_matriz()

    print("Matriz 2: ")
    matriz2 = ingresar_matriz()

    matriz_Resultado = sumar_matriz(matriz1, matriz2)

    print("El resultado es: ")
    imprimir_matriz(matriz_Resultado)

    print("Matriz 1: ")
    matriz1 = im()
    print("Matriz 2: ")
    matriz2 = im()
    matrizv = t_matriz(matriz1, matriz2)
    print("La matriz transposicionada es: ")
    imprimir_matrizt(matrizv)

elif opción =="B":
    def ingresar_matrize():
        matrize = []
        print("Introduce los valores de la matriz de 5x5")
        for i in range(5):
            filae = []
            for j in range(5):
                valore = float(input("Elemento: [{i+1}] [{j+1}]: "))
                filae.append(valore)
            matrize.append(filae)
        return matrize
    
    def ime():
        matrize = []
        for i in range(5):
            filae = []
            for j in range(5):
                valore = float(input("Ingrese los mismos datos de las otras 2 matrices: "))
                filae.append(valore)
            matrize.append(filae)
        return matrize

    def sumar_matrize(matriz1e, matriz2e):
        matrize_suma = []
        for i in range(5):
            filae = []
            for j in range(5):
                filae.append(matriz1e[i][j] + matriz2e[i][j])
            matrize_suma.append(filae)
        return matrize_suma

    def t_matrize(matriz1e, matriz2e):
        matrize_t = []
        for j in range(5):
            filae = []
            for i in range(5):
                filae.append(matriz1e[i][j] + matriz2e[i][j])
            matrize_t.append(filae)
        return matrize_t
    
    def imprimir_matriz(matriz):
        for filae in matriz:
            print(filae)

    def imprimir_matrizte(matrize_t):
        for j in matrize_t:
            print(j)

    print("Matriz 1: ")
    matriz1e = ingresar_matrize()

    print("Matriz 2: ")
    matriz2e = ingresar_matrize()

    matrize_Resultado = sumar_matrize(matriz1e, matriz2e)

    print("El resultado es: ")
    imprimir_matriz(matrize_Resultado)
    print("Matriz 1: ")
    matriz1 = ime()
    print("Matriz 2: ")
    matriz2 = ime()
    matrizv = t_matrize(matriz1, matriz2)
    print("La matriz transposicionada es: ")
    imprimir_matrizte(matrizv)
else:
    print("Opción no válida")