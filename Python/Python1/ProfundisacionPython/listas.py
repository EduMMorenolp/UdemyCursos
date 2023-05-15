


# PROFUNDISANDO EN LISTAS

# Las Listas son mutables (se puede modificar a gusto en cualquier momento)
#212

# formas de armas listas
nombres1 = ["Carla","Juan","Pablo"] 
print(f"Lista 1 : {nombres1}")
print(type(nombres1))

nombres2 = "Pedro Carlos Rodrigo".split() # el metodo split Hace una lista despues de cada espacio

print(f"Lista 2 : {nombres2}")
print(type(nombres2)) 

# sumar listas

print(f" Suma de listas : {nombres1 + nombres2}")

# extender una lista sobre otra

nombres1.extend(nombres2) # se agrega a la primer variable las variables del segundo con extend
print(f"Listas Extendida : {nombres1}")


# listas de numeros
#213

Numeros = [1,2,3,32,5,6]

# obtener el indice(ubicacion) de una valor de la lista 
print(f" Lista Original : {Numeros}")
print(f"Index Numero 32 en la lista : {Numeros.index(32)}")

# Invertir el orden de una lista

Numeros.reverse()

print(f"Lista invertida : {Numeros}") 

# ordenar los elementos de una lista 

# ACENDENTE 

Numeros.sort() # la funcion sort naturalmente ordena de menor a mayor
print(f"Lista ordena acendente : {Numeros}")

# DECENDENTE 

Numeros.sort(reverse=True) # con reverse ordenamos de forma invertida
print(f"Lista ordena decendente : {Numeros}")

#214
# Obetener valores min y max

print(f" Valor minimo {min(Numeros)}")
print(f" Valor maximo {max(Numeros)}")

# Copiar elementos de una lista

Numeros2 = Numeros.copy()

print(f" Lista copiada : {Numeros2}")

print(f"Misma referencia ? : {Numeros is Numeros2}")
print(f"Mismo contenido ? : {Numeros == Numeros2}")

# Constructor de la lista

Numeros2 = list(Numeros)
print(f"Misma referencia Contructor? : {Numeros is Numeros2}")
print(f"Mismo contenido Constructor? : {Numeros == Numeros2}")

# slicing 

Numeros2 = Numeros[:]
print(f"Misma referencia slicing? : {Numeros is Numeros2}")
print(f"Mismo contenido slicing? : {Numeros == Numeros2}")


#215

# LISTAS DE LISTAS
# Multiplicacion de listas 

lista_multiplicada = 5*[[2,3]]
print(lista_multiplicada)
print(f"Misma referencia ? : {lista_multiplicada[0] is lista_multiplicada[1]}")
print(f"Mismo contenido ? : {lista_multiplicada[0] == lista_multiplicada[1]}")
lista_multiplicada[1].append(12) # cuando se agrega un nuevo elemento se modifica en todos
print(lista_multiplicada)

#216

# Matrices en python

matriz = [[2,3],[8,6,3],[3,]]

print(f" Matriz Original : {matriz}")
print(f" Fila 0 y Columna 1 : {matriz[0][1]}")
print(f" Fila 1 y Columna 1 : {matriz[1][1]}")
matriz[1][1] = 80
print(f" Matriz modificada : {matriz}")
print(f" Fila 1 y Columna 1 Modificada : {matriz[1][1]}")

#217

lista_lista = [[2,31,8],[12,6,3,0],[9,]]
print(f" Matriz Original : {lista_lista}")
lista_lista.sort(key=len) # ordenamos la lista por cantidad de elementos
print(f" Matriz Ordenada : {lista_lista}")

# sorted built-in FUNCIONES integradas de python para ordenamiento
# sorted ( iterable , key=llave , reverse=FALSE invertido)

nombres1 = [ "Xavier","JuanPablo","Carlos","Maria"]
print(f"Original : {nombres1}")
nombres1 = sorted(nombres1) # ORDENADA ACENCEDENTE A a Z
print(f"Ordenada : {nombres1}")
nombres1 = sorted(nombres1, reverse=False) # con reverse se ordena DECENDETE
print(f"Ordenada decendente : {nombres1}")
nombres1 = sorted(nombres1,key=len) # ordenado por largo de caracteres
print(f"Ordenada por largo : {nombres1}")
# built-in reversed
nombres1 = reversed(nombres1)
print(f"Ordenada Reverded metod : {list(nombres1)}")