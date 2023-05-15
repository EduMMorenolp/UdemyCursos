

#256

# Palabras reservadas en Python (keywords)
import keyword

print('Palabras reservadas (keywords) en Python')
#print(keyword.kwlist)
lista_keywords = keyword.kwlist
for keywords in lista_keywords:
    print(keywords)

# Variable (no podemos utilizar keyword para el nombre de una variable)
# as = 'Hola'
# Función (no podemos utilizar keyword para el nombre de una función)
# def is():
#     pass