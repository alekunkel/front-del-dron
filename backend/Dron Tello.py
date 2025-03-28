import cv2
import openai
import os
import base64
from djitellopy import Tello

client = openai.OpenAI(api_key=""
tello = Tello()

tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

print(tello.get_battery())

tello.takeoff()
tello.go_xyz_speed(100,-100,100,40)
tello.rotate_clockwise(100)
cv2.imwrite("picture1.png", frame_read.frame)
tello.rotate_clockwise(-100)

tello.go_xyz_speed(100,100, 0, 40)
cv2.imwrite("picture2.png", frame_read.frame)

tello.go_xyz_speed(-100,100, 0, 40)
tello.rotate_clockwise(-100)
cv2.imwrite("picture3.png", frame_read.frame)

tello.rotate_clockwise(100)

tello.go_xyz_speed(-100,-100,-100,40)

tello.land()

# Identificacion de imágen:
image_path = r"C:\Users\Estudiante ProA\Desktop\feria - copia\picture1.png"

# Convertir la imagen a Base64
with open(image_path, "rb") as img_file:
    base64_image = base64.b64encode(img_file.read()).decode("utf-8")

# Enviar la imagen a OpenAI
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Si identificás fuego en la imágen, escribe la palabra 'Fuego' y si no se observa nada, escribe la palabra 'NADA'"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{base64_image}"
                    },
                },
            ],
        }
    ],
)

# Imprimir la descripción de la imagen
print(response.choices[0].message.content)