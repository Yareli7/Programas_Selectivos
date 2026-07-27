# Estaciones del año según el mes

# Entrada: numero de mes 1-12
mes = int(input("Número de mes (1-12): "))

# Proceso: match con las estaciones
match mes:
    case 12 | 1 | 2:
        estacion = "Invierno"  # Dic, Ene, Feb
    case 3 | 4 | 5:
        estacion = "Primavera"  # Mar, Abr, May
    case 6 | 7 | 8:
        estacion = "Verano"  # Jun, Jul, Ago
    case 9 | 10 | 11:
        estacion = "Otoño"  # Sep, Oct, Nov
    case _:
        estacion = "Mes no válido"  # Si pone 13 etc

# Salida: muestra la estacion
print(f"Estación: {estacion}")