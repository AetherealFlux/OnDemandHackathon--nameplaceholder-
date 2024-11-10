<script setup lang="js">
defineProps({ title: String, startTime: String, estimatedDuration: String })
</script>
<template>
  <div class="card mb-3 shadow-sm border-0 bg-light">
    <div class="card-body p-3">
      <h5 class="card-title fw-bold text-secondary">{{ title }}</h5>
      <h6 class="card-subtitle mb-2 text-muted">{{ startTime }}</h6>
      <p class="card-text text-dark">{{ estimatedDuration }}</p>
    </div>
  </div>
</template>
