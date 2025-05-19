def numeros_primos (n):
     if n < 2 :
         return False 
     for i in range(2, n):
         if n % i == 0:
             return False
         return True 
     
n = int(input("ingrese un numero: "))
if numeros_primos(n):
    print(f"{n} es un numero primo")
else:
    print(f"{n} no es un numero primo")