import random
import time

def adivinar_numero():
    numero_aleatorio = random.randint(0, 100)
    intentos = 0
    inicio_tiempo = time.time()

    while True:
        intento = int(input("Adivina el número (entre 0 y 100): "))
        intentos += 1

        if intento < numero_aleatorio:
            print("El número es más grande.")
        elif intento > numero_aleatorio:
            print("El número es más pequeño.")
        else:
            fin_tiempo = time.time()
            tiempo_transcurrido = fin_tiempo - inicio_tiempo
            print(f"Felicidades, adivinaste el número {numero_aleatorio} en {intentos} intentos y {tiempo_transcurrido:.2f} segundos.")
            break

if __name__ == '__main__':
    adivinar_numero()