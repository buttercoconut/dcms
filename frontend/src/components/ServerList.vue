<template>
  <div>
    <h2>Server List</h2>
    <table border="1" cellpadding="5" cellspacing="0">
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Status</th>
          <th>IP</th>
          <th>Uptime</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="server in servers" :key="server.id">
          <td>{{ server.id }}</td>
          <td>{{ server.name }}</td>
          <td>{{ server.status }}</td>
          <td>{{ server.ip_address }}</td>
          <td>{{ server.uptime }} hrs</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const servers = ref([]);

const fetchServers = async () => {
  try {
    const res = await axios.get('http://localhost:8000/api/servers');
    servers.value = res.data;
  } catch (e) {
    console.error('Failed to fetch servers', e);
  }
};

onMounted(() => {
  fetchServers();
});
</script>

<style scoped>
/* Add component specific styles here */
</style>
