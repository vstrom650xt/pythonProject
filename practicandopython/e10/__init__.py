smi = 13300  # en euros

precio_vivienda = float(input("Ingrese el precio de la vivienda en euros: "))
zona = input("Ingrese la zona de la vivienda (A, B, C, D, E): ")
sueldo_anual = float(input("Ingrese el sueldo anual del comprador en euros: "))
edad_comprador = int(input("Ingrese la edad del comprador: "))

factores_zona = {
    'A': 0.85,
    'B': 0.9,
    'C': 0.92,
    'D': 0.97,
    'E': 1.0
}

factor_zona = factores_zona.get(zona, 1.0)  # Obtener el factor de corrección por zona
sueldo_corregido = sueldo_anual * factor_zona

proporcion_smi = sueldo_corregido / smi

if proporcion_smi < 1.5:
    ayuda = 0.15 * precio_vivienda
elif proporcion_smi < 2.5:
    ayuda = 0.10 * precio_vivienda
elif proporcion_smi < 3.5:
    ayuda = 0.08 * precio_vivienda
else:
    ayuda = 0.05 * precio_vivienda

if edad_comprador < 35:
    ayuda += 3000

print(f"La ayuda a la compra de la vivienda es de {ayuda} euros.")
