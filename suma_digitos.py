def suma_digitos(numero):
    suma = 0 
    for digito in numero :
        suma += int(digito)
    return suma
numero = int(input("ingrese un numero: "))
resultado = suma_digitos(numero)
print(f"la suma de los digitos es: {resultado}")