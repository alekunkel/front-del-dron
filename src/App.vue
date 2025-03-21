<script setup>
import { createApp } from 'vue';
import { createPinia } from 'pinia';
import { createRouter, createWebHistory } from 'vue-router';
import Dashboard from './views/Dashboard.vue';
import videodron from './components/videodron.vue';

const pinia = createPinia();
const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: Dashboard }
  ]
});

const app = createApp({
  components: {
    Dashboard,
    videodron
  }
});

app.use(pinia);
app.use(router);
app.mount('#app');
</script>

<template>
    <Dashboard />
    <videodron />
</template>

<style>
.fondo{
  background-color: aliceblue;
}
h1, h2, h3, h4, p{
  color: rgb(55, 0, 255);
}
</style>
