
#218
numeros = [1,2,3]
print(numeros)
print(*numeros) # * comandao para depaquetar para listas
print(*numeros, sep=" - ") # depaquetamos y agregamos un separador

# para diccionarios ** doble asteriscos

#219
def suma(a,b,c):
    return print(f" Suma : {a + b + c}")

suma(*numeros)

 
#220
# Extraer algunas partes de una lista
milista = [1,2,3,4,5]
a,*b,c,d = milista
print(a,b,c,d)

#221

# Unir listas 
lista1 = [1,2]
lista2= [4,3]
lista3= [lista1, lista2]
print(f"Lista de lista : {lista3}")
lista3 = [*lista1,*lista2]
print(f"Unir listas : {lista3}")

# Unir Diccionarios
dic1 = {"A": 2,"B" : 3,"C": 7}
dic2 = {"D": 8,"E" : 4}
dic3 = {**dic1,**dic2}
print(dic3)


# Lista apartir de un String 
lista = [*"Hola mundo"]
print(lista)
