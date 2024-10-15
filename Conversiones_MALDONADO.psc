Algoritmo Conversiones
	Definir pulgadas, pies, yardas, cm, m Como Real
	
	Escribir "Ingrese el número la medida en pies que desea convertir"
	Leer pies
	
	Escribir "Elija la medida a la que quiera convertir"
	Escribir "1. PULGADAS"
	Escribir "2. YARDAS"
	Escribir "3. CM"
	Escribir "4. METROS"
	Leer conversión
	
	Si conversión = 1 Entonces
		pulgadas <- pies * 12
		Escribir pies, " pies son: ",pulgadas, " pulgadas"
	SiNo
		Si conversión = 2 Entonces
			yardas <- pies * .333
			Escribir pies, " pies son: ",yardas, " yardas"
		SiNo
			Si conversión = 3 Entonces
				cm <- pies * 30.48
				Escribir pies, " pies son: ",cm, " centímetros"
			SiNo
				Si conversión = 4 Entonces
					m <- pies * .3048
					Escribir pies, " pies son: ",m, " metros"
				SiNo
					Escribir "La opción seleccionada no es válida"
				Fin Si
			Fin Si
		Fin Si
	Fin Si
FinAlgoritmo
