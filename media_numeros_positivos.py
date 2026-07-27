#Media de numeros positivos
suma = 0 
contador = 0 
while True: 
    num = float(input("Número positivo (negativo sale): ")) # pide numero
    if num < 0: 
        break 
    if num > 0: 
        suma += num 
        contador += 1 
if contador > 0: 
    media = suma / contador # calcula media
    print("Media:", media) # muestra media
else: 
    print("No se ingresaron positivos")