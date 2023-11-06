# 6. Importando la librería subprocess puedes lanzar e interactuar con procesos del sistema.
# Realiza un programa en Python que cambie la MAC de la interfaz de red, preguntando la nueva
# MAC (validando que sea un formato de MAC correcto) y que realice el cambio utilizando el
# comando ifconfig y el comando ip (preguntando con cual de los dos se quiere realizar).

# demasiado complicado , he usado macchanger para facilitarlo

import subprocess


def cambiarMac():
    comando = ["sudo", "ifconfig", "enp4s0", "down"]
    subprocess.run(comando)

    comando = ["sudo", "macchanger", "enp4s0", "-r"]
    subprocess.run(comando)

    comando = ["sudo", "ifconfig", "enp4s0", "up"]
    subprocess.run(comando)


if __name__ == "__main__":
    cambiarMac()
