Algoritmo Estacionamiento_MALDONADO
	Definir hora_entrada, hora_salida Como Cadena
    Definir horas, minutos, total_minutos, costo Como Entero
    Definir h_entrada, m_entrada, h_salida, m_salida Como Entero
	
    Escribir "Ingrese la hora de entrada (formato 24 horas HH:MM): "
    Leer hora_entrada
    Escribir "Ingrese la hora de salida (formato 24 horas HH:MM): "
    Leer hora_salida
	
    h_entrada = convertirANumero(Subcadena(hora_entrada, 1, 2))
    m_entrada = convertirANumero(Subcadena(hora_entrada, 4, 5))
    h_salida = convertirANumero(Subcadena(hora_salida, 1, 2))
    m_salida = convertirANumero(Subcadena(hora_salida, 4, 5))
	
    total_minutos = (h_salida * 60 + m_salida) - (h_entrada * 60 + m_entrada)
	
    Si total_minutos < 15 Entonces
        costo = 0
        Escribir "El estacionamiento es gratuito."
    Sino
        horas = total_minutos / 60
        minutos = total_minutos % 60
        costo = horas * 15
        Si minutos > 0 Entonces
            costo = costo + ((minutos + 14) / 15) * 6
        FinSi
        Escribir "El costo total es: ", costo, " pesos."
    FinSi
FinAlgoritmo
