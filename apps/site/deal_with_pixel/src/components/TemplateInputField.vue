<script setup>

const props = defineProps({
    idInputField: {
        required: true
    },
    typeInputField: {
        default: 'text'
    },
    placeholderInputField: {
        default: 'Текст подсказки'
    },
    labelText: {
        default: 'Текст метки'
    },
    isRequired: {
        default: true
    },
    maxLengthInputField: {
        default: 200
    }
})


</script>

<template>
    <div class="w-100">
        <label :for="idInputField" class="form-label">{{ labelText }}</label>
        <input :type="typeInputField" class="form-control me-1" :id="idInputField" :placeholder="placeholderInputField" :required="isRequired" :maxlength="maxLengthInputField">
    </div>
</template>

<style scoped>

input{
    text-indent: 5px;
    border: 1px solid black;
}

input::placeholder{
    color: transparent;
    background-clip: text;
    background-image: var(--main-color);
}

label, input{
    font-size: x-large;
    font-family: sunless-day;
    letter-spacing: 3px;
}

@media (max-width: 500px){
    label, input{
        font-size: large;
    }
}

</style>