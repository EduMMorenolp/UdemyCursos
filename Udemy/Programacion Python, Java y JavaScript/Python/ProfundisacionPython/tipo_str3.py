

#Seccion 32
#193
#194
#195
#196
#197

# Multiplicacion de Cadenas
#193

resultado = 5*"Hola"

print(f"Resultado 1 : {resultado}")

# Multiplicacion de Tuplas

resultado = 3*("Hola", "Mundo")

print(f"Resultado 2 : {resultado}")

# Multiplicacion de Listas

resultado = 3*[0,1]

print(f"Resultado 2 : {resultado} Largo de la lista : {len(resultado)}")



# Caracteres de Escape
#194

resultado = " Hola \" Mundo" # Corrije en el caso que no cierre la comillas bien.

print(f"Resultado 3 : {resultado}")

# Back Space 

resultado = 'Hola Mundo. \b\b\b' # no se imprime o elimina el ultimo caracter. 

print(f"Resultado 4 : {resultado}")

# Caracter \
    
resultado = "C\\Nuevo\\dir"

print(f"Resultado 5 : {resultado}")

# Raw string 

resultado = "Cadena \n Con salto de linea"

print(resultado)

resultado = r"Cadena \n Sin salto de linea" # No se procesa el salto de linea

print(resultado)



# Caracter Unicode
#195

print("Hola\u0020Mundo") # u en minuscula 0020 es una espacio en Unicode
print("Notacion simple : ","\u0041")

print("Notacion extendida", "\U00000041") # U en mayuscula 

print("Notacion Hexadecimal", "\x41" )

#196

print("Corazon", "\u2665") 

print("Carita sonriente", "\U0001f600")

# Caracteres ACSII

Caracter = chr(65)

print("Caracter en ACSII : ", Caracter)






