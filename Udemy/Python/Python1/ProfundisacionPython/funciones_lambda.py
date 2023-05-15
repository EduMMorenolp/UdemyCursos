


#243

# Funciones Lambda
# son funciones anonimas, y son pequeños (una linea de codigo)

# No es un posible definir una funcion a una variable
# mi_variable = def sumar(a,b) return a+b

# No se nesecita agragar () para los parametros
# No se usa return

mi_funcion_lambda = lambda a,b : a + b

print(f"Funcion lambda suma : {mi_funcion_lambda(4,6)}")


#244

# La funcion lambda que no recive argunmentos, deve devolver una expresion valida 

mi_funcion_lambda = lambda: "Funcion lamba sin argumento"

print(mi_funcion_lambda())

# Funcion lambda con parametros por defoult

mi_funcion_lambda = lambda a=2, b=3 : a + b 

print(f"Funcion lambda con parametros por default : {mi_funcion_lambda()}")
print(f"Funcion lambda con parametros por default + pasarle valores : {mi_funcion_lambda(4,6)}") #opcional pasarle valores

# Funciones con argumentos variables *args y **kwargs

mi_funcion_lambda = lambda *args, **kwargs : len(args) + len(kwargs)

print(f"Funcion lambda con argumentos variables : {mi_funcion_lambda(1,2,3, a=3,b=7 )}")

