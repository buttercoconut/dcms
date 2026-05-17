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

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';

interface Alert {
  id: number;
  message: string;
  severity: string;
}

const alerts = ref<Alert[]>([]);

const fetchAlerts = async () => {
  try {
    const response = await axios.get('/api/alerts');
    alerts.value = response.data;
  } catch (e) {
    console.error('Failed to fetch alerts', e);
  }
};

onMounted(() => {
  fetchAlerts();
});
</script>
