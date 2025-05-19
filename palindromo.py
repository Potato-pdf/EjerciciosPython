def palindromo (palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")
    if palabra == palabra [::-1]:
        return True
    else:
        return False
palabra = input("ingrese una palabra: ")
if palindromo(palabra):
    print("es un palindromo")
else:
    print("no es un palindromo")