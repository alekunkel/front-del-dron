import serial
from djitellopy import Tello
import time

# Inicializar el Tello
tello = Tello()
tello.connect()

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)  # Espera a que Arduino esté listo
while True:
    

    # Verificar el nivel de batería
    battery = tello.get_battery()
    print(f"Batería del dron: {battery}%")
    # Conectar al puerto serial del Arduino (ajusta el puerto según tu sistema)
    # Verifica si la batería es menor a 100 y envía señal al Arduino
    if battery < 99:
        print("Batería baja. Activando el relé para cargar el dron...")
        arduino.write(b'1')  # Enviar '1' para activar el relé
    else:
        print("Batería al 100%. No es necesario cargar.")
        arduino.write(b'0')  # Enviar '0' para desactivar el relé

    # Esperar un poco para asegurarse de que el mensaje se envíe
    time.sleep(2)

    # Cerrar la conexión serial
    arduino.close()
    time.sleep(60)

        