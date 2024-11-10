<script setup lang="js">
defineProps({ name: String, description: String, plan: String })
</script>
<template>
  <div class="row border-top border-bottom py-3 px-4 bg-light rounded shadow-sm mb-3">
    <div class="d-flex flex-column">
      <span class="p-0">
        <h3 class="fw-bold text-success">{{ name }}</h3>
      </span>
      <div class="text-muted mt-1">
        Plan: <span class="fw-medium">{{ plan }}</span>
      </div>
    </div>
  </div>
</template>
