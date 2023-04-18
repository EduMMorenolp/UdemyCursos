

# Profundisacion de SET

#229

# Un set es conjunto de elmentos unicos y mutable
# Y sus elementos deven ser inmutables

# Set vacio

conjun = {"Hola", True, 27}
print(type(conjun))
conjunto = {} # esto no es un set es una diccionario, forma inconrrecta
print(type(conjunto))
conjunto = set() # forma correcta
print(type(conjunto))

# MUTABLE

conjunto.add("Juan")
print(conjunto)

# Contiene Valores unicos 

conjunto.add("Juan") # volverlo a agregar solamente reemplaza
print(conjunto)

# Crear un set a partir de un Iterable

conjunto = set([1,2,3,4,2]) # no se repiten al crearlos
print(conjunto)

#230

# Podemos agregar mas elementos 

conjunto2 = {100,200,400}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20,30,56])
print(conjunto)

# Copiar de un Set a otro Set, solo se copian las referencias

conjunto_copia = conjunto.copy()
print(conjunto_copia)

#231

# Operaciones de conjuntos 

pelo_negro = {"Carla", "Juan", "Pablo"}
pelo_rubio = {"Pedro","Juana"}
ojos_marones = {"Carla","Esther"}
mayor = {"Esther","Pablo "}

# Funcion Union (Union) (conmutativa) Une sin retepir elementos
print(ojos_marones.union(pelo_negro))
# Invertir el orden (conmutativa) (Union)
print(pelo_negro.union(ojos_marones))

#232

# Funcion Intersetion (conmutativa) / Une dejando solamente los repetidos 
print(ojos_marones.intersection(mayor))


# Funcion Difference # elementos que se encuentren en el primer y no en el segundo set

print(pelo_negro.difference(ojos_marones))

# Funcion Simetric Diffrerence # Uno o Otro elemento de los sets

print(f"a{pelo_negro.symmetric_difference(ojos_marones)}")

#233
 
# Pregunta si un set esta contenido dentro de otro

# si contiene en el set
print(pelo_negro.issubset(ojos_marones))

# si es un super set 
print(pelo_negro.issuperset(ojos_marones))

# si tiene algo en comun
print(pelo_negro.isdisjoint(ojos_marones))

