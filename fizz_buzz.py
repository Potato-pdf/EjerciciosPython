def fiss_buzz(numero):
    if numero % 3 == 0 and numero % 5 == 0 :
        return "fizz_buzz"
    if numero % 3 == 0:
        return "fizz"
    if numero % 5 == 0 :
        return "buzz"
    else :
        return numero
    
numero = int(input("ingrese un numero: "))
resultado = fiss_buzz(numero)
print (f"el numero es:  {resultado}")