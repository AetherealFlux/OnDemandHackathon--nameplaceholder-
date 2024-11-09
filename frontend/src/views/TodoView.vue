<script setup lang="js">

import { ref } from 'vue';
import TodoItem from "@/components/TodoItem.vue";

const day = ref(10)

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
                <template v-for="item in [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]">
                    <TodoItem />
                </template>
            </div>
        </div>
        <div class="row">
            <div class="input-group mb-3 px-3">
                <input class="form-control form-control-lg" type="text" placeholder="What do you want to do?">
                <button class="btn btn-primary" type="button" data-bs-toggle="offcanvas"
                    data-bs-target="#offcanvasBottom" aria-controls="offcanvasBottom">Add</button>
            </div>
        </div>
        <div class="offcanvas offcanvas-bottom px-0" tabindex="-1" id="offcanvasBottom"
            aria-labelledby="offcanvasBottomLabel">
            <div class="offcanvas-header px-1">
                <input class="form-control form-control-lg" type="text" placeholder="What do you want to do?">
            </div>
            <div class="offcanvas-body small">
                
            </div>
        </div>
    </div>
</template>