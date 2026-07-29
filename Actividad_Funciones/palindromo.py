# verifica si es palindromo ignorando espacios
def es_palindromo(texto):
    texto = texto.lower()
    limpio = ""
    for caracter in texto:
        if caracter != " ":
            limpio += caracter
    return limpio == limpio[::-1], limpio # compara con reverso

entrada = input("Ingrese una frase: ")
resultado, cadena_limpia = es_palindromo(entrada)

if resultado:
    print("Es un palindromo")
else:
    print("No es palindromo")
print("Longitud de la cadena limpia:", len(cadena_limpia))