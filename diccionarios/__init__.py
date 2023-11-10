# Dado el fichero “el_quijote.txt”, mostrar por
# pantalla todas las palabras distintas del mismo
# junto con su frecuencia de aparición

if __name__ == '__main__':
    archivo = '../el_quijote.txt'
    #diccio = {}
    contadores = dict()
    with open(archivo) as lector:
        contenido = lector.read()
        palabras = contenido.split()
        for palabra in palabras:
            palabra.strip(',.;:')
            contadores[palabra] = contadores.get(palabra,0)+1
print('Contadores',contadores)

list p = contadores
p.sort()
print(p)