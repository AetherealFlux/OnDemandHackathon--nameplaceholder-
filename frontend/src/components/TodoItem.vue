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
  <div class="row border-top border-bottom py-3 px-4 bg-light rounded shadow-sm">
    <div class="d-flex align-items-start">
      <div class="flex-grow-1">
        <div class="row mb-2">
          <span class="p-0">
            <h3 class="fw-bold text-primary">{{ name }}</h3>
          </span>
        </div>
        <div class="row text-muted mb-1">{{ description }}</div>
        <div class="row text-secondary mb-2">{{ duration }}</div>
        <div class="row" v-if="subtasks && subtasks.length != 0">
          <p class="px-0 my-0 d-inline-flex">
            <a
              class="text-decoration-none text-info fw-semibold"
              data-bs-toggle="collapse"
              :href="'#collapse' + id"
              role="button"
              aria-expanded="false"
              :aria-controls="'collapse' + id"
            >
              Show Subtasks
            </a>
          </p>
          <div class="collapse mt-2" :id="'collapse' + id">
            <div class="row mb-2" v-for="task in subtasks" :key="task.title">
              <div class="p-2 bg-white border rounded shadow-sm">
                <div class="d-flex justify-content-between align-items-center">
                  <span class="fw-medium">{{ task.title }}</span>
                  <input class="ms-2 form-check-input" type="checkbox" />
                </div>
                <small class="text-muted">{{ task.estimatedDuration }}</small>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="ps-3 d-flex align-items-start">
        <input
          class="form-check-input"
          type="checkbox"
          style="width: min(6vw, 3vh); height: min(6vw, 3vh)"
        />
      </div>
    </div>
  </div>
</template>
