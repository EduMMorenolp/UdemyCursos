

#251

# Expresion generador 

Multiplicacion = ( valor*valor for valor in range(4))
print(type(Multiplicacion))
print(f"Valor {next(Multiplicacion)}")
print(f"Valor {next(Multiplicacion)}")
print(f"Valor {next(Multiplicacion)}")
print(f"Valor {next(Multiplicacion)}")

# Expresion generadora en un funcion
import math

suma = sum(valor*valor for valor in range(4))
print(f"resultado suma : {suma}")

#252

# Expresiones generadoras

# También podemos usar una lista o cualquier otro iterador
lista = ['Juan','Perez']
generador = (valor for valor in lista)
print(next(generador))
print(next(generador))

# Crear un string a partir de un generador creado a partir de una lista
lista = ['Karla','Gomez', 22]
contador = 0
# Definimos una función para incrementar el contador
def incremetar():
    global contador
    contador += 1
    return contador
# La primera para es el yield, la segunda es el for, entre paréntesis
generador = (f'{incremetar()}. {nombre}' for nombre in lista)
lista = list(generador)
print(lista)
cadena = ', '.join(lista)
print(f'Cadena generada: {cadena}')