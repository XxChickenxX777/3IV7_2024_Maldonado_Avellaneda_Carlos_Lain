Algoritmo Contador_Positivo_Negativo
    Definir num, p, n Como Entero
    p <- 0
    n <- 0
    
    Escribir "Introduce una serie de n�meros (0 para terminar):"
    
    Repetir
        Leer num
        Si num > 0 Entonces
            p <- p + 1
        Sino
            Si num < 0 Entonces
                n <- n + 1
            FinSi
        FinSi
    Hasta Que numero = 0
    
    Escribir "Cantidad de n�meros positivos:", p
    Escribir "Cantidad de n�meros negativos:", n
FinAlgoritmo
