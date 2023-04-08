

#245

# Un closure es una funcion que define a otra, y ademas la regresa


def operacion(a,b):
    def sumar():
        return a+b
    return sumar    


mi_funcion_closure = operacion(3,4)

print(f" Mi funcion closure : {mi_funcion_closure()}")

# podemos llamar la funcion al vuelo

print(f"Funcion closure al vuelo : {operacion(5,4)()}")

#246

# Ahora con funcion lambda

def operacion1(a,b):
    # funcion lambda
    return lambda : a+b

mi_funcion_closure = operacion1(3,4)
print(f" Mi funcion closure lambda : {mi_funcion_closure()}")

