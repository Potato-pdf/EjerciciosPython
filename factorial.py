def factorial(n):
    if n <= 1 :
        return 1 
    if n > 1:
        for n in range (1,n+1):
            factorial = numero* n
        return factorial
    
numero = int(input("ingrese un numero: "))
resultado = factorial(numero)
print (f"el factorial es:  {resultado}")

    