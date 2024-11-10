<script setup lang="js">
import { ref } from 'vue';
import ScheduleItem from '@/components/ScheduleItem.vue';

async function getSchedule() {
  try {
    const response = await fetch('http://localhost:8000/genSchedule')
    if (!response.ok) {
      throw new Error(`Network response was not ok, status: ${response.status}`)
    }
    return await response.json()
  } catch (error) {
    return await response.json()
  }
}

const events = ref([])
const postpones = ref([])
const comment = ref("Generating...")

getSchedule().then((val) => {
  try {
    val = JSON.parse(val.data)
    console.log(val)
    comment.value = val.comment
    events.value = val.events
    postpones.value = val.postpone
  }
  catch (error) {
    comment.value = val.data
  }
})

</script>

<template>
    <div class="d-flex flex-column h-100">
        <div class="row flex-grow-1 h-100 overflow-y-auto">
        <div class="container h-100">
            <h4>{{comment}}</h4>
            <ScheduleItem
            v-for="item in events"
            :title="item.title"
            :start-time="item.startTime"
            :estimated-duration="item.estimatedDuration"
            />
            <br>
            <h5 v-if="postpones.length > 0">Postponed</h5>
            <ScheduleItem
            v-for="item in postpones"
            :title="item.title"
            :start-time="item.startTime"
            :estimated-duration="item.estimatedDuration"
            />
        </div>
        </div>
    </div>
</template>