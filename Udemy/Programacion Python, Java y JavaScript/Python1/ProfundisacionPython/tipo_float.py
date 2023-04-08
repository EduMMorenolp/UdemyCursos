


#Profundisacion Float

a = 3.0
print(F"a = {a}")
# Interpolacion
print(F"a interpolada = {a:.2f}")

# Contructor de float puede recivir int o string

b = float(10) # int
b1 = float("10") # string
print(F"b = {b:.2f} y b1 = {b1:.2f}")

# Notacion exponencial ( valores + y -)

e = 1e2 # Positivo
print(f"e = {e:.2f}")
e = 1e-2 # Negativo
print(f"e = {e:.3f}")

# Cualquier calculo con un float se volvera float

f = 4.5
f1 = 5
f2 = f + f1
print(f"flotante {f2} Tipo {type(f2)}")

