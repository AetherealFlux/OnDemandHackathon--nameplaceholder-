<script setup lang="js">
defineProps({ name: String, description: String, plan: String })
</script>
<template>
  <div class="row border-top border-bottom py-2 px-4">
    <div class="row">
      <span class="p-0">
        <h3>{{ name }}</h3>
      </span>
    </div>
    <div class="row">Plan: {{ plan }}</div>
  </div>
</template>
