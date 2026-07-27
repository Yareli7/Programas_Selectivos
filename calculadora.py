#Calculadora Básica
while True:
    print("1.Suma 2.Resta 3.Multiplicación 4.División 5.Salir")
    op = int(input("Opción: "))
    if op == 5:
        break
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    match op:
        case 1: print(a + b)
        case 2: print(a - b)
        case 3: print(a * b)
        case 4:
            if b != 0:
                print(a / b)
            else:
                print("Error: división por cero") # evita dividir entre 0
    resp = input("¿Desea continuar? (s/n): ").lower() # pasa a minuscula
    if resp == 'n':
        break