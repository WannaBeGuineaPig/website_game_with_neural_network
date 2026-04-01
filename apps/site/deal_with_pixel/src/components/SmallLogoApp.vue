<template>
    <Transition name="modal">
        <router-link to="/" class="logo-box d-flex justify-content-center align-items-center text-reset text-decoration-none">
            <img src="@/assets/images/logo.svg" alt="" class="logo-image me-1">
            <div class="d-flex flex-column  align-items-center">
                <div class="logo-text position-relative">DEAL</div>
                <div class="logo-text position-relative">WITH</div>
                <div class="small-text-logo logo-text position-relative">PIXEL</div>
            </div>
        </router-link>
    </Transition>
</template>

<style scoped>

.logo-box{
    max-width: 20vh;
    max-height: 10vh;
    transition: opacity 0.5s ease-in-out;
}

.logo-box div{
    transition: opacity 0.5s ease-in-out;
}

.logo-box:hover, .logo-box:hover div{
    opacity: 0.7;
}

.logo-box:active, .logo-box:hover div{
    opacity: 0.5;
}

.logo-text{
    display: inline;
    font-size: 4vh;
    font-family: sunless-day;
    letter-spacing: 5px;
}

.logo-text:first-child{
    top: 1vh;
}

.logo-text:nth-child(2){
    top: -2vh;
}

.small-text-logo{
    font-size: 1.5vh;
    top: -4vh;
}

.logo-image{
    max-height: 10vh;
    min-width: 40px;
    min-height: 40px;
}


@media (max-width: 1200px){
    .logo-text{
        display: none;
    }

    .logo-image{
        max-height: 7vh;
    }
}

@media (max-width: 600px){
    .logo-image{
        max-height: 5vh;
    }
}

</style>