<script setup lang="js">
const props = defineProps({ name: String, description: String, duration: Number, id: Number, subtasks: [Object] })

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
  <div class="row border-top border-bottom py-2 px-4">
    <div class="col">
      <div class="row">
        <span class="p-0">
          <h3>{{ name }} </h3>
        </span>
      </div>
      <div class="row">{{ description }}</div>
      <div class="row">{{ durationtext }}</div>
      <div class="row" v-if="subtasks && subtasks.length != 0">
        <p class="px-0 my-0 d-inline-flex">
          <a data-bs-toggle="collapse" :href="'#collapse' + id" role="button" aria-expanded="false"
            :aria-controls="'collapse'+id">
            Show Subtask
          </a>
        </p>
        <div class="collapse" :id="'collapse'+id">
          <div class="row" v-for="task in subtasks">
            <div>{{task.name}}<input class="ms-2 form-check-input" type="checkbox" /></div>
          </div>
          <div class="row">
            <div>{{task.name}}<input class="ms-2 form-check-input" type="checkbox" /></div>
          </div>
          <div class="row">
            <div>{{task.name}}<input class="ms-2 form-check-input" type="checkbox" /></div>
          </div>
        </div>
      </div>
    </div>
    <div class="col-1 ps-0">
      <div>
        <input class="form-check-input" type="checkbox" style="width: min(6vw, 3vh); height: min(6vw, 3vh)" />
      </div>
    </div>
  </div>
</template>
