#5. Crea un programa en Python que, a partir del número de DNI,
# calcule la letra que le corresponde. Busca en internet la operación
# que tienes que realizar y la tabla de correspondencia. Busca dicha
# tabla y valida que tanto el número sea válido y esté dentro de rango.
# Define una función para realizar el cálculo.
def calcularLetra(num):
    if 0 <= num <= 99999999:
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        letra = tabla[num % 23]
        return letra
    else:
        return "no valido"

if __name__ == "__main__":
    dni = int(input("pon dni"))
    letraCalculada = calcularLetra(dni)

    if letraCalculada != "no valido":
        print("La letra del DNI  es" + letraCalculada)
    else:
        print(letraCalculada)