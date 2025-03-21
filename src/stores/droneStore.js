import { defineStore } from 'pinia';

export const useDroneStore = defineStore('drone', {
  state: () => ({
    battery: 100,            
    altitude: 0,             
    additionalInfo: '',      
    capturedPhotos: [],      
    alerts: []               
  }),
  actions: {
    // Acción para actualizar el nivel de batería
    updateBattery(level) {
      this.battery = level;
    },
    // Acción para actualizar la altura del dron
    updateAltitude(height) {
      this.altitude = height;
    },
    // Acción para agregar una alerta
    addAlert(alert) {
      this.alerts.push(alert);
    },
    // Acción para agregar una foto
    addPhoto(photo) {
      this.capturedPhotos.push(photo);
    }
  }
});
