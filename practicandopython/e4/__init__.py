numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

if numero1 > numero2:
    mayor = numero1
    menor = numero2
elif numero2 > numero1:
    mayor = numero2
    menor = numero1
else:
    print("Los números son iguales. No se puede determinar si uno es múltiplo del otro.")
    exit()

if mayor % menor == 0:
    print(f"{mayor} es múltiplo de {menor}.")
else:
    print(f"{mayor} no es múltiplo de {menor}.")
