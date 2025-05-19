import copy

listas = [] #Una lista es una estructura de datos que permite almacenar una coleccion de elementos en un orden especifico, y que puede ser modificada.
#Las listas en python son mutables, es decir, se pueden modificar, son iterables, es decir, se pueden recorrer, son dinamicas, es decir, se pueden agregar, eliminar, modificar elementos.
#Las listas en python son una estructura de datos que permite almacenar una coleccion de elementos en un orden especifico, y que puede ser modificada
listas.append(1) #Agrega un elemento al final de la lista
listas.extend([2,3,4]) #Agrega una lista al final de la lista
listas.insert(0,5) #Agrega un elemento en una posicion especifica
listas.remove(4) #Remueve un elemento de la lista
listas.pop(0) #Remueve un elemento de una posicion especifica
listas.clear() #Remueve todos los elementos de la lista
listas.index(3) #Devuelve la posicion de un elemento en la lista
listas.index(3,0,3) #Devuelve la posicion de un elemento en una posicion especifica, primer parametro es el elemento, segundo parametro es la posicion inicial, tercer parametro es la posicion final
listas.count(3) #Devuelve la cantidad de veces que aparece un elemento en la lista
listas.sort() #Ordena la lista
copia_lista = listas.copy() #Copia la lista
copia_profunda_lista = copy.deepcopy(listas) #Copia la lista de forma profunda
print(listas)
print(elemento_eliminado)
del listas #Elimina la lista completa


tuplas = () #Una tupla es una estructura de datos que permite almacenar una coleccion de elementos en un orden especifico, y que no puede ser modificada.
#Las tuplas en python son inmutables, es decir, no se pueden modificar, son iterables, es decir, se pueden recorrer, son dinamicas, es decir, se pueden agregar, eliminar, modificar elementos.
