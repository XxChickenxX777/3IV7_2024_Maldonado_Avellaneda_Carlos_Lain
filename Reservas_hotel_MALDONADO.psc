Proceso Reserva_Hotel
    Definir nombreCliente Como Cadena
    Definir fechaEntrada, fechaSalida Como Cadena
    Definir numeroReserva, habitacionSeleccionada, totalHabitaciones, ocupadas, opcion, reservaActiva Como Entero
    totalHabitaciones = 10
    ocupadas = 0
    reservaActiva = 0
	
    Mientras Verdadero Hacer
        Escribir " SISTEMA DE GESTIÓN DE RESERVAS DE HOTEL"
        Escribir "1. Registrar nueva reserva"
        Escribir "2. Cancelar reserva"
        Escribir "3. Consultar disponibilidad de habitaciones"
        Escribir "4. Gestionar ocupación del hotel"
        Escribir "5. Salir"
        Escribir "Seleccione una opción: "
        Leer opcion
        
        Segun opcion Hacer
            Caso 1:
                Si ocupadas < totalHabitaciones Entonces
                    Escribir "Ingrese su nombre:"
                    Leer nombreCliente
                    Escribir "Ingrese la fecha de entrada (dd/mm/aaaa):"
                    Leer fechaEntrada
                    Escribir "Ingrese la fecha de salida (dd/mm/aaaa):"
                    Leer fechaSalida
					
                    Escribir "Habitaciones disponibles:"
                    Escribir "Hay ", totalHabitaciones - ocupadas, " habitaciones disponibles."
					
                    Escribir "Seleccione el número de habitación a reservar (1 a ", totalHabitaciones, "):"
                    Leer habitacionSeleccionada
					
                    Si habitacionSeleccionada >= 1 Y habitacionSeleccionada <= totalHabitaciones Entonces
                        ocupadas = ocupadas + 1
                        reservaActiva = 1
                        numeroReserva = ocupadas
                        Escribir "Reserva confirmada. Su número de reserva es: ", numeroReserva
                    SiNo
                        Escribir "Número de habitación no válido."
                    FinSi
                SiNo
                    Escribir "No hay habitaciones disponibles."
                FinSi
				
            Caso 2:
                Si reservaActiva = 1 Entonces
                    Escribir "Ingrese su número de reserva para cancelar:"
                    Leer numeroReserva
                    Si numeroReserva = ocupadas Entonces
                        ocupadas = ocupadas - 1
                        reservaActiva = 0
                        Escribir "Reserva cancelada correctamente."
                    SiNo
                        Escribir "Número de reserva no válido."
                    FinSi
                SiNo
                    Escribir "No hay reservas activas para cancelar."
                FinSi
				
            Caso 3:
                Escribir " HABITACIONES DISPONIBLES"
                Si ocupadas < totalHabitaciones Entonces
                    Escribir "Hay ", totalHabitaciones - ocupadas, " habitaciones disponibles."
                SiNo
                    Escribir "El hotel está completamente ocupado."
                FinSi
				
            Caso 4:
                Definir porcentajeOcupacion Como Real
                porcentajeOcupacion = (ocupadas / totalHabitaciones) * 100
                Escribir "Porcentaje de ocupación del hotel: ", porcentajeOcupacion, "%"
				
            Caso 5:
                Escribir "Saliendo del sistema..."

De Otro Modo:
	Escribir "Opción no válida. Intente nuevamente."
FinSegun
FinMientras
FinProceso

