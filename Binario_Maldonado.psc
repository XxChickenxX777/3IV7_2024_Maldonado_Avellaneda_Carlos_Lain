Algoritmo Conversi�n_Binaria
	Definir num Como Entero
	Definir cociente Como Real
	Definir binario Como texto
	
	binario = ""
	
	Escribir "Ingresa el n�mero que deseas convertir a decimal"
	Leer num
	
	Si num >= 0 Entonces
		Mientras num > 0 Hacer
			residuo = num%2
			nuevobinario <- ConvertirATexto(residuo)
			binario = nuevobinario + binario
			
			num = Trunc(num/2)
		Fin Mientras
		
		Si binario="" Entonces
			binario= "0"
		FinSi
		
		Escribir "El n�mero en binario es: ", binario
		
	Fin Si
FinAlgoritmo
