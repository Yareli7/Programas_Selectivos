# contar pares e impares
def contar_pares_impares(numeros): # define función para contar
    pares = 0 
    impares = 0 
    for num in numeros: 
        if num % 2 == 0: 
            pares += 1 # suma a pares
        else:
            impares += 1 # suma a impares
    return pares, impares

numeros = [] 
for i in range(10): # pide 10 números
    num = int(input("Número {}: ".format(i+1))) # lee número
    numeros.append(num) # guarda en lista

p, i = contar_pares_impares(numeros) 
print("Pares:", p)
print("Impares:", i)