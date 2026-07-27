# Convertidor de temperatura

# Entrada: temperatura en Celsius
celsius = float(input("Temperatura en °C: "))
print("1. Fahrenheit\n2. Kelvin")
opcion = int(input("Elige opción: "))  # Elegir conversion

# Proceso: usar match-case
match opcion:
    case 1:
        resultado = celsius * 9/5 + 32  
        unidad = "°F"
    case 2:
        resultado = celsius + 273.15  
        unidad = "K"
    case _:
        resultado = None  
        unidad = ""

# Salida: muestra conversion
if resultado is not None:
    print(f"Resultado: {resultado:.2f} {unidad}")
else:
    print("Opción no válida")