# 2. Crea un programa que dado el PID de un proceso devuelva:
# - información relevante de dicho proceso
# - dónde se encuentra el archivo ejecutable
# (busca información y juega con subprocess.check_output() o con psutil.Process())
import subprocess


def obtenerInfo(pid):
    proceso = subprocess.call('ps -q ' + str(pid) + ' -f', shell=True)
    print(proceso)


if __name__ == "__main__":
    pid = int(input("pon pid"))
    obtenerInfo(pid)
