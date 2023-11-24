# 1. Crea un programa en Python que dado un número entero que
# designa un periodo de tiempo expresado en segundos, imprima el
# equivalente en días, horas, minutos y segundos. Por ejemplo: 300000
# segundos serán 3 días, 11 horas, 20 minutos y 0 segundos. Por ejemplo: 7400
# segundos serán 0 días, 2 horas, 3 minutos y 20 segundos.

def inAsec(num):
    return int(num) % 60


def secAmin(num):
    return int(num) // 60


def minAhoras(num):
    return int(num) // 60


def horaAdia(num):
    return int(num) // 24


if __name__ == '__main__':

    while True:
        try:
            second = int(input('Ingrese los segundos: '))
            break
        except ValueError:
            print('Ingrese un número válido.')
            continue

    sec = inAsec(second)
    print('segundos:', sec)

    min = secAmin(second)
    print('minutos:', min)

    hours = minAhoras(min)
    print('horas:', hours)

    days = horaAdia(hours)
    print('días:', days)