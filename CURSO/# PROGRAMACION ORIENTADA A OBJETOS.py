 # PROGRAMACION ORIENTADA A OBJETOS
 
 
class persona0:
    pass

# METODOS de clases de objetos

class persona0:
    def __init__(self): # metodo de clase domber (doble guion bajo)
        pass

class personas1:
    def __init__(self) -> None: #METODO INICIALIZADOR
        self.nombre1 = "juan"
        self.apellido1 = "perez"
        self.edad1 = 22
        
persona1 = personas1()

print("TEST 1")
print(persona1.nombre1)
print(persona1.apellido1)
print(persona1.edad1)

class personas2:
    def __init__(self, nombre, apellido, edad): #METODO INICIALIZADOR
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
         
persona2 = personas2("pablo", "Perez", 22) # PASAR VALORES A LA CLASE

print("TEST 2")
print(f"Persona 2 : {persona2.nombre} {persona2.apellido} {persona2.edad}") # FORMA COMPACTA


class persona3:
    def __init__(self, nombre, apellido, edad): #METODO INICIALIZADOR
        self.nombre3 = nombre
        self.apellido3 = apellido
        self.edad3 = edad    
    def mostrar_objeto(self):
        print(" TEST 3 ")
        print(f"Persona : {self.nombre3} {self.apellido3} {self.edad3}")
        
persona1 = persona3( "carlos", "santos", 51)
persona1.mostrar_objeto()

persona2 = persona3( "manu", "feo", 37)
persona2.mostrar_objeto()

# ejercicio aritmetica con classes

class atirmetica:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def arearecatangulo(self):
        return self.base * self.altura


base = int(input("Ingrese base : "))
altura = int(input("Ingrese altura : "))

resultado = atirmetica(base, altura)
print(f"reslutado : {resultado.arearecatangulo()}")


class tuplas_diccionarios: #se puede pasar valores como tublas y diccionarios
    def __init__(self, base, altura, *tuplas, **diccionarios):
        self.base = base
        self.altura = altura
        self.tuplas = tuplas
        self.diccionario = diccionarios
     
     def mostrar(self):
        print(f"Persona : {self.altura} {self.base} {self.tuplas} {self.diccionario}")
        
