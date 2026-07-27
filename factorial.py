#Factorial
num = int(input("Número para factorial: ")) 
factorial = 1 # empieza en 1
if num < 0: 
    print("Factorial no definido para negativos")
else: # si es positivo o 0
    for i in range(1, num + 1): 
        factorial *= i # multiplica
    print("El factorial de", num, "es:", factorial) # resultado