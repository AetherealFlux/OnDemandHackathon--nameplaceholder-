<script setup lang="js">
import { ref } from 'vue'
import HabitItem from '@/components/HabitItem.vue'

let habitList = ref([])
const habitName = ref('')
const habitDescription = ref('')
const habitPlan = ref('')

async function getHabitList() {
  try {
    const response = await fetch('http://localhost:8000/getHabits')
    if (!response.ok) {
      throw new Error(`Network response was not ok, status: ${response.status}`)
    }
    return await response.json()
  } catch (error) {
    console.error('Problem with fetch:', error)
    return []
  }
}
getHabitList().then((val) => {
  habitList.value = val
})
// if (val.length > 0) habitList.value = val
// else
//   habitList.value = [
//     { name: 'Read a book', description: 'Read a book everyday', plan: 'Read 10 pages per day' },
//   ]
// })

async function addHabit(habit) {
  try {
    const response = await fetch(
      `http://localhost:8000/addHabit?name=${habit.name}&description=${habit.description}`,
    )
    if (!response.ok) {
      throw new Error(`Adding habit was not ok, status: ${response.statusText}`)
    }
  } catch (error) {
    console.error('Error occured:', error)
  }
}

function onSubmit() {
  if (habitName.value.trim() !== '' && habitDescription.value.trim() !== '') {
    let newHabit = {
      name: habitName.value.trim(),
      description: habitDescription.value.trim(),
      plan: habitPlan.value.trim(),
    }
    addHabit(newHabit)
  }
}
function generatePlan() {}

function regeneratePlan() {
  plan.value = 'ReGenerating...'
}
</script>

<template>
  <div class="d-flex flex-column h-100">
    <div class="row flex-grow-1 h-100 overflow-y-auto">
      <div class="container h-100">
        <HabitItem
          v-for="item in habitList.Habits"
          :name="item.name"
          :description="item.description"
          :plan="item.plan"
        />
      </div>
    </div>
    <div class="row">
      <div class="input-group mb-3 px-3">
        <input
          class="form-control form-control-lg"
          type="text"
          placeholder="Want to have good habits?"
          v-model.lazy="habitName"
        />
        <button
          class="btn btn-primary"
          type="button"
          data-bs-toggle="offcanvas"
          data-bs-target="#offcanvasBottom"
          aria-controls="offcanvasBottom"
          @click="generatePlan()"
        >
          Start
        </button>
      </div>
    </div>
    <div
      class="offcanvas offcanvas-bottom h-50"
      tabindex="-1"
      id="offcanvasBottom"
      aria-labelledby="offcanvasBottomLabel"
    >
      <div class="offcanvas-header px-1">
        <input
          class="form-control form-control-lg"
          type="text"
          placeholder="Want to have good habits?"
          v-model.lazy="habitName"
        />
        <input
          class="form-control form-control-lg"
          type="text"
          placeholder="Want to have good descriptions?"
          v-model.lazy="habitDescription"
        />
      </div>
      <div class="offcanvas-body">
        <div class="mb-3">
          <label for="habitPlan" class="form-label">
            <h3>Plan</h3>
          </label>
          <textarea
            class="form-control"
            id="habitPlan"
            rows="10"
            v-model="habitPlan"
            disabled
          ></textarea>
          <div class="row p-2 justify-content-between">
            <button type="button" class="btn btn-secondary btn-lg col-3">Regenerate</button>
            <button type="button" class="btn btn-primary btn-lg col-8" @click="onSubmit()">
              Submit
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
