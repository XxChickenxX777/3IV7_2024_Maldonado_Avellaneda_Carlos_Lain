SubProceso Cuadrado(perimetro Por Referencia, area Por Referencia)
	Definir lado Como Real
	
	Escribir "Ingrese la longitud del lado:"
	Leer lado
	
	perimetro <- lado * 4
	area <- lado * lado
FinSubProceso

SubProceso Rectangulo(perimetro Por Referencia, area Por Referencia)
	Definir base, altura Como Real
	
	Escribir "Ingrese la base:"
	Leer base
	Escribir "Ingrese la altura:"
	Leer altura
	
	perimetro <- 2 * (base + altura)
	area <- base * altura
FinSubProceso

SubProceso Pentagono(perimetro Por Referencia, area Por Referencia)
	Definir lado, apotema Como Real
	
	Escribir "Ingrese la longitud del lado:"
	Leer lado
	Escribir "Ingrese la apotema:"
	Leer apotema
	
	perimetro <- lado * 5
	area <- (perimetro * apotema) / 2
FinSubProceso

SubProceso Hexagono(perimetro Por Referencia, area Por Referencia)
	Definir lado, apotema Como Real
	
	Escribir "Ingrese la longitud del lado:"
	Leer lado
	Escribir "Ingrese la apotema:"
	Leer apotema
	
	perimetro <- lado * 6
	area <- (perimetro * apotema) / 2
FinSubProceso

SubProceso Octagono(perimetro Por Referencia, area Por Referencia)
	Definir lado, apotema Como Real
	
	Escribir "Ingrese la longitud del lado:"
	Leer lado
	Escribir "Ingrese la apotema:"
	Leer apotema
	
	perimetro <- lado * 8
	area <- (perimetro * apotema) / 2
FinSubProceso

SubProceso Dodecagono(perimetro Por Referencia, area Por Referencia)
	Definir lado, apotema Como Real
	
	Escribir "Ingrese la longitud del lado:"
	Leer lado
	Escribir "Ingrese la apotema:"
	Leer apotema
	
	perimetro <- lado * 12
	area <- (perimetro * apotema) / 2
FinSubProceso

SubProceso Resultados(figura, perimetro, area)
	Escribir "El �rea de ", figura, " es de ", area, " unidades y el per�metro es de ", perimetro, " unidades"
	Escribir ""
FinSubProceso

Algoritmo CalculoFigurasGeometricas
	Definir opcion Como Entero
	Definir perimetro, area Como Real
	
	Repetir
		Escribir "Ingrese la figura geom�trica que deseas conocer su �rea y su per�metro: "
		Escribir "1. Cuadrado (4 lados)"
		Escribir "2. Rect�ngulo (4 lados)"
		Escribir "3. Pent�gono (5 lados)"
		Escribir "4. Hex�gono (6 lados)"
		Escribir "5. Oct�gono (8 lados)"
		Escribir "6. Dodec�gono (12 lados)"
		Escribir "7. Salir"
		
		Leer opcion
		
		Segun opcion Hacer
			1:
				Cuadrado(perimetro, area)
				Resultados("CUADRADO", perimetro, area)
			2:
				Rectangulo(perimetro, area)
				Resultados("RECT�NGULO", perimetro, area)
			3:
				Pentagono(perimetro, area)
				Resultados("PENT�GONO", perimetro, area)
			4:
				Hexagono(perimetro, area)
				Resultados("HEX�GONO", perimetro, area)
			5:
				Octagono(perimetro, area)
				Resultados("OCT�GONO", perimetro, area)
			6:
				Dodecagono(perimetro, area)
				Resultados("DODEC�GONO", perimetro, area)
			7:
			De Otro Modo:
				Escribir "Opci�n inv�lida. Intenta nuevamente."
		FinSegun
		
	Hasta Que opcion = 7
FinAlgoritmo

