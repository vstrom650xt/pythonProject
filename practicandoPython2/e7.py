#7. Importando la librería re puedes encontrar patrones,
# extraer o sustituir información e incluso validar formatos.
# Mejora el programa anterior añadiendo una pregunta previa al usuario,
# dándole a elegir de que interfaz de red quiere cambiar la MAC y, según
# elija, muestres la MAC actual, le pregunte por la nueva y la cambie.
# Deberás localizar tanto el nombre de la interfaz de red como la MAC
# mediante expresiones regulares (puedes probarlas en la siguiente web:
# https://pythex.org/)
#PISTA: re.search(r"EXPRESIONREGULAR", texto)
import subprocess
import re

def obtener_interfaces_red():
    # Ejecutamos el comando "ifconfig" para obtener información de las interfaces de red
    resultado_ifconfig = subprocess.check_output(["ifconfig"]).decode("utf-8")
    # Utilizamos una expresión regular para encontrar los nombres de las interfaces de red
    interfaces = re.findall(r'^\w+', resultado_ifconfig, re.MULTILINE)
    return interfaces

def obtener_mac_actual(interfaz):
    # Ejecutamos el comando "ifconfig [interfaz]" para obtener la información de la interfaz
    resultado_ifconfig = subprocess.check_output(["ifconfig", interfaz]).decode("utf-8")
    # Utilizamos una expresión regular para encontrar la dirección MAC actual
    mac_actual = re.search(r'ether ([0-9A-Fa-f:]+)', resultado_ifconfig)
    if mac_actual:
        return mac_actual.group(1)
    else:
        return None

def validar_mac(mac):
    # Utilizamos una expresión regular para validar el formato de la dirección MAC
    mac_pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    return re.match(mac_pattern, mac)

def cambiar_mac(interfaz, nueva_mac):
    # Ejecutamos los comandos para cambiar la dirección MAC
    comando_down = ["ifconfig", interfaz, "down"]
    subprocess.run(comando_down)

    comando_set_mac = ["ifconfig", interfaz, "hw", "ether", nueva_mac]
    subprocess.run(comando_set_mac)

    comando_up = ["ifconfig", interfaz, "up"]
    subprocess.run(comando_up)

if __name__ == "__main":
    interfaces = obtener_interfaces_red()

    print("Interfaces de red disponibles:")
    for i, interfaz in enumerate(interfaces):
        print(f"{i + 1}. {interfaz}")

    seleccion = int(input("Seleccione el número de la interfaz de red para cambiar la MAC: ")) - 1

    if 0 <= seleccion < len(interfaces):
        interfaz_seleccionada = interfaces[seleccion]
        mac_actual = obtener_mac_actual(interfaz_seleccionada)

        if mac_actual:
            print(f"MAC actual de la interfaz {interfaz_seleccionada}: {mac_actual}")
            nueva_mac = input("Ingrese la nueva dirección MAC (formato XX:XX:XX:XX:XX:XX): ")

            if validar_mac(nueva_mac):
                cambiar_mac(interfaz_seleccionada, nueva_mac)
                print(f"La dirección MAC de la interfaz {interfaz_seleccionada} se ha cambiado a {nueva_mac}.")
            else:
                print("La dirección MAC ingresada no tiene un formato válido.")
        else:
            print(f"No se pudo obtener la MAC actual de la interfaz {interfaz_seleccionada}.")
    else:
        print("Selección no válida.")
