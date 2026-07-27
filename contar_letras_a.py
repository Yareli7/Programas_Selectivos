#Contar letras a
palabra = input("Ingrese una palabra: ").lower() # convierte a minuscula
contador = 0
for letra in palabra:
    if letra == 'a':
        contador += 1
print("La letra 'a' aparece", contador, "veces")