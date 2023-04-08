




# 257

class Persona:
    contador_personas = 0

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# Mostrar los atributos de un objeto
persona1 = Persona('Juan','Perez')
print(persona1.__dict__)

# Crear un atributo al vuelo
print(persona1.contador_personas) # Accediendo al atributo de clase
# Pero no es posible modificarlo con el objeto, sino con la clase
persona1.contador_personas = 10
print(persona1.__dict__)
# El atributo anterior oculta al atributo de clase
print(Persona.contador_personas) # Atributo clase
print(persona1.contador_personas) # Atributo del objeto 1

# Un segundo objeto
persona2 = Persona('Karla', 'Gomez')
print(persona2.__dict__)
print(persona2.contador_personas)

# Asociar un atributo de clase al vuelo
Persona.contador2 = 20
print(Persona.contador2)

# Desde los objetos creados, accedemos al nuevo atributo de la clase
# Esto es posible por que los atributos de clase se comparten con todos los objetos
print(persona1.contador2)
print(persona2.contador2)

#258

# Simulación de sobrecarga de constructores en python
# otras formas de crear objectos
class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    @classmethod
    def crear_persona_vacia(cls):
        return cls(None, None)

    @classmethod
    def crear_persona_con_valores(cls, nombre, apellido):
        return cls(nombre, apellido)

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}'

persona1 = Persona('Juan', 'Perez')
print(persona1)

persona_vacio = Persona.crear_persona_vacia()
print(persona_vacio)

persona_con_valores = Persona.crear_persona_con_valores('Karla', 'Gomez')
print(persona_con_valores)

#259


