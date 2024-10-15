Algoritmo Conversiones_Temperatura
	Definir f, c, k, r Como Real
	
	Escribir "Ingrese la temperatura en grados fahrenheit que desea convertir"
	Leer f
	
	Escribir "Elija la medida a la que quiera convertir"
	Escribir "1. Celcius"
	Escribir "2. Kelvin"
	Escribir "3. Rankine"
	Leer conversión
	
	Segun conversión Hacer
		1:
			c <- (f-32)/1.8
			Escribir f, " grados fahrenheit son: ",c, " grados celcius"
		2:
			k <- ((f-32)/1.8)+273.15
			Escribir f, " grados fahrenheit son: ",k, " grados kelvin"
		3:
			r <- f+459.67
			Escribir f, " grados fahrenheit son: ",r, " grados rankine"
		De Otro Modo:
			Escribir "La opción seleccionada no es válida"
	Fin Segun
	
FinAlgoritmo
