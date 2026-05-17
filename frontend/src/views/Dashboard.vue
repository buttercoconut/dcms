<template>
  <div>
    <h1>Dashboard</h1>
    <ServerList />
    <AlertDashboard />
  </div>
</template>

<script setup lang="ts">
import ServerList from '@/components/ServerList.vue';
import AlertDashboard from '@/components/AlertDashboard.vue';
</script>
