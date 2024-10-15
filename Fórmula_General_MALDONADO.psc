Algoritmo Fórmula_General
	Definir ra, x1, x2, a, b, c Como real
	
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
FinAlgoritmo