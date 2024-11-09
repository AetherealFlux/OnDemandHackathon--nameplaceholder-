<script setup lang="js">
import { ref } from "vue";

const habit = ref("")
const plan = ref("")

function generatePlan() {
    plan.value = "Generating..."
}

function regeneratePlan() {
    plan.value = "ReGenerating..."
}

</script>

<template>
    <div class="d-flex flex-column h-100">
        <div class="row flex-grow-1 h-100 overflow-y-auto">
            <div class="container h-100">
                <template v-for="item in [1, 1, 1]">
                    <div class="row border-top border-bottom py-2 px-4">
                        <div class="row">
                            <span class="p-0">
                                <h3>Name</h3>
                            </span>
                        </div>
                        <div class="row">
                            Description
                        </div>
                    </div>
                </template>
            </div>
        </div>
        <div class="row">
            <div class="input-group mb-3 px-3">
                <input class="form-control form-control-lg" type="text" placeholder="Want to have good habits?"
                    v-model.lazy="habit" />
                <button class="btn btn-primary" type="button" data-bs-toggle="offcanvas"
                    data-bs-target="#offcanvasBottom" aria-controls="offcanvasBottom" @click="generatePlan()">
                    Start
                </button>
            </div>
        </div>
        <div class="offcanvas offcanvas-bottom h-50" tabindex="-1" id="offcanvasBottom"
            aria-labelledby="offcanvasBottomLabel">
            <div class="offcanvas-header px-1">
                <input class="form-control form-control-lg" type="text" placeholder="Want to have good habits?"
                    v-model.lazy="habit" />
            </div>
            <div class="offcanvas-body">
                <div class="mb-3">
                    <label for="habitPlan" class="form-label">
                        <h3>Plan</h3>
                    </label>
                    <textarea class="form-control" id="habitPlan" rows="10" v-model="plan" disabled></textarea>
                    <div class="row p-2 justify-content-between">
                        <button type="button" class="btn btn-secondary btn-lg col-3">Regenerate</button>
                        <button type="button" class="btn btn-primary btn-lg col-8">Submit</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
