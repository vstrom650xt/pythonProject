
archivo = 'hola.txt'
def leerTexto():
    global cont
    with open(archivo, 'r') as f:
        cont = f.read()



def escribirTexto():
    nombre_archivo = "hola.txt"

    # Abre el archivo en modo de escritura ("w" para escribir, "a" para agregar)
    # Si el archivo no existe, se creará
    with open(nombre_archivo, "w") as archivo:
        # Escribe en el archivo
        archivo.write("Hola, este es un ejemplo de escritura en un archivo en Python.\n")
        archivo.write("Aquí puedes agregar más líneas si deseasadsadsadasddsaass.\n")
    print("Se ha escrito en el archivo exitosamente.")


if __name__ == '__main__':
   leerTexto()
   escribirTexto()
   leerTexto()

