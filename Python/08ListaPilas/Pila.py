#aqui vamos a crear toda la logica de programacion de la pila

def crear_pila():
    return []

def apilar(pila, elemento):
    pila.append(elemento)

def esta_vacia(pila):
    return len(pila)==0

def desapilar(pila):
    if esta_vacia(pila):
        raise IndexError("Error no se puede desapilar, la pila esta vacia")
    return pila.pop()

def cima(pila):
    if esta_vacia(pila):
        raise IndexError("La pila esta vacia")
    return pila[-1]

def tamano(pila):
    return len(pila)

def mostrar_pila(pila):
    if esta_vacia(pila):
        raise IndexError("Error no se puede mostrar, la pila esta vacia")
    return f"Pila Actual: {pila}"

