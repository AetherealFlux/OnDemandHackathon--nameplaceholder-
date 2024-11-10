<script setup lang="js">
import { ref } from 'vue'
import ScheduleItem from '@/components/ScheduleItem.vue'

async function getSchedule() {
  try {
    const response = await fetch('http://localhost:8000/genSchedule')
    if (!response.ok) {
      throw new Error(`Network response was not ok, status: ${response.status}`)
    }
    return await response.json()
  } catch (error) {
    console.error('Error getting schedule: ', error)
  }
}

const events = ref([])
const postpones = ref([])
const comment = ref('Generating...')

getSchedule().then((val) => {
  try {
    val = JSON.parse(val.data)
    console.log(val)
    comment.value = val.comment
    events.value = val.events
    postpones.value = val.postpone
  } catch (error) {
    comment.value = val.data
  }
})
</script>
<template>
  <div class="d-flex flex-column h-100 bg-light shadow-sm rounded">
    <div class="row flex-grow-1 h-100 overflow-y-auto">
      <div class="container h-100 py-3">
        <h4 class="text-secondary fw-bold mb-3">{{ comment }}</h4>
        <div class="mb-4">
          <ScheduleItem
            v-for="item in events"
            :key="item.title"
            :title="item.title"
            :start-time="item.startTime"
            :estimated-duration="item.estimatedDuration"
            class="mb-3"
          />
        </div>
        <div v-if="postpones.length > 0" class="mt-4">
          <h5 class="text-warning fw-semibold mb-2">Postponed</h5>
          <ScheduleItem
            v-for="item in postpones"
            :key="item.title"
            :title="item.title"
            :start-time="item.startTime"
            :estimated-duration="item.estimatedDuration"
            class="mb-3"
          />
        </div>
      </div>
    </div>
  </div>
</template>
