


#200
#201


#from urllib.request import urlopen

#with urlopen("http://globalmentoring.com.mx/recursos/GlobalMentoring.txt") as mensaje:
    
    #contenido = mensaje.read().decode("utf-8")
    #print(contenido) # Formato origial





# NO ME FUNCIONA NADA NO TENGO IDEA.


#202
# upper convierte todo a MAYUSCULA

contenido = "Hola Mundo? Como va. Espero que bien. Adios"

print(contenido.upper())

# lover convierte todo a MINUSCULA

print(contenido.lower())

# startwith Inicia con...

print(contenido.startswith("Hola mundo"))

# endswith Termina con ...

print(contenido.endswith("Adios"))


#203 

print(contenido)

print(contenido.islower()) # Pregunto si es minicula el contenido

print(contenido.isupper()) # Pregunta si esta dodo en Mayuscula
 
#204

# ALINIAR CADENAS

# center - Centrar un str

titulo = " Sitio web Arcanos potengte.Arg.Com "

print(len(titulo))

print(titulo.center(50,"-")) # compeleta los caracteres 

print(len(titulo.center(50,"-"))) # solamente un caracter de RELLENO 

print(titulo.center(len(titulo)+50,"*")) # Agrega caracteres hasta llegar al numero deseado 

#205
# aliniar a la izquieda

print(titulo.ljust(50,"+"))

 # Alinia a la derecha
 
print(titulo.rjust(50, "+"))

#206

# Reemplaza contenido en un str

