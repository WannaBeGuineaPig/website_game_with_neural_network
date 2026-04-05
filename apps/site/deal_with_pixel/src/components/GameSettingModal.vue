<script setup>

import TemplateBTN from './TemplateBTN.vue'
import router from '../router'

function startTheGame() {
    if (document.getElementById('selectTypeGame').value == 'traing'){
        let myBTN = document.getElementById('btnClose');
        myBTN.click();
        router.push('/game');
    }
    else{
        
    }
}

</script>

<template>

<div class="modal fade" id="gameSettingModal" tabindex="-1" aria-labelledby="gameSettingModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg modal-dialog-centered modal-dialog-scrollable">
    <div class="modal-content">
        <div class="modal-header">
            <h4 class="modal-title" id="gameSettingModalLabel">Настройка игры</h4>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Закрыть"></button>
        </div>
      
        <div class="modal-body">
            
            <h5>Выбор категории изображений: </h5>
            <select class="form-select">
                <option selected value="all">Все категории</option>
                <option value="animal">Животные</option>
                <option value="Figure">Геометрические фигуры</option>
            </select>

            <h5>Выбор типа игры: </h5>
            <select class="form-select" id="selectTypeGame">
                <option selected value="traing">Тренировка</option>
                <option disabled value="animal">Лобби на двух(1vs1).P.s. в будущем...</option>
                <option disabled value="animal">Лобби на троих(1vs2).P.s. в будущем...</option>
                <option disabled value="animal">Лобби на четверых(1vs3).P.s. в будущем...</option>
                <option disabled value="animal">Лобби на пятерых(1vs4).P.s. в будущем...</option>
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