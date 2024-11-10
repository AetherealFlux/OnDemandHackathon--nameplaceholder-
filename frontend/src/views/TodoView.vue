<script setup lang="js">
import { ref } from 'vue'
import TodoItem from '@/components/TodoItem.vue'
import SubtaskItem from '@/components/SubtaskItem.vue'

const day = ref(10)
const todoName = ref('')
const todoDesc = ref('')
const todoDur = ref('')
const subtasks = ref([])

async function getTodoList() {
  try {
    const response = await fetch('http://localhost:8000/getTodos')
    if (!response.ok) {
      throw new Error(`Network response was not ok, status: ${response.status}`)
    }
    return await response.json()
  } catch (error) {
    console.error('Problem with fetch:', error)
    return []
  }
}

async function addTodo(todoObj) {
  try {
    const response = await fetch(
      `http://localhost:8000/addTodo?title=${todoObj.title}${todoObj.description && `&description=${todoObj.description}`}${todoObj.duration && `&estimatedDuration=${todoObj.duration}`}&subtasks=${JSON.stringify(todoObj.subtasks)}`,
    )
    if (!response.ok) {
      throw new Error(`Network response was not ok, status: ${response.status}`)
    }
    return await response.json()
  } catch (error) {
    console.error('Problem with adding todo:', error)
    return []
  }
}
async function getSubtask(name) {
  try {
    const response = await fetch(`http://localhost:8000/genSubtodos?todo=${name}`)
    if (!response.ok) {
      throw new Error(`Generation subtasks was not ok, status: ${response.statusText}`)
    }
    return await response.json()
  } catch (error) {
    console.error('Problem with gen subtodos', error)
    return []
  }
}

function onAdd() {
  getSubtask(todoName.value).then((val) => {
    subtasks.value = JSON.parse(val.data).content
  })
}

function onSubmit() {
  let todoObj = {
    title: todoName.value,
    description: todoDesc.value,
    duration: todoDur.value,
    subtasks: subtasks.value,
  }
  addTodo(todoObj).then(() => {
    window.location.reload()
  })
}

let todoList = ref([])
getTodoList().then((val) => {
  todoList.value = val
})
</script>

<template>
  <div class="d-flex flex-column h-100">
    <!-- <div class="row h-10">
            <div class="col-3">
                <button type="button" class="btn btn-light" @click="day -= 1">Yesterday</button>
            </div>
            <div class="col">
                <h3 class="text-center mt-2">{{ day }}/11/2024</h3>
            </div>
            <div class="col-3">
                <button type="button" class="btn btn-light" @click="day += 1">Tomorrow</button>
            </div>
        </div> -->
    <div class="row flex-grow-1 h-100 overflow-y-auto">
      <div class="container h-100">
        <template v-for="todoList in todoList">
          <TodoItem
            v-for="item in todoList"
            :name="item.title"
            :description="item.description"
            :duration="item.estimatedDuration"
            :subtasks="item.subTodo"
            :id="item.id"
          />
        </template>
      </div>
    </div>
    <div class="row">
      <div class="input-group mb-3 px-3">
        <input
          class="form-control form-control-lg"
          type="text"
          placeholder="What do you want to do?"
          v-model.lazy="todoName"
        />
        <button
          class="btn btn-primary"
          type="button"
          data-bs-toggle="offcanvas"
          data-bs-target="#offcanvasBottom"
          aria-controls="offcanvasBottom"
          @click="onAdd()"
        >
          Add
        </button>
      </div>
    </div>
    <div
      class="offcanvas offcanvas-bottom h-75"
      tabindex="-1"
      id="offcanvasBottom"
      aria-labelledby="offcanvasBottomLabel"
    >
      <div class="offcanvas-header px-1">
        <input
          class="form-control form-control-lg"
          type="text"
          placeholder="What do you want to do?"
          v-model.lazy="todoName"
        />
      </div>
      <div class="offcanvas-body">
        <div class="mb-3 row">
          <input
            class="form-control my-2"
            type="text"
            placeholder="Description"
            v-model="todoDesc"
          />
          <input class="form-control my-2" type="text" placeholder="Duration" disabled />
          <template v-for="subtask in subtasks">
            <SubtaskItem :name="subtask.title" :duration="subtask.estimatedDuration" />
          </template>
          <div class="row ms-1 mt-2 justify-content-between">
            <button type="button" class="btn btn-secondary btn-lg col-3" @click="onAdd()">
              Regenerate
            </button>
            <button type="button" class="btn btn-primary btn-lg col-8" @click="onSubmit()">
              Submit
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
