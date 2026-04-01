<script setup>

import LogoApp from '../components/LogoApp.vue'
import AuthPerAccBTN from '../components/AuthPerAccBTN.vue'
import TemplateBTN from '../components/TemplateBTN.vue'

document.title = 'Deal With Pixel - Меню игры';

function startTheGame() {
    alert("ПОЛУЧИЛОСЬ?!");
}

</script>

<template>


<AuthPerAccBTN class="position-absolute end-0 top-0 m-4"/>
<div class="vh-100 overflow-y-auto overflow-x-hidden d-flex flex-column justify-content-evenly align-items-center">
    <LogoApp />
    <TemplateBTN textButton="Играть" :actionClick="startTheGame"/>
    <!-- <TemplateBTN /> -->
    <!-- <TemplateBTN /> -->
    <TemplateBTN textButton="Справка" :actionClick="() => {}" data-bs-toggle="modal" data-bs-target="#projectInformationModal"/>
</div>


</template>


<style scoped>


</style>