
if __name__ == '__main__':
    numhoras = input("write num hours ")
    num2 = input("write price * h ")
    numfijo = int(22)
    aprtHora = int(8)

    numhoras = int(numhoras)
    num2 = float(num2)

    salario = (numhoras * numfijo) * num2

    if numhoras > aprtHora:
        res = numhoras - aprtHora
        extra = res * num2 / 2
        salario = salario + extra


    print(salario)
    
    

