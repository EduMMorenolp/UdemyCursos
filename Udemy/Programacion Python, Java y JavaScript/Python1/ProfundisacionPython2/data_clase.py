
#277 - 278 

from dataclasses import dataclass
from typing import ClassVar

@dataclass(eq=True, frozen=True)
class Domicilio:
    calle: str
    numero: int = 0

@dataclass(eq=True, frozen=True)
class Persona:
    nombre: str
    apellido: str
    domicilio: Domicilio
    contador_personas: ClassVar[int] = 0

    def __post_init__(self):
        if not self.nombre:
            raise ValueError(f'Valor nombre vacío: {self.nombre}')

domicilio1 = Domicilio('Saturno', 15)
persona1 = Persona('Juan','Perez', domicilio1)
print(f'{persona1!r}')
# Variable de clase
print(f'Variable clase: {Persona.contador_personas}')
# Variables de instancia
print(f'Variables de instancia: {persona1.__dict__}')
# Variable con valores vacíos
persona_vacia = Persona('Karla','', None)
print(f'Persona vacía: {persona_vacia}')
# Revisar igualdad entre objetos (__eq__)
persona2 = Persona('Juan','Perez', Domicilio('Saturno', 15))
print(f'Objetos iguales?: {persona1 == persona2}')
# Agregar esta clase a una colecciones
coleccion = {persona1, persona2}
print(coleccion)
# Frozen = True
# coleccion[0].nombre='Juan Carlos'
# persona1.nombre = 'Juan Carlos'

