




# DECORADORES 
#247
# Lo utilizamos para extender funcionalidad
# 1 Funcion decorador A
# 2 Funcion a decorar B
# 3 funcion decorada C

def funcion_decorador_A(funcion_a_decorar_b):
    def funcion_decorada_C():
        print(f"Antes de ejecutar decorador")
        funcion_a_decorar_b()
        print(f"Despues de ejecutar decorador")
    return funcion_decorada_C


@funcion_decorador_A
def mostrar_mensaje():
    print(f"Hola desde mi funcion decorada!")
    
mostrar_mensaje()   


#248

def funcion_decorador_A(funcion_a_decorar_b):
    def funcion_decorada_C(*args,**kwargs):
        print(f"Antes de ejecutar decorador")
        res = funcion_a_decorar_b(*args,**kwargs)
        print(f"Despues de ejecutar decorador")
        return res
    return funcion_decorada_C

@funcion_decorador_A
def sumar(a,b):
    return a+b

resultado = sumar(5,4)

print(f"Suma {resultado}")