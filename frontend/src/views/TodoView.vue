<script setup lang="js">
import { ref } from 'vue';
import TodoItem from '@/components/TodoItem.vue';
import SubtaskItem from '@/components/SubtaskItem.vue';

const day = ref(10)
const todo = ref("")

const description = ref("")
const duration = ref("")
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

function genSubtask() {
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
          <TodoItem v-for="item in todoList" :name="item.title" :description="item.description"
            :duration="item.duration" :id="item.id" />
        </template>
      </div>
    </div>
    <div class="row">
      <div class="input-group mb-3 px-3">
        <input class="form-control form-control-lg" type="text" placeholder="What do you want to do?"
          v-model.lazy="todo" />
        <button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasBottom"
          aria-controls="offcanvasBottom" @click="genSubtask()">
          Add
        </button>
      </div>
    </div>
    <div class="offcanvas offcanvas-bottom h-50" tabindex="-1" id="offcanvasBottom"
      aria-labelledby="offcanvasBottomLabel">
      <div class="offcanvas-header px-1">
        <input class="form-control form-control-lg" type="text" placeholder="What do you want to do?"
          v-model.lazy="todo" />
      </div>
      <div class="offcanvas-body">
        <div class="mb-3 row">
          <input class="form-control my-2" type="text" placeholder="Description">
          <input class="form-control my-2" type="text" placeholder="Duration" disabled>
          <template v-for="subtask in subtasks">
            <SubtaskItem :name="subtask.name" :duration="subtask.duration" />
          </template>
          <div class="row ms-1 mt-2 justify-content-between">
            <button type="button" class="btn btn-secondary btn-lg col-3">Regenerate</button>
            <button type="button" class="btn btn-primary btn-lg col-8">Submit</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
