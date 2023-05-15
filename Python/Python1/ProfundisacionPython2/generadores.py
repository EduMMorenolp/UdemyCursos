

# Generadores
# 249
def generador():
    yield 1
    print(f"Se reanuda la ejecucion")
    yield 2
    print(f"Se reanuda la ejecucion")
    yield 3
    
gen = generador()

print(next(gen))
print(next(gen))
print(next(gen))
# Tira error si pide mas de los generadores 
# print(next(gen))

# Generador con metodo for
print(f" Generador con metodo FOR ")
for valor in generador():
    print(f"{valor}")
    
# 250
 