def binario_a_decimal(binario):
    decimal = 0
    for digito in binario:
        decimal = decimal * 2 + int(digito)
    return decimal

def decimal_a_binario(decimal):
    if decimal == 0:
        return "0"
    binario = ""
    numero = decimal
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2
    return binario

seguir_ejecutando = "si"

while seguir_ejecutando == "si":
    print("1. Binario a Decimal")
    print("2. Decimal a Binario")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        binario = input("Ingresa un número binario: ")
        print("En decimal es:", binario_a_decimal(binario))
    
    elif opcion == "2":
        decimal = int(input("Ingresa un número decimal: "))
        print("En binario es:", decimal_a_binario(decimal))
    
    seguir_ejecutando = input("¿Quieres hacer otra conversión?").lower()

print("¡Hasta luego!")
