
# DESPAQUETANDO EN PYTHON
# 209

valores = 1,2,3

print(valores)
print(type(valores))

valor1,valor2,valor3 = 1,2,3 # Se asigna a las variables dependiendo la posicion

print(valores) 

valor1, _, valor3 = 1,2,3 # forma de no asignar un valor

print(valor1,valor3)

valor1, valor2, *valor3 = 1,2,3,4,5,6,7,8,9 # con el * hacemos que los valores restantes esten todos, sino se se ejecuta 

print(valor1,valor2,valor3)

valor1, valor2, *valor3, valor4, valor5 = 1,2,3,4,5,6,7,8,9 # Se le asigna los ultimos valores

print(valor1,valor2,valor3,valor4,valor5)

#210

# En LISTAS

valor1, valor2, *valor3, valor4, valor5 = [1,2,3,4,5,6,7,8,9]

print(valor1,valor2,valor3,valor4,valor5)
print(type(valor3))

def variables():
    return 1,2,3

valor5, *valor_restantes = variables()

print(valor5, *valor_restantes)


#211

#help(str.partition)

hora, separador,minutos = "17:20".partition(":") # con partition separamos y lo asignamos a las variables

print(f"Hora : {hora} Minutos : {minutos}")



