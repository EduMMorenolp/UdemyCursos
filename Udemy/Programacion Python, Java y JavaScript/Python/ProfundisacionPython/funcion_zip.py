

# FUNCION ZIP 
#222

numero = (1,2,3)
letras =("a","b","c")
mescla = zip(letras,numero)
print(list(mescla))

#223

print(type(mescla)) # lo arma en base a la menor cantidad de iterables
identificadores = 100,101,102,103,104,105

mescla = zip(letras,numero,identificadores)
print(list(mescla))

#224

# Iterar en paralelo
for letras,numero,meslca in 