def calcular_salario(numhoras, num2):
    salario = (numhoras * numfijo) * num2
    if numhoras > aprtHora:
        res = numhoras - aprtHora
        extra = res * num2 / 2
        salario += extra

    return salario


if __name__ == '__main__':
    while True:
        try:
            numhoras = input(" num horas ")
            num2 = input("precio * h ")

            numhoras = int(numhoras)
            num2 = float(num2)

            numfijo = 22
            aprtHora = 8

            salario = calcular_salario(numhoras, num2)

            print("El salario es:", salario)
            break
        except ValueError:
            print("Error: introducir valores numéricos")
