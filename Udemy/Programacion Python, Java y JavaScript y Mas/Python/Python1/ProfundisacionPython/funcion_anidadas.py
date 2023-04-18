

# FUNCIONES ANIDADAS

#236

def calculadora(a,b):
    # Funcion anidada
    def sumar(a,b):
        return a+b
    def resta(a,b):
        return a-b
# llamamos la funcion
    print(f"Suma : {sumar(a,b)}")
    print(f"Resta: {resta(a,b)}")


calculadora(3,4)


    
    