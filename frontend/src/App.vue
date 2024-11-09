<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="container-fluid vh-100 justify-content-between">
    <div class="container-fluid h-100">
      <RouterView />
    </div>
    <div class="container-fluid">
      <nav class="nav nav-pills nav-justified">
        <a class="nav-link" href="/todo">Todo</a>
        <a class="nav-link" href="/schedule">Schedule</a>
        <a class="nav-link" href="/habit">Habit</a>
      </nav>
    </div>
  </div>
</template>