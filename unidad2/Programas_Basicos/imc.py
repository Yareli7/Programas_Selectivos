# Calcula el IMC de una persona
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
imc = peso / (altura ** 2)
print("Su IMC es:", imc)