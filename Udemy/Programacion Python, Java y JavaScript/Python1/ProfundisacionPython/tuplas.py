


# PROFUNDISACION en Tuplas

# Declarar variables

a , b = "Hola","Mundo"
print(a,b)

# swap ( intercambio de variables )

a, b = b, a
print(a,b)

# regresar multiples valores en una funcion

def minmax (elementos):
   return min(elementos), max(elementos)

a,b = minmax([1,2,3,7,5])

print(a,b)

# regresa la suma 

# Una forma
resultado = sum((1,2,3,4,5))
print(f"Primera forma : {resultado}")

def suma(*argm):
    return sum(argm)

resultado = suma(1,2,3,4,5)
print(f"Segunda  forma : {resultado}")


