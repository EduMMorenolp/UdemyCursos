import datetime
import time

while True:
    # Obtener la hora actual
    ahora = datetime.datetime.now()

    # Imprimir la hora en formato hh:mm:ss
    print("Hora actual:", ahora.strftime("%H:%M:%S"))

    # Esperar un segundo antes de actualizar la hora
    time.sleep(1)