


# SECCION 31
# 189


# DAR formato a un STR

nombre = "juan"

edad = 48

Sueldo = 3000

# format de forma directa
mensaje = "Ejemplo 1 : nombre {} edad {} sueldo {:.2f}".format(nombre,edad,Sueldo)

print(mensaje)

# format Por INDICE
mensaje = "Ejemplo 2 : sueldo {2:.2f} edad {1} nombre {0}".format(nombre,edad,Sueldo)

print(mensaje)

# format Con Diccionarios
diccionario = {"nombre" : "juan", "edad": 35, "sueldo" : 3000}

mensaje = "Ejemplo 3 : nombre : {dic[nombre]} edad : {dic[edad]} sueldo : {dic[sueldo]:.2f} ".format(dic=diccionario) 

print(mensaje)

# Metodo print 

print(nombre, edad, Sueldo, sep= " , ") # sep agrega entre las variables que se pasan.  

# METODO f string

mensaje = f"Ejemplo 4 : nombre {nombre} edad {edad} sueldo {Sueldo:.2f}"

print(mensaje)

