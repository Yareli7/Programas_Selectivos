# Calculadora de nota final con validacion de rango

# Entrada de datos - Se solicitan las tres calificaciones
parcial = float(input("Nota parciales (0-100): "))
proyecto = float(input("Nota proyecto (0-100): "))
examen = float(input("Nota examen final (0-100): "))

# Validacion de rango
if (parcial < 0 or parcial > 100) or (proyecto < 0 or proyecto > 100) or (examen < 0 or examen > 100):
    print("Error: las notas deben estar entre 0 y 100")
else:
    nota_final = (parcial * 0.4) + (proyecto * 0.3) + (examen * 0.3)
    print("Nota final:", nota_final)
