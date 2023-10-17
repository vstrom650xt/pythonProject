def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def mult(a,b):
    return a*b

def menu():



    try:
        numero1 = input("pon numero1")
        numero2 = input("pon numero2")

        numero1 = int(numero1)
        numero2 = int(numero2)
        print('1 suma  2 resta 3 multi')
        num = input("pon un numero ")
        num = int(num)
        
        if num == 1:
            print(suma(numero1 , numero2))
        elif num == 2:
            if numero1> numero2:
                print(resta(numero1, numero2))
            else:
                print(resta(numero2, numero1))
        else:
            print(mult(numero1,numero2))

    except ValueError:
        print('error en el input')







if __name__ == '__main__':
    menu()