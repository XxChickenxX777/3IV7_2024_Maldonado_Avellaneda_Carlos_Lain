Proceso Sistema_Inventario
    Definir nombreP Como Cadena
    Definir codigoP, cantidadP, precioP, ventasT, totalVentasDelProducto Como Real
    Definir opcion, cantidadVendida Como Entero
    ventasTotales = 0
    
    Mientras Verdadero Hacer
        Escribir " SISTEMA DE GESTI�N DE INVENTARIOS"
        Escribir "1. Ingresar nuevo producto"
        Escribir "2. Actualizar stock (Registrar venta)"
        Escribir "3. Consultar inventario"
        Escribir "4. Generar reporte de ventas"
        Escribir "5. Salir"
        Escribir "Seleccione una opci�n: "
        Leer opcion
	
        Segun opcion Hacer
            Caso 1:
                Escribir "Ingrese el nombre del producto:"
                Leer nombreP
                Escribir "Ingrese el c�digo del producto:"
                Leer codigoP
                Escribir "Ingrese la cantidad en stock:"
                Leer cantidadP
                Escribir "Ingrese el precio del producto:"
                Leer precioP
                totalVentasDelProducto=0
                Escribir "Producto ingresado correctamente."
				
            Caso 2:
                Si cantidadP > 0 Entonces
                    Escribir "Ingrese la cantidad vendida:"
                    Leer cantidadVendida
                    
                    Si cantidadP >= cantidadVendida Entonces
                        cantidadP = cantidadP - cantidadVendida
                        totalVentasDelProducto = cantidadVendida * precioP
                        ventasTotales = ventasT + totalVentasDelProducto
                        Escribir "Venta registrada correctamente."
                    SiNo
                        Escribir "No hay suficiente stock disponible."
                    FinSi
                SiNo
                    Escribir "No hay stock disponible.Ingrese m�s stock."
                FinSi
                
            Caso 3:
                Escribir " INVENTARIO ACTUAL"
                Escribir "Producto: ", nombreP
                Escribir "C�digo: ", codigoP
                Escribir "Cantidad en stock: ", cantidadP
                Escribir "Precio unitario: $", precioP
				
            Caso 4:
                Escribir " REPORTE DE VENTAS"
                Escribir "Producto: ", nombreP
                Escribir "C�digo: ", codigoP
                Escribir "Ventas del producto: $", totalVentasDelProducto
                Escribir "Ventas totales del d�a: $", ventasT
				
            Caso 5:
                Escribir "Saliendo del sistema"

De Otro Modo:
	Escribir "Opci�n no v�lida. Intente nuevamente."
FinSegun
FinMientras
FinProceso

