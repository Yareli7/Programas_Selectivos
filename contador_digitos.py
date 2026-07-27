#Contador de digitos
num = int(input("Número entero: ")) 
if num == 0: 
    digitos = 1 # el 0 tiene 1 digito
else: 
    digitos = 0 
    if num < 0: 
        num = abs(num) # lo hacemos positivo para poder contarlo
    while num > 0: 
        num //= 10 
        digitos += 1 
print("El número tiene", digitos, "dígitos") # resultado final