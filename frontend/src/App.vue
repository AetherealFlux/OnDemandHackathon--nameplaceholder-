<script setup>
import { RouterView, useRouter } from 'vue-router'
import { ref } from 'vue'

const activenum = ref(0)
const pagename = ["todo", "schedule", "habit"]
const router = useRouter()

function nav(to) {
  activenum.value = to
  router.push({ name: pagename[to] })
}

</script>

<template>
  <div class="container-fluid vh-100 justify-content-between p-0">
    <div class="d-flex flex-column h-100 p-0">
      <div class="container-fluid flex-grow-1 px-0 overflow-y-hidden">
        <RouterView />
      </div>
      <div class="container-fluid px-0 border-top">
        <nav class="nav nav-pills nav-justified">
          <a class="nav-link col-3" :class="{ active: activenum == 0 }" @click="nav(0)">Todo</a>
          <a class="nav-link col-3" :class="{ active: activenum == 1 }" @click="nav(1)">Schedule</a>
          <a class="nav-link col-3" :class="{ active: activenum == 2 }" @click="nav(2)">Habit</a>
        </nav>
      </div>
    </div>
  </div>
</template>