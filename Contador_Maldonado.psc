Algoritmo Contador_Positivo_Negativo
    Definir num, p, n, cont Como Entero
    p <- 0
    n <- 0
    
	Repetir
		Escribir "Introduce una serie de números (0 para terminar):"
		Repetir
			Leer num
			Si num > 0 Entonces
				p <- p + 1
			Sino
				Si num < 0 Entonces
					n <- n + 1
				FinSi
			FinSi
		Hasta Que num = 0
		
		Escribir "Cantidad de números positivos:", p
		Escribir "Cantidad de números negativos:", n
		Escribir "Si desea contar los positivos de otra serie ingrese 101 de lo contrario ingrese 102"
		Leer cont
	Hasta Que cont = 102
		
		
FinAlgoritmo
