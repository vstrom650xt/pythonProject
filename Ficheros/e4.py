import os
def mostrarX():
    fichero = '../mbox.txt'
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    cont7 = 0
    if os.path.isfile(fichero):
        man = open(fichero)
        for a in man:
            linea = a.strip()
            if linea.startswith('Mon'):
                cont1 +=1
            if linea.startswith('Tue'):
                cont2 += 1
            if linea.startswith('Wed'):
                cont3 += 1
            if linea.startswith('Thu'):
                cont4 += 1
            if linea.startswith('Fri'):
                cont5 += 1
            if linea.startswith('Sat'):
                cont6 += 1
            if linea.startswith('Sun'):
                cont7 += 1

        print('el lunes tiene', cont1)
        print('el m tiene', cont2)
        print('el mm tiene', cont3)
        print('el j tiene', cont4)
        print('el v tiene', cont5)
        print('el s tiene', cont6)
        print('el d tiene', cont7)

    else:
        print('no existe')


if __name__ == '__main__':
    print(mostrarX())