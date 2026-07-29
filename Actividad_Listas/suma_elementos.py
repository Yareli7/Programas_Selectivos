# suma de elementos
def sumar_lista(lista): # suma manual con bucle
    suma = 0
    for num in lista:
        suma += num
    return suma

numeros = []
for i in range(5):
    valor = int(input(f"Ingrese número {i+1}: "))
    numeros.append(valor)

total = sumar_lista(numeros)
total_sum = sum(numeros) # suma con función built-in

print("Suma con bucle:", total)
print("Suma con sum():", total_sum)