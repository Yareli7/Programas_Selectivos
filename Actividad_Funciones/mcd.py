import math

# funcion MCD con Euclides
def mcd(a, b):
    a = abs(a) # convierte a positivo
    b = abs(b)
    if a == 0 and b == 0:
        return 0 # caso especial
    while b != 0:
        a, b = b, a % b # algoritmo de Euclides
    return a

num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))

resultado = mcd(num1, num2)
resultado_math = math.gcd(num1, num2)

print(f"MCD calculado: {resultado}")
print(f"MCD con math.gcd: {resultado_math}")
print(f"Los resultados {'coinciden' if resultado == resultado_math else 'No coinciden'}")

if num1 == 0 and num2 == 0:
    print("Caso especial: ambos números son cero")
else:
    print("Programa terminado")