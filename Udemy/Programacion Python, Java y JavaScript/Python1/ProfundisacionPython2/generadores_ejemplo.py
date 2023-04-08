
#250

# generador de numeros 1 a 5
def generador_numeros():
    for numero in range(1,6):
        yield numero 
        print(f"Se reaunda la generacion")
        
        
# Utitlizamos en generador 
generador = generador_numeros()
print(f"objeto generador : {generador}")
print(type(generador))

# Consumimos los valores ciclo for
for valor in generador:
    print(f" Numero producido : {valor}")
    
# Cusimimos a demanda
generador = generador_numeros()
try: # hacemos un ciclo try para que no nos tire error
    print(f"Consumidor a demanda :  {next(generador)}")
    print(f"Consumidor a demanda :  {next(generador)}")
    print(f"Consumidor a demanda :  {next(generador)}")
    print(f"Consumidor a demanda :  {next(generador)}")
    print(f"Consumidor a demanda :  {next(generador)}")
    print(f"Consumidor a demanda :  {next(generador)}")
except StopIteration as e:
    print(f" Error en consumir en generador ") 
    
       
# Consumimor los valores ciclo while 

generador = generador_numeros()
while True:
    try:
        valor = next(generador)
        print(f" Valor generador {valor}")
    except StopIteration as e: 
        print(f" Error en consumir en generador ")  
        break
    
        