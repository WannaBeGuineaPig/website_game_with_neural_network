<script setup>

import TemplateBTN from './TemplateBTN.vue'

function setTypeImage() {
  const typeImage = document.getElementById('selectTypeImageGame').value;
}


</script>

<template>

<div class="modal fade main-font-family letter-spacing-five" id="setTypeImage" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="setTypeImageLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <h4 class="modal-title" id="setTypeImageLabel">Выбор тип изображения</h4>
        <button type="button" id="closeBtnTypeImage" class="btn-close" data-bs-dismiss="modal" aria-label="Закрыть"></button>
      </div>
      <div class="modal-body">
        <h5>Выберете тип изображения, для предсказания нейросетью: </h5>
        <select class="form-select letter-spacing-five" id="selectTypeImageGame">
            <option selected value="cat">Кот</option>
            <option value="dog">Собака</option>
        </select>
      </div>
      <div class="modal-footer">
        <div class="">
          <TemplateBTN textButton="Предсказать" :actionClick="setTypeImage" style="font-size: 2.5vh;" />
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