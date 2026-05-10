<template>
  <div>
    <h2>Alert Dashboard</h2>
    <ul>
      <li v-for="alert in alerts" :key="alert.id">
        {{ alert.message }} ({{ alert.severity }})
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const alerts = ref([]);

const fetchAlerts = async () => {
  try {
    const res = await axios.get('http://localhost:8000/api/alerts');
    alerts.value = res.data;
  } catch (e) {
    console.error('Failed to fetch alerts', e);
  }
};

onMounted(() => {
  fetchAlerts();
});
</script>

<style scoped>
/* Add component specific styles here */
</style>
