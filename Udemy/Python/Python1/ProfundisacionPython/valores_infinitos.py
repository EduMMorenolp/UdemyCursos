


# Paquete para verificar un numero infitino
import math
from decimal import Decimal


# Manejo de numeros infinitos

infinito_positivo = float("inf") # Asi se representa el infinito
print(f"Infinito positivo : {infinito_positivo} ")
print(f" Es Infitino ? : {math.isinf(infinito_positivo)}") # math.isinf comando que responde con F o T 

infinito_negativo = float("-inf") 
print(f"Infinito positivo : {infinito_negativo} ")
print(f" Es Infitino ? : {math.isinf(infinito_negativo)}")

# Creando infinito con el Modulo math

infinito_positivo = math.inf 
print(f"Infinito positivo Modulo math : {infinito_positivo} ")
print(f" Es Infitino ? : {math.isinf(infinito_positivo)}") # math.isinf comando que responde con F o T 

infinito_negativo = -math.inf 
print(f"Infinito positivo Modulo math : {infinito_negativo} ")
print(f" Es Infitino ? : {math.isinf(infinito_negativo)}")

# Infinito con Modulo Decimal

infinito_positivo = Decimal("Infinity")
print(f"Infinito positivo Modulo Decimal Positivo : {infinito_positivo} ")
print(f" Es Infitino ? : {math.isinf(infinito_positivo)}")

infinito_negativo = Decimal("-Infinity")
print(f"Infinito positivo Modulo Decimal Negativo : {infinito_negativo} ")
print(f" Es Infitino ? : {math.isinf(infinito_negativo)}")



