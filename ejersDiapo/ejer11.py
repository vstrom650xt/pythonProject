import os
def mostrarX():
    fichero = '../mbox-short.txt'
    if os.path.isfile(fichero):
        man = open(fichero)
        for linea in man:
            if linea.startswith('X-'):
                print(linea)
    else:
        print('no existe')


if __name__ == '__main__':
    print(mostrarX())