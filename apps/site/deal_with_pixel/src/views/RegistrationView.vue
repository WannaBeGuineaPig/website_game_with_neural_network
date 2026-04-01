<script setup>

import Complete from '@/assets/images/Complete.svg'
import Important from '@/assets/images/Important.svg'
import Cancel from '@/assets/images/Cancel.svg'
import SmallLogoApp from '../components/SmallLogoApp.vue'
import AuthPerAccBTN from '../components/AuthPerAccBTN.vue'
import TemplateBTN from '../components/TemplateBTN.vue'
import TemplateInputField from '../components/TemplateInputField.vue'

document.title = 'Deal With Pixel - Регистрация';

function showAlert(textAlert, typeAlert = 'success', checkMark = Complete) {
    const alertContainer = document.getElementById('alert-container');
    alertContainer.innerHTML = '';
    const wrapper = document.createElement('div');
    wrapper.innerHTML = `
        <div class="alert alert-${typeAlert} alert-dismissible fade show" role="alert">
            <img src="${checkMark}" style="width: 40px;"/>
            ${textAlert}
            <button type="button" class="btn-close" style="height: 50%;" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    `;
    alertContainer.appendChild(wrapper);

    setTimeout(() => {
        wrapper.remove()
    }, 5000); 
}

function logInAccount() {
    showAlert('САЛАМ');
}

</script>

<template>

<AuthPerAccBTN class="position-absolute end-0 top-0 m-xl-4 m-lg-3 m-2"/>
<SmallLogoApp  class="position-absolute start-0 top-0 mt-xl-3 mt-lg-2 ms-lg-1 mt-md-2 ms-md-2"/>

<div class="container-lg h-100 d-flex justify-content-center">

    <!-- Блок для добавления уведомлений -->

    <div id="alert-container" class="position-absolute" style="left: 20%; width: 60%;"></div>

    <!--  -->

    <div class="col-sm-4 col-md-8 col-lg-10 d-flex align-items-center flex-column justify-content-evenly">
        <div class="text-center">
            <h1 class="title-auth main-font-family">Регистрация</h1>
            <div class="box-info d-flex align-items-center justify-content-center main-font-family">
                <p class="main-font-family" style="letter-spacing: 3px;">Чтобы создать аккаунт, необходимо заполнить поля ниже </p>
                <img src="@/assets/images/Down.svg" alt="">
            </div>
        </div>

        <form action="" @submit.prevent="logInAccount" class="d-flex flex-column align-items-center justify-content-between" style="height: 60%; width: max(60%, 225px);">
            
            <TemplateInputField idInputField="MailIF" placeholderInputField="Введите почту" labelText="Почта" />
            
            <TemplateInputField idInputField="LoginIF" placeholderInputField="Введите логин" labelText="Логин" />
            
            <TemplateInputField idInputField="PasswordIF" placeholderInputField="Введите пароль" labelText="Пароль" typeInputField="password" />
            
            <div class="w-100 d-flex justify-content-between">
                <p></p>
                <router-link to="/authorization" class="link-text text-decoration-none text-center main-font-family">Есть аккаунт? Войти!</router-link>
            </div>

            <div style="width: max(40%, 175px);" class="mt-5">
                <TemplateBTN textButton="Войти" />
            </div>
            
        </form>

    </div>
        
</div>

</template>

<style scoped>
    
#alert-container{
    left: 45%;
    top: 1%;
}

.title-auth{
    font-size: 4rem;
    letter-spacing: 5px;
}

.box-info p{
    font-size: 2rem;
    margin-bottom: 0;
}

.box-info img{
    max-width: 40px;
}

.link-text{
    letter-spacing: 2px;
    font-size: large;
}

@media (max-width: 1000px) {
    .link-text{
        font-size: small;
    }
}

@media (max-width: 500px) {
    .title-auth{
        font-size: 3rem;
    }
    .box-info p{
        font-size: 1rem;
    }
    
    .box-info img{
        max-width: 20px;
    }

    .link-text{
        font-size: small;
    }
}

@media (max-width: 400px){
    .title-auth{
        font-size: 2.5rem;
    }
    
    .box-info p{
        font-size: 14px;
    }
    
    .link-text{
        font-size: x-small;
    }
}

</style>