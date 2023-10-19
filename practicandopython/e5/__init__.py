import math

# Solicitar al usuario qué área desea calcular
opcion = input("¿Desea calcular el área de un triángulo o un círculo? (triángulo/círculo): ").lower()

if opcion.lower() == "triángulo":
    # Calcular el área de un triángulo
    base = float(input("Ingrese la longitud de la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area_triangulo = 0.5 * base * altura
    print(f"El área del triángulo es: " + str(area_triangulo))


elif opcion.lower() == "círculo":
    radio = float(input("Ingrese el radio del círculo: "))
    area_circulo = math.pi * (radio ** 2)
    print(f"El área del círculo es: {area_circulo:.2f}")

else:
    print("Opción no válida. Por favor, elija 'triángulo' o 'círculo'.")

