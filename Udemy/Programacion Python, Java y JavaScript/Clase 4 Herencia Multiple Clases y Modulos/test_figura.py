from Cuadrado import Cuadrado

cuadrado1 = Cuadrado(5, "rojo")
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.color)

print(cuadrado1.calcular_area())

#MRO -  METHOD RESOLUTION ORDER (para saber el orden que se llama cada clase)

print(Cuadrado.mro())





