def leerFichero():
    archivo = '../clown.txt'
    contador=0
    with open(archivo, 'r') as reader:
        for linea in open(archivo):
            contador = contador + 1
            print(linea)
        cont = reader.read()
        print(contador)
        print(cont)


if __name__ == '__main__':
    leerFichero()
