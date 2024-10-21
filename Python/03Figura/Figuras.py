import math

#funcion para calcular el área y perímetro

def rectángulo(base, altura):
    área = base * altura
    perímetro = 2*(base + altura)
    return área, perímetro

def triángulo(base, altura):
    área = (base * altura)/2
    perímetro = l1 + l2 + l3
    return área, perímetro

def esfera(radio):
    volumen = (4/3)*math.pi*radio**3
    return volumen

def menú():
    print("Hola bienvenido a pythen con funciones")
    print("Elije una opción: ")
    print("A.- Área y perímetro de Rectángulo")
    print("B.- Área y perímetro de Triángulo")
    print("C.- Volumen de Esfera")

menú()
opción = input("Introduce la opción a desear: ").upper()

if opción == "A":
    base = float(input("Introduce la base"))
    altura = float(input("Introduce la altura"))
    área, perímetro = rectángulo(base, altura)
    print("El área es de:", área)
    print("El perímetro es de:", perímetro)
elif opción == "B":
    base = float(input("Introduce la base"))
    altura = float(input("Introduce la altura"))
    l1 = float(input("Introduce l1"))
    l2 = float(input("Introduce l2"))
    l3 = float(input("Introduce l3"))
    área, perímetro = triángulo(base, altura, l1, l2, l3)
    print("El área es de:", área)
    print("El perímetro es de:", perímetro)
elif opción == "C":
    radio = float(input("Introduce el radio"))
    volumen = esfera(radio)
    print("El volumen es de: ", volumen)

else:
    print("SOpción no válida")