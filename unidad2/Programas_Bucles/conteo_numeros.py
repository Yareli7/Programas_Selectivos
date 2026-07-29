#Conteo de números
n = int(input("Cantidad de números a ingresar: "))
mayores = 0
menores = 0
iguales = 0 # para contar los ceros
for i in range(n): # se repite n veces
    num = int(input("Número: "))
    if num > 0:
        mayores += 1
    elif num < 0:
        menores += 1
    else:
        iguales += 1

print(f"Mayores que 0: {mayores}")
print(f"Menores que 0: {menores}")
print(f"Iguales a 0: {iguales}")