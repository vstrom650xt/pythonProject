# 6. Importando la librería subprocess puedes lanzar e interactuar con procesos del sistema.
# Realiza un programa en Python que cambie la MAC de la interfaz de red, preguntando la nueva
# MAC (validando que sea un formato de MAC correcto) y que realice el cambio utilizando el
# comando ifconfig y el comando ip (preguntando con cual de los dos se quiere realizar).


import subprocess
import re


def elegirInterfaz():
    interfaces = subprocess.check_output(["ls", "/sys/class/net"]).decode('utf-8').split()
    print("Interfaces de red disponibles:")
    for i in interfaces:
        print(i)

    respuesta = input("pon nombre de la interfaz ").strip()

    if respuesta in interfaces:
        return respuesta
    else:
        print(" no existe.")
        return None



def cambiarMac(interface, new_mac):
    comando = ["sudo", "ifconfig", interface, "down"]
    subprocess.run(comando)

    comando = ["sudo", "ifconfig", interface, "hw", "ether", new_mac]
    subprocess.run(comando)

    comando = ["sudo", "ifconfig", interface, "up"]
    subprocess.run(comando)


def comprobarText():
    texto = subprocess.check_output(["ifconfig"]).decode('utf-8')
    macactual = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", texto)
    print("tu mac actual es")
    print(macactual.group(0))
    return  macactual


if __name__ == "__main__":

    comprobarText()
    interface = elegirInterfaz()
    if interface:
        nuevaMac = input("pon nueva mac ").strip()

        while len(nuevaMac) == 17 and nuevaMac.count(":") == 5:
            cambiarMac(interface, nuevaMac)
            nuevaMac = input("pon nueva mac ").strip()

        print(" mac  cambiado ")
