if __name__ == '__main__':
    archivo = '../el_quijote.txt'
    cont = dict()

    with open(archivo, encoding='utf-8') as lector:
        contenido = lector.read()
        palabras = contenido.split()

        for palabra in palabras:
            palabra = palabra.strip(',.;:')
            palabra = palabra.lower()
            cont[palabra] = cont.get(palabra, 0) + 1

    fm = min(cont.values())

    pmf = [palabra for palabra, frecuencia in cont.items() if frecuencia == fm]

    print('Frecuencia mínima', fm)
    print('Palabras con frecuencia mínima', pmf)
