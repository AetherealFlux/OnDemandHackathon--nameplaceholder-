<script setup lang="js">
defineProps({ title: String, startTime: String, estimatedDuration: String })

</script>

<template>
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">{{ title }}</h5>
            <h6 class="card-subtitle mb-2 text-muted">{{ startTime }}</h6>
            <p class="card-text">{{ estimatedDuration }}</p>
        </div>
    </div>
</template>