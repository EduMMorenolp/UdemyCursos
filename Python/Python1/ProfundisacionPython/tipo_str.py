



# PROFUNDISANDO EN STR

# Concatenacion Automatica en Python
#183

variable = "Adios Mundo..."
mensaje = " Hola " "Mundo " # se concatena sin el + 
print(mensaje)
mensaje = mensaje + variable # pero no sirve para variables
print(mensaje)
mensaje += " Eh " "Vuelto!" # pero si de forma directa
print(mensaje)

# SOLICITANDO AYUDA
#184

#help(str)

# DOCSTRING
#185

from mi_clase import MiClase

#help(MiClase)
print("MICLASE".center(50,"-"))
print(MiClase.__doc__)
print("INIT".center(50,"-"))
print(MiClase.__init__.__doc__)


# SRT INMUTABLES 
#186
print("SRT INMUTABLES")
mensaje1 = "hola mundo" # INMUTABLE
mensaje2 = mensaje1.capitalize() # Modifica 
print(f"Mensaje 1 : {mensaje1}")
print(f"Mensaje 2 : {mensaje2}")


# METODO JOIN (UNIR)
#187
print("METODO JOIN (UNIR)")

tupla_lista = ["Hola","mundo","!!"]
print(f"TUPLA o LISTAS {tupla_lista}")
mensaje = " ".join(tupla_lista) # (caracters).join(lista,tupla) Para unir el contenido con la variable
print(mensaje)

cadena = "Holamundo"
print(cadena)
mensaje = ".".join(cadena)
print(mensaje)

diccionario = {"nombre":"juan","edad":"10","apellido":"Perez"} # SOLO PARA CARACTERES
llaves = "-".join(diccionario.keys()) # INDICANDOLE QUE UNIR DEL DICCIONARIO
valores = "*".join(diccionario.values())

print(f" diccionario : {diccionario} tipo : {type(diccionario)}")
print(f" llaves : {llaves} tipo : {type(llaves)}")
print(f" llaves : {valores} tipo : {type(valores)}")


# METODO SPLIT (SEPARAR)
#188
print("METODO SPLIT (SEPARAR)")

cursos = "Java Python SQL Angular Excel"
lista_cursos = cursos.split() # POR DEFAULT el SEPARA VA A SER "" (espacio en blanco)

print(f" variable de caracteres : {cursos} tipo : {type(cursos)}")
print(len(cursos))
print(f" lista : {lista_cursos} tipo : {type(lista_cursos)}")
print(len(lista_cursos)) # VER CANTIDAD DE OBJETOS

lista_cursos = cursos.split(" ", 2) # MAX SPLIT ( cantida de separaciones )

print(f" lista max 2 separaciones : {lista_cursos} tipo : {type(lista_cursos)}")
print(len(lista_cursos))


