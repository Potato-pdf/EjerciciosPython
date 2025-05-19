def invertir_cadena(cadena):
    if len(cadena) == 0:
        return cadena
    else:
        return invertir_cadena(cadena[1:]) + cadena[0]
    
cadena_original = "Hola, mundo!"
cadena_invertida = invertir_cadena(cadena_original)
print(cadena_invertida)