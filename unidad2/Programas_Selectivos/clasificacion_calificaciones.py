# Clasificación de Calificaciones
# Evalúa una calificación numérica y asigna una letra A, B, C, D, F

# Entrada: Solicita la calificación (0-100)
nota = float(input("Ingrese calificación (0-100): "))

# Proceso: Evaluación por rangos usando if-elif-else
if nota >= 90:
    letra = "A"  
elif nota >= 80:
    letra = "B"  
elif nota >= 70:
    letra = "C"  
elif nota >= 60:
    letra = "D"  
else:
    letra = "F"  

# Salida: Muestra la letra correspondiente
print(f"Calificación: {letra}")