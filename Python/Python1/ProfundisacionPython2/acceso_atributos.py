# Ejemplo atributos publicos, protegidos, privados
class MiClase:
    def __init__(self, publico, protegido, privado):
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado


objeto = MiClase('Valor público', 'Valor protegido', 'Valor privado')
# Acceso al valor publico
print(objeto.publico)
# Modificar el valor publico
objeto.publico = 'Modificando valor público'
print(objeto.publico)

# Acceso al valor protegido
# Solo dentro de la misma clase o clase hija
print(objeto._protegido)
# Modificando valor protegido (solo dentro misma clase o subclases)
objeto._protegido = 'Modificando valor protegido'
print(objeto._protegido)

# Accediendo al valor privado (solo dentro de la misma clase)
# Directamente no se puede acceder
#print(objeto.__privado)
# Pero, se convierte a objeto._clase__atributo_privado
print(objeto._MiClase__privado)
# Incluso se puede modificar
objeto._MiClase__privado = 'Cambiando valor privado'
print(objeto._MiClase__privado)

# En conclusión, no se puede comparar con otros lenguajes
# como C++ o Java, ya que no es la misma funcionalidad
# ni las mismas limitantes
# Debemos ser programadores responsables y respetar las buenas prácticas
# Impuestas en Python
# En la mayoría de los casos es suficiente con usar un guión bajo
# para encapsular y ocultar el detalle de una clase si somos programadores responsables