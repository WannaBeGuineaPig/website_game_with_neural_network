<script setup>

import TemplateBTN from './TemplateBTN.vue'


function setSizeBrush(){
    const canvas = document.getElementById("сanvasDrawing");
    if(canvas == undefined)
    {
        return;
    }

    const ctx = canvas.getContext("2d");
    ctx.lineWidth = document.getElementById('sizeBrush').value;
    const myBtn = document.getElementById('CloseBtn');
    myBtn.click();
}

function changeRangeData(){
    const rangeInput = document.getElementById('sizeBrush');
    const rangeOutput = document.getElementById('sizeBrushValue');

    rangeOutput.textContent = rangeInput.value;
}

function backToCurrent(){
    const rangeInput = document.getElementById('sizeBrush');
    const rangeOutput = document.getElementById('sizeBrushValue');
    rangeInput.value = document.getElementById("сanvasDrawing").getContext("2d").lineWidth;
    rangeOutput.textContent = rangeInput.value;
}

</script>

<template>
    <div class="modal fade" id="setSizeBrush" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="setSizeBrushLabel">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="setSizeBrushLabel">Изменение размера пера/ластика</h5>
                <button v-on:click="backToCurrent" type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Закрыть"></button>
            </div>
            <div class="modal-body">
                <label for="sizeBrush" class="form-label">Выберете размер пера/ластика: </label>
                <input type="range" class="form-range" min="1" max="100" value="1" id="sizeBrush" v-on:input="changeRangeData">
                <output for="sizeBrush" id="sizeBrushValue" aria-hidden="true">1</output>
            </div>
            <div class="modal-footer d-flex">
                <div class="">
                    <TemplateBTN textButton="Применить" :actionClick="setSizeBrush" style="font-size: 2.5vh;" />
                </div>  
                <div class="">
                    <TemplateBTN id="CloseBtn" :actionClick="backToCurrent" textButton="Отменить" data-bs-dismiss="modal" style="font-size: 2.5vh;" />
                </div>
            </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
    
</style>