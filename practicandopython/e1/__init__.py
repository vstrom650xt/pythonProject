def IMC(weight, height):
    return weight * height / 2


if __name__ == '__main__':
    try:
        weight = input("put your weight")
        height = input("put your height")

        weight = float(weight)
        height = float(height)

        print(IMC(weight, height))

        if 25 > IMC(weight, height) > 20:
            print("you are great")
        else:
            print("you should train your self")

    except ValueError:
        print('error en el input')
