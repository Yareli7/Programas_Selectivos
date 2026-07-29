#Contador de números impares
N = int(input("Número positivo: ")) 
i = 1 
while True: # para que se repita
    if i % 2 != 0: 
        print(i, end=" ") 
    i += 1 # para que avance
    if i > N: 
        break 
print("\nFin. Se mostraron los impares hasta", N) # fin