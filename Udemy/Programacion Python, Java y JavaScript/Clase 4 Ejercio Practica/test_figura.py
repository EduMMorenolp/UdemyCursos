from Cuadrado import Cuadrado
from Rectangulo import rectangulo

cuadrado1 = Cuadrado(5, "rojo")
print(f"AREA DEL CUADRADO : {cuadrado1.calcular_area()}")
print(cuadrado1)

#MRO -  METHOD RESOLUTION ORDER (para saber el orden que se llama cada clase)
print(Cuadrado.mro())

rectangulo1 = rectangulo(3, 4, "Verde")
print(f"AREA DEL RECTANGULO : {rectangulo1.calcular_area()}")
print(rectangulo1)