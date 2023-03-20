from FiguraGeometrica import *
from Color import *


class Cuadrado(FiguraGeometrica, Color): # EL ORDEN AFECTA A COMO LLAMA CLASES
    def __init__(self, lado, color):
        #super().__init__(lado, color) FORMA NO CORRECTA DE PASAR POR HERENCIA
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self ,color)
        
    def calcular_area(self):
        return self.alto * self.ancho
    
    
    
        