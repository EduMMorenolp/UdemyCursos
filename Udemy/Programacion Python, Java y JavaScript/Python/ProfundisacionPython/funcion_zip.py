

# FUNCION ZIP 
#222

numero = (1,2,3)
letras =("a","b","c")
mescla = zip(letras,numero)
print(list(mescla))

#223

print(type(mescla)) # lo arma en base a la menor cantidad de iterables
identificadores = 100,101,102,103,104,105

mescla = zip(letras,numero,identificadores)
print(list(mescla))

#224

# Iterar en paralelo
nueva_lista = []
for letras,numero,identificadores, in zip(letras,numero,identificadores,):
    print(f"Letra : {letras}, Numero : {numero}, ID : {identificadores}")
    nueva_lista.append(f"{letras}-{numero}-{identificadores}")
    
print(nueva_lista)

#225

# Unzip 

mesclas = [('a', 1, 100), ('b', 2, 101), ('c', 3, 102)]
letras,numero,id = zip(*mesclas)

print(f"{letras}---{numero}---{id}")

#226

# Ordenar Zip

letras = ['b', 'a', 'e',"c"]
numeros = [2, 3, 1, 4]
mesclas = zip(letras,numeros)
print(f"Sin ordenar : {tuple(mesclas)}")

# ordenar las letras y numeros
print(sorted(zip(letras,numeros)))

#227

# Crear un diccionario con un zip con dos iterales

llaves = ["Nombre", "Apellido","Edad"]
valores = ["Juan", "Perez", 32]

diccionario = dict(zip(llaves,valores))

print(diccionario)

# Actualizar nuestro Diccionario

llave = ["Edad"]
nueva_edad = [30]
diccionario.update(zip(llave,nueva_edad))
print(diccionario)

