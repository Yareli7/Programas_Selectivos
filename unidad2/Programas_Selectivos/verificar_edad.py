# Verificar edad para votar

# Entrada: Solicita la edad al usuario
edad = int(input("¿Cuál es tu edad? "))

# Proceso: Valida si es mayor o igual a 18
if edad >= 18:
    # Salida: Si cumple
    print("Si puede votar")
else:
    # Salida: Si no cumple
    print("No puede votar")