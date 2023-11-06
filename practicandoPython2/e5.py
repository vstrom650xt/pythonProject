#5. Crea un programa en Python que, a partir del número de DNI,
# calcule la letra que le corresponde. Busca en internet la operación
# que tienes que realizar y la tabla de correspondencia. Busca dicha
# tabla y valida que tanto el número sea válido y esté dentro de rango.
# Define una función para realizar el cálculo.
def calcular_letra_dni(numero_dni):
    # Comprobar si el número de DNI es válido (debe estar entre 0 y 99999999)
    if 0 <= numero_dni <= 99999999:
        tabla_correspondencia = "TRWAGMYFPDXBNJZSQVHLCKE"

        # Calcular la letra del DNI
        letra = tabla_correspondencia[numero_dni % 23]

        return letra
    else:
        return "Número de DNI no válido"

if __name__ == "__main__":
    numero_dni = int(input("Ingrese el número de DNI (sin letra): "))
    letra_calculada = calcular_letra_dni(numero_dni)

    if letra_calculada != "Número de DNI no válido":
        print(f"La letra del DNI {numero_dni} es: {letra_calculada}")
    else:
        print(letra_calculada)