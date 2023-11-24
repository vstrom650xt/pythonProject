if __name__ == '__main__':
    while True:
        try:
            numhoras = input(" num horas ")
            num2 = input("precio * h ")

            numhoras = int(numhoras)
            num2 = float(num2)

            numfijo = 22
            aprtHora = 8

            salario = (numhoras * numfijo) * num2

            if numhoras > aprtHora:
                res = numhoras - aprtHora
                extra = res * num2 / 2
                salario += extra

            print("El salario es:", salario)
            break  # Break the loop if valid inputs and calculation are successful
        except ValueError:
            print("Error: introducir valores numéricos")
