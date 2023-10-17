if __name__ == '__main__':
    while True:
        try:
            numhoras = input("Ingrese el número de horas trabajadas: ")
            num2 = input("Ingrese el precio por hora: ")

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
            print("Error: Ingrese un número válido para las horas y el precio por hora.")
