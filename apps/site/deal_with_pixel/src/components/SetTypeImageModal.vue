<script setup>

import TemplateBTN from './TemplateBTN.vue'
import { getTopics } from '@/assets/scripts/action-topics'
import { inject, ref } from 'vue'
import { getPredictModel } from '@/assets/scripts/predict-model.js'

const $cookies = inject('$cookies');
const gameSetting = $cookies.get('gameSetting');
let topics = await getTopics()
const predictData = ref('')

function getPredictData() {
  predictData.value = 'Идёт предсказание, ожидайте...';
  let typeImage = document.getElementById('selectTypeImageGame').value;
  let canvas = document.getElementById('сanvasDrawing')
  if (canvas == undefined) return;
  canvas.toBlob(async function (blob) {
    predictData.value = await getPredictModel(typeImage, blob);
  })
}


</script>

<template>

<div class="modal fade main-font-family letter-spacing-five" id="setTypeImage" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="setTypeImageLabel" aria-hidden="true">
  <div class="modal-dialog  modal-lg modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <h4 class="modal-title" id="setTypeImageLabel">Выбор тип изображения</h4>
        <button type="button" id="closeBtnTypeImage" class="btn-close" data-bs-dismiss="modal" aria-label="Закрыть"></button>
      </div>
      <div class="modal-body">
        <h5>Выберете тип изображения, для предсказания нейросетью: </h5>
        <select class="form-select letter-spacing-five" id="selectTypeImageGame">
            <option :value="topic" :selected="gameSetting.typeImageGame == topic" v-for="topic in topics">{{ topic }}</option>
        </select>
        <p style="font-size: 2.5vh; white-space: pre-wrap;">{{ predictData }}</p>
      </div>
      <div class="modal-footer">
        <div class="">
          <TemplateBTN textButton="Предсказать" :actionClick="getPredictData" style="font-size: 2.5vh;" />
        </div>
        <div class="">  
            <TemplateBTN textButton="Отменить" data-bs-dismiss="modal" style="font-size: 2.5vh;" />
        </div>

      </div>
    </div>
  </div>
</div>

</template>

<style>
    
</style>