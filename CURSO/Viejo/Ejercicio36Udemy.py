edad = int(input("Ingrese una edad"))
mensaje = ""
if 0 < edad <= 10:
    mensaje = " La infancia es increible "
elif edad >= 11 and edad <= 20:
    mensaje = " Muchos cambios y Mucho estudio "
elif 21 <= edad <= 30:
    mensaje = " Amor y Comiensa trabajo "
elif edad > 31 :
    mensaje = " Que mas por delante (?) "
else:
    mensaje = "dato mal ingresado, ingrese un numero"
print(f" Su edad : {edad} , {mensaje}")
