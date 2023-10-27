def buscar(frase):
    xe = frase.find('.')
    y = frase.find('')
    res = frase[xe - 1: len(frase)]
    res2 = round(float(res), 2)
    return res2



def eliminar(frase):
    a = frase.replace('X-', '')
    return a

def eliminar2(frase):
    xe = frase.find('X-')
    res = frase[xe+2: len(frase)]
    print(res)

    return res




if __name__ == '__main__':
    fra = input("pon frase")
    print(eliminar2(fra))

    eliminar(fra)
    print(eliminar(fra))
    print(fra)


    x = buscar(fra)
    print(x)
