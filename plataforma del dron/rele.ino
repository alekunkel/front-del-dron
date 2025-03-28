int relePin = 7;  // Pin donde está conectado el relé

void setup() {
  // Inicializar el pin del relé como salida
  pinMode(relePin, OUTPUT);
  
  // Inicializar la comunicación serial
  Serial.begin(9600);
}

void loop() {
  // Verificar si se recibe un dato desde el puerto serial
  if (Serial.available() > 0) {
    char received = Serial.read();  // Leer el dato recibido

    if (received == '1') {
      // Activar el relé (cargar el dron)
      digitalWrite(relePin, HIGH);  // Enciende el relé
      Serial.println("Relé activado. Cargando el dron...");
    }
    else if (received == '0') {
      // Desactivar el relé (detener carga)
      digitalWrite(relePin, LOW);  // Apaga el relé
      Serial.println("Relé desactivado.");
    }
  }
}
