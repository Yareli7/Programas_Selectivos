#Secuencia aritmetica
inicio = int(input("Primer número: "))
diferencia = int(input("Diferencia: ")) 
limite = int(input("Límite máximo: ")) 
num = inicio 
while True: # ciclo infinito tipo do-while
    print(num, end=" ") 
    num += diferencia # suma la diferencia
    if num > limite: 
        break 
print("\nSecuencia aritmética desde", inicio, "hasta", limite) 