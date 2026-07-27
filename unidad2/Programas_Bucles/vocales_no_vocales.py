#Vocales / No vocales
while True: 
    letra = input("Ingrese letra (espacio termina): ") 
    if letra == " ": 
        break # con espacio termina 
    letra = letra.lower() # pasa a minuscula
    if letra in "aeiou": 
        print("Vocal") 
    else: # si no es vocal
        print("Consonante") 
print("Programa finalizado") # mensaje final