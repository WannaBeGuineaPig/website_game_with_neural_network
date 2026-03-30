<template>
    <div class="logo-box d-flex align-items-center">
        <img src="@/assets/images/logo.svg" alt="" class="logo-image mx-3">
        <div class="d-flex flex-column justify-content-between">
            <p class="logo-text position-relative z-3">DEAL</p>
            <p class="logo-text position-relative z-2">WITH</p>
            <p class="small-text-logo logo-text position-relative text-center z-1">PIXEL</p>
        </div>
    </div>
</template>

<style scoped>

.logo-text{
    font-size: min(15vw, 80px);
    font-family: sunless-day;
    letter-spacing: 5px;
}

.logo-text:first-child{
    top: 60px;
}

.logo-text:nth-child(2){
    top: -10px;
}

.small-text-logo{
    font-size: 25px;
    top: -65px;
}

.logo-image{
  max-width: 25vw;
}

@media (max-width: 500px){
    .small-text-logo{
        top: -50px;
        font-size: 20px;
    }

    .logo-text:nth-child(2){
        top: 0px;
    }
}

</style>