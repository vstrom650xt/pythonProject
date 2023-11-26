





if __name__ == "__main__" :
    cont = 0
    fichero = open("hola.txt","r+")
    fichero.write("\n otralinea")

    for i in fichero :
       cont= cont+1
       print(i)


    print (cont)