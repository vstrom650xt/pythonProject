import random
import time

def adivinarNum():
    num = random.randint(0, 100)
    intentos = 0
    inicioTiempo = time.time()

    while True:

        intento = int(input("adivina el num "))
        intentos += 1

        if intento < num:
            print("mas grande")
        elif intento > num:
            print("mas pequeño.")
        else:
            finTiempo = time.time()
            totalTiempo = finTiempo - inicioTiempo
            print("numerp de intentos"+ str(intento)+ "tiempo " + str(totalTiempo) + "el nuumero era el " + str(num))
            break

if __name__ == '__main__':
    adivinarNum()