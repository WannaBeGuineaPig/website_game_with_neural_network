<script setup>

import SmallLogoApp from '../components/SmallLogoApp.vue'
import AuthPerAccBTN from '../components/AuthPerAccBTN.vue'
import TemplateBTN from '../components/TemplateBTN.vue'

document.title = 'Deal With Pixel - Авторизация';

function logInAccount() {
    alert('test');
}

</script>

<template>

<AuthPerAccBTN class="position-absolute end-0 top-0 m-4"/>
<SmallLogoApp  class="position-absolute start-0 top-0 mt-xl-3 mt-lg-2 ms-lg-1 mt-md-2 ms-md-2"/>

<div class="container-lg h-100 d-flex justify-content-center">
    <div class="col-sm-4 col-md-8 col-lg-10 d-flex align-items-center flex-column justify-content-evenly">
        <div class="text-center">
            <h1 class="main-font-family" style="font-size: 4vw;">Авторизация</h1>
            <div class="d-flex align-items-center justify-content-center main-font-family">
                <p class="main-font-family" style="font-size: 2.5vw; margin-bottom: 0;">Чтобы войти в систему, необходимо заполнить поля ниже</p>
                <img src="@/assets/images/Down.svg" style="max-width: 5vw;" alt="">
            </div>
        </div>
        <TemplateBTN textButton="Войти" :actionClick="logInAccount" style="max-width: 150px;" />
    </div>
        
</div>

</template>

<style scoped>
    
</style>