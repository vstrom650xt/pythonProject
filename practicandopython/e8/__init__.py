# Solicitar la edad del gato al usuario
edad_gato = int(input("Ingrese la edad de su gato: "))

# Calcular el equivalente humano de la edad del gato
if edad_gato == 1:
    edad_humana = 15
elif edad_gato == 2:
    edad_humana = 15 + 10
else:
    edad_humana = 15 + 10 + (edad_gato - 2) * 4

# Mostrar el resultado
print(f"La edad de su gato equivale a aproximadamente {edad_humana} años en humanos.")
