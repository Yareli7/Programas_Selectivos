#Adivinar numero
import random
secreto = random.randint(1, 100) # numero secreto
while True:
    intento = int(input("Adivina (1-100): "))
    if intento < secreto:
        print("Demasiado bajo")
    elif intento > secreto:
        print("Demasiado alto")
    else:
        print("¡Correcto! Era", secreto)
        break
print("Juego terminado. El número era", secreto)