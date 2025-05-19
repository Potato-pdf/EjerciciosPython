def par_impar(numero):
    if numero % 2  == 0 :
        return "par"
    else:
        return "impar"
    
numero = int(input("ingrese un numero: "))
resultado = par_impar(numero)
print (f"el numero es:  {resultado}")