import cola
import vista


def main():
    #diccionario de funciones
    logica_cola = {
        "crear_cola" : cola.crear_cola,
        "encolar" : cola.encolar,
        "desencolar": cola.desencolar,
        "frente" : cola.frente,
        "esta_vacia" : cola.esta_vacia,
        "tamano" : cola.tamano,
        "mostrar_pila" : cola.mostrar_cola
    }

    vista.crear_interfaz(logica_cola)


main()