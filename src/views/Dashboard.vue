<script setup>
import { useDroneStore } from '../stores/droneStore.js'; 

// Acceder al store dentro del setup()
const droneStore = useDroneStore(); // Inicializa el store
</script>

<template>
  <div class="fondo">
    <div class="dashboard">
      <div class="top-bar">
        <span><strong>BATERIA:</strong> {{ droneStore.battery }}%</span>
        <span><strong>ALTURA:</strong> {{ droneStore.altitude }}m</span>
        <span><strong>INFO. ADICIONAL:</strong> {{ droneStore.additionalInfo }}</span>
        <span><strong>FOTOS CAPTURADAS:</strong> {{ droneStore.capturedPhotos.length }}</span>
      </div>
      <div class="content">
        <div class="left-column">
          <div class="alerts">
            <h3>ALERTAS:</h3>
            <ul>
              <li v-for="(alert, index) in droneStore.alerts" :key="index">{{ alert }}</li>
            </ul>
          </div>
          <div class="map">
            <img src="https://via.placeholder.com/150x150.png?text=Mapa" alt="Mapa del dron">
          </div>
        </div>
        <div class="camera-view">
          <h3>Vista de la cámara del dron</h3>
          <img src="https://via.placeholder.com/350x200.png?text=Vista+de+la+Cámara" alt="Vista de la cámara del dron">
          <p>Batería: {{ droneStore.battery }}%</p>
          <p>Altura: {{ droneStore.altitude }}m</p>
          <button @click="droneStore.addPhoto('fotoNueva')">Capturar Foto</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Fondo general */
.fondo {
  background-color: #e5ddd5; /* Fondo beige claro */
  min-height: 100vh;
  padding: 20px;
  box-sizing: border-box;
  font-family: Arial, sans-serif;
  color: #333; /* Texto más legible: gris oscuro */
}

/* Dashboard contenedor principal */
.dashboard {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

/* Barra superior con datos clave */
.top-bar {
  display: flex;
  justify-content: space-around;
  background-color: #ffffff;
  padding: 10px;
  border-radius: 8px;
  font-weight: bold;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

/* Contenido principal: alertas/mapa + cámara */
.content {
  display: flex;
  gap: 20px;
}

/* Columna izquierda: alertas + mapa */
.left-column {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.alerts {
  border: 1px solid #000;
  padding: 10px;
  width: 200px;
  height: 200px;
  background-color: #ffffff;
  border-radius: 8px;
}

.map {
  width: 200px;
  height: 200px;
  border-radius: 8px;
  overflow: hidden;
}

.map img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Vista de la cámara combinada con los estilos previos */
.camera-view {
  background-color: #f3fff0;
  border: 2px solid #ccc;
  border-radius: 12px;
  padding: 20px;
  text-align: center;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.camera-view img {
  max-width: 100%;
  border-radius: 8px;
  margin-bottom: 10px;
}

.camera-view h3 {
  margin-bottom: 10px;
  font-size: 1.5em;
  color: #222; /* Más oscuro y legible */
}

.camera-view p {
  margin: 10px 0;
  font-weight: bold;
  color: #333;
}

.camera-view button {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1em;
  transition: background-color 0.3s ease;
}

.camera-view button:hover {
  background-color: #45a049;
}

.camera-view button:focus {
  outline: 2px solid #4CAF50;
  outline-offset: 2px;
}
</style>

