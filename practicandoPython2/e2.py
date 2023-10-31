#4. Crea un programa en Python que pida una fecha formada por tres valores numéricos (día, mes y año), y determine si la fecha corresponde a un valor válido.
#Pista: se debe tener presente el valor de los días en función de los meses y de los años. Es decir:
#- Los meses 1, 3, 5, 7, 8, 10 y 12 tienen 31 días.
#- Los meses 4, 6, 9 y 11 tienen 30 días.
#- El mes 2 tiene 28 días, excepto cuando el año es divisible por 4, que tiene 29 días. (¡pero no cuando es divisible por 100, a menos que sea divisible también por 400!)
#Pista: para saber si un número es divisible por 4, pregunta si el resto de dividirlo por 4 es cero.
def es_bisiesto(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def validar_fecha(dia, mes, anio):
    if mes < 1 or mes > 12:
        return False

    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return dia > 0 and dia <= 31
    elif mes in [4, 6, 9, 11]:
        return dia > 0 and dia <= 30
    elif mes == 2:
        if es_bisiesto(anio):
            return dia > 0 and dia <= 29
        return dia > 0 and dia <= 28

    return False

if __name__ == '__main__':
    dia = int(input("Ingresa el dia "))
    mes = int(input("Ingresa el mes "))
    anio = int(input("Ingresa el año "))

    if validar_fecha(dia, mes, anio):
        print("La fecha ingresada es valida.")
    else:
        print("La fecha ingresada no es valida.")