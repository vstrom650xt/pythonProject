#
# 8. Crea un programa que calcule el factorial de un número entero introducido
# por el usuario. El número introducido por el usuario debe ser mayor que 0 y menor a 20.
# De no ser así, el programa debe pedirlo de nuevo tantas veces como sea necesario.

if __name__ == '__main__':
    num = input('pon num')
    result = 1
    for i in reversed(range(1, int(num))):
        result *= i

    print(result)
