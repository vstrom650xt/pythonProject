nota_primera_evaluacion = float(input("Ingrese la nota de la primera evaluación: "))
nota_segunda_evaluacion = float(input("Ingrese la nota de la segunda evaluación: "))
nota_tercera_evaluacion = float(input("Ingrese la nota de la tercera evaluación: "))

# Definir los pesos de las evaluaciones
peso_primera_evaluacion = 0.30
peso_segunda_evaluacion = 0.40
peso_tercera_evaluacion = 0.30

# Calcular la nota media del curso
nota_media = (nota_primera_evaluacion * peso_primera_evaluacion +
              nota_segunda_evaluacion * peso_segunda_evaluacion +
              nota_tercera_evaluacion * peso_tercera_evaluacion)

# Mostrar el resultado
print(f"La nota media del curso es: {nota_media:.2f}")