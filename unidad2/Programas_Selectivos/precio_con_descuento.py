# Calcular precio con descuento

# Entrada: precio original
precio = float(input("Precio original: "))

# Proceso: porcentaje de descuento
if precio <= 100:
    descuento = 0  # Sin descuento
elif precio <= 200:
    descuento = 0.10  # 10% de descuento
elif precio <= 500:
    descuento = 0.20  # 20% de descuento
else:
    descuento = 0.25  # 25% de descuento

# Calculo del precio final
precio_final = precio - (precio * descuento)

# Salida: precio con descuento
print("Precio con descuento:", precio_final)