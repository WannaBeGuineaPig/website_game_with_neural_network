<script setup>

import TemplateBTN from './TemplateBTN.vue'
import router from '../router'
import { inject } from 'vue'
import { getTopics } from '@/assets/scripts/action-topics'

const $cookies = inject('$cookies')

let topics = await getTopics()

function startTheGame() {
    let typeGame = document.getElementById('selectTypeGame').value;
    if (typeGame == 'traing'){
        $cookies.set('gameSetting', {
            'typeGame' : typeGame,
            'typeImageGame' : document.getElementById('selectTypeImage').value,
        })
        let myBTN = document.getElementById('btnClose');
        myBTN.click();
        window.location = 'http://localhost:5173/game' 
    }
    else{
        
    }
}

function changeTypeGame(e){
    const typeImage = document.getElementById('selectTypeImage');
    const text = document.getElementById('TextTypeImage');
    const categoryImage = document.getElementById('selectCategoryImage');

    if(e.target.value == 'traing'){
        typeImage.style.display = 'block';
        text.style.display = 'block';
        categoryImage.selectedIndex = 0;
        categoryImage.disabled = true;
    }
    else{
        typeImage.style.display = 'none';
        text.style.display = 'none';
        categoryImage.disabled = false;
    }
}

</script>

<template>
<div class="modal fade main-font-family letter-spacing-five" id="gameSettingModal" tabindex="-1" aria-labelledby="gameSettingModalLabel" aria-hidden=" true">
  <div class="modal-dialog modal-lg modal-dialog-centered modal-dialog-scrollable">
    <div class="modal-content">
        <div class="modal-header">
            <h4 class="modal-title" id="gameSettingModalLabel">Настройка игры</h4>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Закрыть"></button>
        </div>
      
        <div class="modal-body">
            
            <h5>Выбор категории изображений: </h5>
            <select class="form-select letter-spacing-five" id="selectCategoryImage" disabled>
                <option selected value="all">Все категории</option>
                <option value="animal">Животные</option>
                <option value="Figure">Геометрические фигуры</option>
            </select>
            
            <h5 id="TextTypeImage" class="mt-3">Выбор тип изображения: </h5>
            <select class="form-select letter-spacing-five" id="selectTypeImage">
                <option :value="topic" v-for="topic in topics">{{ topic }}</option>
            </select>

            <h5 class="mt-3">Выбор типа игры: </h5>
            <select class="form-select letter-spacing-five" id="selectTypeGame" v-on:change="changeTypeGame">
                <option selected value="traing">Тренировка</option>
                <option disabled value="twoPainter">Лобби на двух(1vs1).P.s. в будущем...</option>
                <option disabled value="therePainter">Лобби на троих(1vs2).P.s. в будущем...</option>
                <option disabled value="fourPainter">Лобби на четверых(1vs3).P.s. в будущем...</option>
                <option disabled value="fivePainter">Лобби на пятерых(1vs4).P.s. в будущем...</option>
            </select>

        </div>
        <div class="modal-footer">
            <div>
                <TemplateBTN textButton="Начать поиск игры" :actionClick="startTheGame" style="font-size: 2.5vh;"/>
            </div>
            <div>
                <TemplateBTN id="btnClose" textButton="Закрыть" data-bs-dismiss="modal" style="font-size: 2.5vh;"/>
            </div>
        </div>
    </div>
  </div>
</div>


</template>

<style>

</style>