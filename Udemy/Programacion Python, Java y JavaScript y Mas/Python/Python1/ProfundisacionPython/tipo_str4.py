# PROFUNDISACION EN EL TIPO STR

# Seccion 33
# 198
# Caracteres tipo Byte

caracterEnBinario = b"Hola Mundo"

print(caracterEnBinario) 
print(caracterEnBinario[0]) # Caracter posicion 0 
print(chr(caracterEnBinario[0])) # chr lo convierte a Decimal 

lista_caracteres = caracterEnBinario.split() # 
print(lista_caracteres) # podes ver que se imprimer en fomrato Byte

#199

# CONVERTIR de String a Byte

string = " Hola Múndilo"
print(string)
bytes = string.encode("UTF-8") # Con encode convertirmos a byte el string
print(bytes)

# CONVERTIR de byte a String

string2 = bytes.decode() # Con decode lo convertimos de byte a string
print(string2) # Podemos ver que volvemos a formato original 

print(string == bytes)
print(string == string2)




 
