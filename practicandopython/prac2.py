# 1. Crea un programa en Python que dado un número entero que
# designa un periodo de tiempo expresado en segundos, imprima el
# equivalente en días, horas, minutos y segundos. Por ejemplo: 300000
# segundos serán 3 días, 11 horas, 20 minutos y 0 segundos. Por ejemplo: 7400
# segundos serán 0 días, 2 horas, 3 minutos y 20 segundos.

def inAsec(num):
    return int(num) % 60
def secAmin(num , numSec):
    return int(num) / 60
def minAhoras(num):
    return int(num) / 60
def horaAdia(num):
    return int(num) / 24

if __name__ == '__main__':
  #  second = input("pon segundos")
    second = 7400
    sec = inAsec(second)
    print('segundos ' + str(sec))
    min = secAmin(second) - sec
    print('minutos ' + str(min))

    # print(secAmin(second))
    # min = secAmin(second)
    # print(minAhoras(min -second))
    # hora = horaAdia(min)
    # print(horaAdia(min))
