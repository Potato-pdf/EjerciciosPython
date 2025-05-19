def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

texto = input("ingrese un texto: ")
resultado = contar_palabras(texto)
print(f"el numero de palabras es: {resultado}")