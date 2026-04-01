<template>
    <div class="logo-box d-flex justify-content-center align-items-center">
        <img src="@/assets/images/logo.svg" alt="" class="logo-image mx-3">
        <div class="d-flex flex-column  align-items-center">
            <div class="logo-text position-relative">DEAL</div>
            <div class="logo-text position-relative">WITH</div>
            <div class="small-text-logo logo-text position-relative">PIXEL</div>
        </div>
    </div>
</template>

<style scoped>

.logo-box{
    width: 35vh;
    height: 30vh;
}

.logo-text{
    display: inline;
    font-size: 8vh;
    font-family: sunless-day;
    letter-spacing: 5px;
}

.logo-text:first-child{
    top: 4vh;
}

.logo-text:nth-child(2){
    top: -2vh;
}

.small-text-logo{
    font-size: 3.5vh;
    top: -6vh;
}

.logo-image{
  max-width: 25vw;
}

</style>