#Secuencia de cuadrados
N = int(input("Número positivo: "))
i = 1
while True:
    print(i ** 2) # calcula cuadrado
    i += 1
    if i > N:
        break
print("Secuencia de cuadrados hasta", N)