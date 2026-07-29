def reemplazar_manual(texto, viejo, nuevo):
    if len(viejo) != 1 or len(nuevo) != 1:
        return texto, 0
    resultado = ""
    contador = 0
    for letra in texto:
        if letra == viejo:
            resultado += nuevo
            contador += 1 # cuenta reemplazos
        else:
            resultado += letra
    return resultado, contador

texto = input("Cadena: ")
car_viejo = input("Caractér a reemplazar: ")
car_nuevo = input("Caractér nuevo: ")

if len(car_viejo) != 1 or len(car_nuevo) != 1:
    print("Debe ingresar un solo carácter")
else:
    res_manual, total = reemplazar_manual(texto, car_viejo, car_nuevo)
    print(f"Resultado manual: {res_manual}")
    print(f"Numero de reemplazos: {total}")
    print(f"Resultado con replace(): {texto.replace(car_viejo, car_nuevo)}")