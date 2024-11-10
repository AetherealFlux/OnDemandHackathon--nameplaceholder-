<script setup lang="js">
const props = defineProps({ name: String, duration: String })

</script>

<template>
    <div class="row border-top border-bottom px-4">
        <div class="row">{{ name }}</div>
        <div class="row">{{ duration }}</div>
    </div>
</template>