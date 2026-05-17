<template>
  <div>
    <h2>Server List</h2>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Status</th>
          <th>IP</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="server in servers" :key="server.id">
          <td>{{ server.id }}</td>
          <td>{{ server.name }}</td>
          <td>{{ server.status }}</td>
          <td>{{ server.ip_address }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';

interface Server {
  id: number;
  name: string;
  status: string;
  ip_address: string;
}

const servers = ref<Server[]>([]);

const fetchServers = async () => {
  try {
    const response = await axios.get('/api/servers');
    servers.value = response.data;
  } catch (e) {
    console.error('Failed to fetch servers', e);
  }
};

onMounted(() => {
  fetchServers();
});
</script>

<style scoped>
  table {
    width: 100%;
    border-collapse: collapse;
  }
  th, td {
    border: 1px solid #ddd;
    padding: 8px;
  }
  th {
    background-color: #f2f2f2;
  }
</style>