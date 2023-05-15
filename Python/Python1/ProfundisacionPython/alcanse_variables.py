
# ALCANSE DE VARIABLES

#237

var_global = "Variable Global"

def imprimir():
    # Acceder a una variable global
    print(f"Variable Gloabal desde funcion {var_global}")
    # Variable Local
    var_local = "Variable Local"
    print(f"Variable Local desde funcion {var_local}")
    def Anidada():
        print(f"Variable Local de funcion Anidada : {var_local}")
    Anidada()

imprimir()

#238

def imprimir():
    # la forma de accecer a una variable global y poder usarla en la funcion es:
    global var_global
    var_global = "Nueva variable Global"
    print(f"Variable Gloabal desde funcion {var_global}")

imprimir()

#239
print(f"#239".center(50,"-" ))
# Mas de funciones anidadas y alcanse

def funcion_externa():
    
    variable_local_externa = "Variable Local Externa"
    
    def funcion_anidada():
        
        variable_anidada_local = "Variable Local Anidada"
        
        nonlocal variable_local_externa
        
        variable_local_externa = " Nuevo valor Variable Local Externa"
        
    funcion_anidada()
     
    print(f"Funcion Externa Modificada : {variable_local_externa}")
     
funcion_externa()

#240
print(f"#240".center(50,"-" ))
# Definimos variable Global

contador = 0

def mostrar_contador():
    print(contador)
    
def modificar_contador(c):
    global contador
    contador = c
    
modificar_contador(5)
mostrar_contador()

#241

# USOS DE FUNCIONES

# First class citizens 

def suma(a,b):
    return a+b

# 1-Asignar una funcion a una variable (no se usan parentesis)

mi_funcion = suma

# Verificar tipo de variable
print(type(mi_funcion))
# llamamos la funcion a traves de la Variable 
print(mi_funcion(3,4))

print(f"#242".center(50,"-" ))

# 2-Funcion como Argumento 

def operacion(a,b, suma_def):
    print(f"Resultado suma {suma_def(a,b)}")
    
operacion(3,5, suma)

# 3 - retorna funcion 

def retornar_funcion ():
    return suma

mi_funcion_return = retornar_funcion()

print(f"Funcion retornada {mi_funcion_return(1,9)}")

