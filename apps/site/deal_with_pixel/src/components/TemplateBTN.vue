<script setup>

defineProps({
    textButton: {
        default: 'Текст кнопки'
    },
    actionClick: {
        
    },
})

</script>

<template>

<button v-on:click="actionClick" class="button-style w-100">
    <span class="button-text">
        {{ textButton }}
    </span>
</button>

</template>

<style scoped>
    
.button-style{
    height: 6vh;
    font-size: xx-large;
    border-radius: 10px;
    font-family: sunless-day;
    letter-spacing: 5px;
    background-color: white;
    transition: background-color 0.5s ease-in-out;
}

.button-style:hover{
    background-color: rgb(240, 225, 205);

}

.button-style:active{
    background-color: wheat;
}

.button-text{
    color: transparent;
    background-clip: text;
    background-image: var(--main-color);
}

@media (max-width: 400px){
    .button-style{
        font-size: x-large;
    }
}

</style>