def div(a,b):
    return a % b

if __name__ == '__main__':

    try:
        numero1 = input("pon numero1")
        numero2 = input("pon numero2")

        numero1 = int(numero1)
        numero2 = int(numero2)

        if div(numero1,numero2)  == 0:
            print("its was an exact division")
        else:
            print("it wanst an exact division")












    except ValueError:
        print("input error")