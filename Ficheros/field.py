
archivo = 'hola.txt'
def leerTexto():
    global cont
    with open(archivo, 'r') as f:
        cont = f.read()



def escribirTexto():
    nombre_archivo = "hola.txt"

    with open(nombre_archivo, "w") as archivo:
        archivo.write("Hola, este es un ejemplo de escritura en un archivo en Python.\n")
        archivo.write("Aquí puedes agregar más líneas si deseasadsadsadasddsaass.\n")
    print("Se ha escrito en el archivo exitosamente.")


if __name__ == '__main__':
   leerTexto()
   escribirTexto()
   leerTexto()

