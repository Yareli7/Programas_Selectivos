# Convertidor de MXN a 10 monedas extranjeras

# Entrada
cantidad = float(input("Cantidad en MXN: "))
print("1.USD 2.EUR 3.THB 4.JPY 5.KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS")
opcion = int(input("Elige opción: "))

# Proceso con match
match opcion:
    case 1:
        resultado = cantidad / 17.0  # USD
        moneda = "USD"
    case 2:
        resultado = cantidad / 18.5  # EUR
        moneda = "EUR"
    case 3:
        resultado = cantidad / 0.45  # THB
        moneda = "THB"
    case 4:
        resultado = cantidad / 0.12  # JPY
        moneda = "JPY"
    case 5:
        resultado = cantidad / 0.013  # KRW
        moneda = "KRW"
    case 6:
        resultado = cantidad / 11.5  # AUD
        moneda = "AUD"
    case 7:
        resultado = cantidad / 2.8  # PEN
        moneda = "PEN"
    case 8:
        resultado = cantidad / 8.2  # CAD
        moneda = "CAD"
    case 9:
        resultado = cantidad / 0.0023  # VES
        moneda = "VES"
    case 10:
        resultado = cantidad / 0.046  # ARS
        moneda = "ARS"
    case _:
        print("Opción no válida")  # Opcion incorrecta
        resultado = None
        moneda = ""

# Salida
if resultado is not None:
    print(f"{cantidad} MXN = {resultado:.2f} {moneda}")
