Algoritmo Censo_personas_MALDONADO
    Definir N, Q Como Entero
    Definir i, j, xj, vivos, menor_edad, mayor_edad Como Entero
    Definir a, b, x Como Entero
    Dimension na(1000), f(1000), p(1000)
    
    Escribir "Ingresa el n�mero de personas y el n�mero de a�os que desea consultar"
    Leer N, Q
    
    Para i = 1 Hasta N Con Paso 1 Hacer
        Escribir "Ingrese el a�o de nacimiento de la persona ", i
        Leer a
		Escribir " y el a�o de fallecimiento de la persona ", i
		Leer b
        na(i) = a
        f(i) = b
    FinPara
    
    Para j = 1 Hasta Q Con Paso 1 Hacer
        Escribir "Ingrese el a�o para la pregunta ", j, ":"
        Leer x
        p(j) = x
    FinPara
    
    Para j = 1 Hasta Q Con Paso 1 Hacer
        xj = p(j)
        vivos = 0
        me_edad = 1000000
        ma_edad = -1
        
        Para i = 1 Hasta N Con Paso 1 Hacer
            Si na(i) <= xj y f(i) >= xj Entonces
                vivos = vivos + 1
                edad = xj - na(i)
                Si edad < me_edad Entonces
                    me_edad = edad
                FinSi
                Si edad > ma_edad Entonces
                    ma_edad = edad
                FinSi
            FinSi
        FinPara
        Escribir "En el a�o ", xj, ":"
        Escribir "Hab�a ", vivos, " vivos"
        Si vivos > 0 Entonces
            Escribir "Edad de la persona m�s joven: ", me_edad
            Escribir "Edad de la persona m�s anciana: ", ma_edad
        FinSi
    FinPara
FinAlgoritmo
