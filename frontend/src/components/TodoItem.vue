<script setup lang="js">
</script>

<template>
    <div class="row border-top border-bottom py-2 px-4">
        <div class="col">
            <div class="row">
                <span class="p-0">
                    Name <span class="badge text-bg-danger">!!!</span>
                </span>
            </div>
            <div class="row">
                Description
            </div>
            <div class="row">
                Duration DDL
            </div>
            <div class="row">
                <p class="px-0 my-0 d-inline-flex">
                    <a data-bs-toggle="collapse" href="#collapseExample" role="button"
                        aria-expanded="false" aria-controls="collapseExample">
                        Show Subtask
                    </a>
                </p>
                <div class="collapse" id="collapseExample">
                    <div class="row">
                        <div>123<input class="ms-2 form-check-input" type="checkbox"></div>
                    </div>
                    <div class="row">
                        <div>123<input class="ms-2 form-check-input" type="checkbox"></div>
                    </div>
                    <div class="row">
                        <div>123<input class="ms-2 form-check-input" type="checkbox"></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-1 ps-0">
            <div>
                <input class="form-check-input" type="checkbox" style="width:min(6vw, 3vh);height:min(6vw, 3vh);">
            </div>
        </div>
    </div>
</template>