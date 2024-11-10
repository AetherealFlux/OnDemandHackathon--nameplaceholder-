<script setup lang="js">
const props = defineProps({
  name: String,
  description: String,
  duration: String,
  id: Number,
  subtasks: Object,
})
</script>

<template>
  <div class="row border-top border-bottom py-2 px-4">
    <div class="col">
      <div class="row">
        <span class="p-0">
          <h3>{{ name }}</h3>
        </span>
      </div>
      <div class="row">{{ description }}</div>
      <div class="row">{{ duration }}</div>
      <div class="row" v-if="subtasks && subtasks.length != 0">
        <p class="px-0 my-0 d-inline-flex">
          <a
            data-bs-toggle="collapse"
            :href="'#collapse' + id"
            role="button"
            aria-expanded="false"
            :aria-controls="'collapse' + id"
          >
            Show Subtask
          </a>
        </p>
        <div class="collapse" :id="'collapse' + id">
          <div class="row" v-for="task in subtasks">
            <div>
              {{ task.title }} <input class="ms-2 form-check-input" type="checkbox" /><br />
              {{ task.estimatedDuration }}
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="col-1 ps-0">
      <div>
        <input
          class="form-check-input"
          type="checkbox"
          style="width: min(6vw, 3vh); height: min(6vw, 3vh)"
        />
      </div>
    </div>
  </div>
</template>
