

class persona:
    def __init__(self, nombre, apellido, edad): #METODO INICIALIZADOR
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad    
        
    @property
    def nombre(self):
        return self.nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre : nombre

    @property
    def apellido(self):
        return self.apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido : apellido
        
    @property
    def edad(self):
        return self.edad
    
    @edad.setter
    def edad(self, edad):
        self._edad : edad
    
    def mostrar_objeto(self):
       print(f"Persona : {self._nombre} {self._apellido} {self._edad}")
       
    def __del__(self):
        print(f"Persona : {self._nombre} {self._apellido}")
 

        
       
#persona1 = persona( "carlos", "santos", 51)
#persona1.mostrar_objeto()