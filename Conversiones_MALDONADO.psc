Algoritmo Conversiones
	Definir pulgadas, pies, yardas, cm, m Como Real
	
	Escribir "Ingrese el n�mero la medida en pies que desea convertir"
	Leer pies
	
	Escribir "Elija la medida a la que quiera convertir"
	Escribir "1. PULGADAS"
	Escribir "2. YARDAS"
	Escribir "3. CM"
	Escribir "4. METROS"
	Leer conversi�n
	
	Si conversi�n = 1 Entonces
		pulgadas <- pies * 12
		Escribir pies, " pies son: ",pulgadas, " pulgadas"
	SiNo
		Si conversi�n = 2 Entonces
			yardas <- pies * .333
			Escribir pies, " pies son: ",yardas, " yardas"
		SiNo
			Si conversi�n = 3 Entonces
				cm <- pies * 30.48
				Escribir pies, " pies son: ",cm, " cent�metros"
			SiNo
				Si conversi�n = 4 Entonces
					m <- pies * .3048
					Escribir pies, " pies son: ",m, " metros"
				SiNo
					Escribir "La opci�n seleccionada no es v�lida"
				Fin Si
			Fin Si
		Fin Si
	Fin Si
FinAlgoritmo
