<script setup>

import { RouterLink, RouterView } from 'vue-router'
import InformationModal from './components/InformationModal.vue'
import GameSettingModal from './components/GameSettingModal.vue'
import SetSizeBrushModal from './components/SetSizeBrushModal.vue'
import SetTypeImageModal from './components/SetTypeImageModal.vue'

document.title = "Deal With Pixel - ";

</script>

<template>

<!-- Модальное окно со справочной информацией -->

<InformationModal />

<!--  -->

<!-- Модальное окно с выбором типа игры -->

<GameSettingModal />

<!--  -->


<!-- Модальное окно с выбором пера -->

<SetSizeBrushModal />

<!--  -->

<!-- Модальное окно с выбором типа изображения -->

<SetTypeImageModal />

<!--  -->

  <div class="position-relative vh-100">
    <div class="z-3 position-absolute vh-100 container-fluid d-flex justify-content-center align-items-center">
      <router-view></router-view>
    </div>
    <div class="background-color-page z-1 vh-100 vw-100 position-absolute"></div>
    
    <div class="box-image z-2 position-absolute opacity-50">
      <img src="@/assets/images/hexagon_left_top.svg" alt="">
    </div>

    <div class="box-image z-2 position-absolute opacity-50 bottom-0 end-0">
      <img src="@/assets/images/hexagon_right_bottom.svg" alt="">
    </div>
    
  </div>


</template>

<style scoped>

.box-image{
  max-width: 30vw;
}
.box-image img{
  max-width: 100%;
  max-height: 100%;
}

</style>
