#Multiplos de 3 y 5
print("Números divisibles por 3 y 5 (1-100):") # mensaje del inicio
for i in range(1, 101): 
    if i % 3 == 0 and i % 5 == 0: 
        print(i, end=" ") 
print() # salto de linea final 