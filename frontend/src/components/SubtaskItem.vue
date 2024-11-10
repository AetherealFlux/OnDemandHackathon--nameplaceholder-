<script setup lang="js">
const props = defineProps({ name: String, duration: Number })

let durationtext = ""
let duration = props.duration

if (duration < 60) {
    durationtext = duration + " second"
}
else if (duration < 3600) {
    durationtext = Math.floor(duration / 6) / 10 + " min"
}
else if (duration < 216000) {
    durationtext = Math.floor(duration / 360) / 10 + " hour"
}
else {
    durationtext = "Long time"
}
</script>

<template>
    <div class="row border-top border-bottom px-4">
        <div class="row">{{ name }}</div>
        <div class="row">{{ durationtext }}</div>
    </div>
</template>