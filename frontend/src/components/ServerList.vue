<template>
  <div>
    <h2>Servers</h2>
    <ul>
      <li v-for="server in servers" :key="server.id">
        {{ server.name }} - {{ server.status }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../api'

const servers = ref([])

onMounted(async () => {
  try {
    const { data } = await api.get('/servers')
    servers.value = data
  } catch (e) {
    console.error(e)
  }
})
</script>
