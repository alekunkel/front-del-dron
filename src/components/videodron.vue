<script setup>
import { useDroneStore } from '../stores/droneStore.js'; 

// Acceder al store
const droneStore = useDroneStore();
</script>

<template>
  <div class="camera-view">
    <h3>Vista de la cámara del dron</h3>
    <p>Batería: {{ droneStore.battery }}%</p>
    <p>Altura: {{ droneStore.altitude }}m</p>
    <button @click="droneStore.addPhoto('fotoNueva')">Capturar Foto</button>
  </div>
</template>

<style>
.camera-view {
  background-color: #f3fff0;
  border: 2px solid #ccc;
  border-radius: 12px;
  padding: 20px;
  text-align: center;
  max-width: 400px;
  margin: auto;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}


.camera-view img {
  max-width: 100%;
  border-radius: 8px;
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


h1, h2, h3, h4 {
  color: #222;
}

p {
  color: #333;
}
</style>
