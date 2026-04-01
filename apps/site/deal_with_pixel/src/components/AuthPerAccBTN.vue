<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { inject } from 'vue';

const $cookies = inject('$cookies');

defineProps({
    canClick: {
        default: true
    },
})

</script>

<template>

<router-link :to="canClick ? ($cookies.isKey('test') ? '/personal-account' : '/authorization') : ''" class="box-btn d-flex justify-content-center align-items-center">
    <img src="@/assets/images/Unauthorized.svg" alt="" v-if="!$cookies.isKey('test')">
    <img src="@/assets/images/Authorized.svg" alt="" v-else>
</router-link>

</template>

<style scoped>
    
.box-btn{
    width: min(10vw, 100px);
    height: min(10vw, 100px);
    min-width: 50px;
    min-height: 50px;
    background-color: white;
    border-radius: 50%;
    border: 2px dashed black;
    transition: opacity 0.5s ease-in-out;

}

.box-btn img{
    max-width: 80%;
    max-height: 80%;
}

.box-btn:hover{
    opacity: 0.7;
}

.box-btn:active{
    opacity: 0.5;
}


</style>