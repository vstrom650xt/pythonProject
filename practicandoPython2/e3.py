# 3. Crea un programa en Python que pida una contraseña por
# teclado e indique si es correcta o incorrecta. La contraseña
# # correcta es “iloveyou123”. Una vez funcione, añade código para que
# si la contraseña era incorrecta la pida de nuevo.

if __name__ == '__main__':
    intento1 = input('pon contraseña')
    intento2 = input('otra vez')
    while intento1 != intento2:
        intento1 = input('pon contraseña')
        intento2 = input('otra vez')

print('ya son iguales')
