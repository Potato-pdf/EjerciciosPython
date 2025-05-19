def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    contador = 0
    for caracter in texto:
        if caracter in vocales:
            contador += 1
    return contador

texto= input ("ingrese un texto: ")
print(f"El numero de vocales es: {contar_vocales(texto)}")