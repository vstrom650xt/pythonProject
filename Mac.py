import requests

def obtener_fabricante_oui(direccion_mac):
    # Formatea la dirección MAC eliminando caracteres especiales
    direccion_mac = direccion_mac.replace(':', '').replace('-', '').upper()

    # Consulta la base de datos de OUI en línea
    url = f"https://www.macvendors.com/query/{direccion_mac}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.text.strip()
    else:
        return "No se pudo obtener información del fabricante"

# Ejemplo de uso
direccion_mac = "00:1A:2B:3C:4D:5E"
fabricante = obtener_fabricante_oui(direccion_mac)
print(f"La dirección MAC {direccion_mac} pertenece a: {fabricante}")