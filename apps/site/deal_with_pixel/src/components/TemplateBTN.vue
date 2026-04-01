<script setup>

defineProps({
    textButton: {
        default: 'Title button'
    },
    actionClick: {

    }
})

</script>

<template>

<button v-on:click="actionClick" class="button-style">
    <span class="button-text">
        {{ textButton }}
    </span>
</button>

</template>

<style scoped>
    
.button-style{
    width: 35vh;
    height: 8vh;
    border-radius: 10px;
    font-family: sunless-day;
    font-size: 5vh;
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

</style>