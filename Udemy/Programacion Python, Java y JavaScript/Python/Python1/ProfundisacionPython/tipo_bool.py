


# bool contiene los datos False o True

# Tipo numericos, Flase para 0 y True para el resto
print("NUMERICO")
valor = 0
resultado = bool(valor)
print(f" valor : {valor} de tipo : {resultado}")

valor = 1
resultado = bool(valor)
print(f" valor : {valor} de tipo : {resultado}")

# Tipo String, Falso "", Verdadero demas valores
print("STRING")
valor = ""
resultado = bool(valor)
print(f" valor : {valor} de tipo : {resultado}")

valor = "a"
resultado = bool(valor)
print(f" valor : {valor} de tipo : {resultado}")

# Tipo colecciones, Falso para vacias, Verdadero para las llenas
#LISTAS
print("LISTAS")
valor = []
resultado = bool(valor)
print(f" valor lista : {valor} de tipo : {resultado}")

valor = [2,3,"hola"]
resultado = bool(valor)
print(f" valor lista : {valor} de tipo : {resultado}")

#TUPLAS
print("TUPLAS")
valor = ()
resultado = bool(valor)
print(f" valor tupla : {valor} de tipo : {resultado}")

valor = (2,3,"hola")
resultado = bool(valor)
print(f" valor tupla : {valor} de tipo : {resultado}")

#DICCIONARIO
print("DICCIONARIO")
valor = {}
resultado = bool(valor)
print(f" valor diccionario : {valor} de tipo : {resultado}")

valor = {"nombre" : "juan", "edad" : 33}
resultado = bool(valor)
print(f" valor diccionario : {valor} de tipo : {resultado}")    


# CONDICIONALES
print("CONDICIONALES if/else")
variable_vacia = []
variable_llena = [2,3,4]
if bool(""): # DEFINIDO
    print("Regresa Verdadero")
else:
    print("Definido Regresa Falso (Vacio)")
   
if "": # SIN DEFINIR
    print("Regresa Verdadero")
else:
    print("Sin Definir Regresa Falso (Vacio)") 
    
if bool("a"): # DEFINIDO
    print("Definido Regresa Verdadero (lleno)")
else:
    print("Regresa Falso")
   
if "a": # SIN DEFINIR
    print("Sin Definir Regresa Verdadero (lleno)")
else:
    print("Regresa Falso")   
    
while variable_vacia:
    print("se ejecuta infito") # por VERDADERO
else:
    print("se termina") # por FALSO

