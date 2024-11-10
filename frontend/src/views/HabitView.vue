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

async function addHabit(habit) {
  try {
    const response = await fetch(
      `http://localhost:8000/addHabit?name=${habit.name}&plan=${habit.plan}`,
    )
    if (!response.ok) {
      throw new Error(`Adding habit was not ok, status: ${response.statusText}`)
    }
  } catch (error) {
    console.error('Error occured:', error)
  }
}

function onSubmit() {
  if (habitName.value.trim() !== '') {
    let newHabit = {
      name: habitName.value.trim(),
      description: habitDescription.value.trim(),
      plan: habitPlan.value.trim(),
    }
    addHabit(newHabit).then(() => {
      window.location.reload()
    })
  }
}
async function getPlan(habitName) {
  try {
    const response = await fetch(`http://localhost:8000/genHabitPlan?habit=${habitName}`)
    if (!response.ok) {
      throw new Error(`Generating plan was not ok, status: ${response.statusText}`)
    }
    return await response.json()
  } catch (error) {
    console.error('Error occured:', error)
    return []
  }
}

async function onGenerate() {
  const plan = await getPlan(habitName.value)
  habitPlan.value = plan.data
}
</script>
<template>
  <div class="d-flex flex-column h-100 bg-light shadow-sm rounded">
    <div class="row flex-grow-1 h-100 overflow-y-auto">
      <div class="container h-100 py-3">
        <HabitItem
          v-for="item in habitList.Habits"
          :key="item.name"
          :name="item.name"
          :description="item.description"
          :plan="item.plan"
          class="mb-3"
        />
      </div>
    </div>
    <div class="row bg-white py-2 shadow-sm border-top">
      <div class="input-group mb-3 px-3">
        <input
          class="form-control form-control-lg border-success rounded-start"
          type="text"
          placeholder="Want to have good habits?"
          v-model.lazy="habitName"
        />
        <button
          class="btn btn-success btn-lg rounded-end"
          type="button"
          data-bs-toggle="offcanvas"
          data-bs-target="#offcanvasBottom"
          aria-controls="offcanvasBottom"
          @click="onGenerate()"
        >
          Start
        </button>
      </div>
    </div>
    <div
      class="offcanvas offcanvas-bottom h-75 border-top shadow-lg"
      tabindex="-1"
      id="offcanvasBottom"
      aria-labelledby="offcanvasBottomLabel"
    >
      <div class="offcanvas-header px-3 bg-light">
        <input
          class="form-control form-control-lg mb-2 border-success rounded"
          type="text"
          placeholder="Want to have good habits?"
          v-model.lazy="habitName"
        />
      </div>
      <div class="offcanvas-body bg-white">
        <div class="mb-3">
          <label for="habitPlan" class="form-label">
            <h4 class="text-success">Plan</h4>
          </label>
          <textarea
            class="form-control border-secondary rounded"
            id="habitPlan"
            rows="15"
            v-model="habitPlan"
            disabled
          ></textarea>
          <div class="row p-2 mt-3 justify-content-between">
            <button type="button" class="btn btn-secondary btn-lg col-3" @click="onGenerate()">
              Regen
            </button>
            <button type="button" class="btn btn-success btn-lg col-8" @click="onSubmit()">
              Submit
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
