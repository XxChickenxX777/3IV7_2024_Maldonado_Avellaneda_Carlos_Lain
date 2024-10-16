Algoritmo Fórmula_General
	Definir ra, x1, x2, a, b, c Como real
	
	Repetir
		Escribir "Ingresa el valor de a"
		Leer a
		Escribir "Ingresa el valor de b"
		Leer b
		Escribir "Ingresa el valor de c"
		Leer c
		
		ra <- ((b)^2-(4*a*c))
		
		Si ra > 0 Entonces
			x1 <- (-b+raiz(ra))/2
			x2 <- (-b-raiz(ra))/2
			Escribir "El valor de x1 es: ", x1
			Escribir "El valor de x2 es: ", x2
		SiNo
			Escribir "La solución es irreal"
		FinSi
		Escribir "Si desea resolver otra ecuación cuadrática ingrese 101 de lo contrario ingrese 102"
		Leer cont
	Hasta Que cont = 102
	
	
FinAlgoritmo