# Solicitar información al usuario sobre las notas de las evaluaciones
nota_primera_evaluacion = input("¿Ha suspendido la primera evaluación? (S/N): ").upper()
nota_segunda_evaluacion = input("¿Ha suspendido la segunda evaluación? (S/N): ").upper()
nota_tercera_evaluacion = input("¿Ha suspendido la tercera evaluación? (S/N): ").upper()

# Determinar si el alumno puede aprobar el curso en convocatoria ordinaria
if nota_primera_evaluacion == "S" and nota_segunda_evaluacion == "S" and nota_tercera_evaluacion == "S":
    print("El alumno ha suspendido todas las evaluaciones y no puede aprobar el curso en convocatoria ordinaria.")
elif nota_primera_evaluacion == "N" or nota_segunda_evaluacion == "N" or nota_tercera_evaluacion == "N":
    print("El alumno ha aprobado al menos una de las evaluaciones y puede aprobar el curso en convocatoria ordinaria.")
else:
    print("El alumno ha suspendido todas las evaluaciones, pero puede aprobar el curso en convocatoria ordinaria debido a que se permite aprobar con la primera evaluación suspendida.")
