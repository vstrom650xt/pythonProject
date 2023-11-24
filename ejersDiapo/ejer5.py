

if __name__ =='__main__':
    res=0
    cont =0
    while True:
        try:
            a = input('pon nums')
            if a == 'fin':
                break
            res = res+ int(a)
            cont= cont+1
            print(res)
        except:
            print('error')

    salida= res / cont
    print(salida)