if __name__ == '__main__':
    archivo = '../el_quijote.txt'
    contadores = dict()

    with open(archivo, encoding='utf-8') as lector:
        contenido = lector.read()
        palabras = contenido.split()

        for palabra in palabras:
            palabra = palabra.strip(',.;:')
            palabra = palabra.lower()
            contadores[palabra] = contadores.get(palabra, 0) + 1

    pmf = max(contadores, key=contadores.get)
    fmf = contadores[pmf]

    print('Palabra más frecuente:', pmf)
    print('Frecuencia:', fmf)
