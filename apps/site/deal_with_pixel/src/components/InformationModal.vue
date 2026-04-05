<script setup>

import AuthPerAccBTN from './AuthPerAccBTN.vue'

</script>

<template>

<div class="modal fade" id="projectInformationModal" tabindex="-1" aria-labelledby="projectInformationModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg modal-dialog-centered modal-dialog-scrollable">
    <div class="modal-content">
      <div class="modal-header">
        <h4 class="modal-title" id="projectInformationModalLabel">Справочная информация по сайту</h4>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Закрыть"></button>
      </div>
      <div class="modal-body">
        <h5>В чем суть проекта Deal With Pixel?</h5>
        <p class="text-indent-modal">Проект Deal with Pixel это веб-игра в которой лобби игроков рисуют на своём полотне заданную тематику. По истечению времени игроки смотрят каждую работы и модель нейронной сети показывает процент схожести на оригинал тематики. Побеждает игрок у которого больще всего процент схожести.</p>
        <h5 id="create-account">Как создать аккаунт?</h5>
        <div class="d-flex gap-2 align-items-center">
          <p class="text-indent-modal">В правом верхнем углу находится данная иконка -> </p>
          <AuthPerAccBTN :canClick="false" style="min-width: 50px; width: 50px; height: 50px;"/>
        </div>
        <p class="text-indent-modal">Нажав на данную иконку, вас перенаправит на страницу с авторизацией, на которой нужно нажать на кнопку '<a href="#">Нет аккаунта? Создать!</a>'.</p>
        <p class="text-indent-modal">После вы попадёте на страницу с регистрацией, введя корректные данные в поля, у вас создаться аккаунт!</p>
        <h5>Как начать рисовать?</h5>
        <p class="text-indent-modal">Чтобы начать рисовать, нужно выполнить следующие шаги:</p>
        <ol>
          <li>Войти в свой аккаунт. P.s. Если у вас нет аккаунта, необходимо его создать. <a href="#create-account" class="tooltip-test" title="Нажмите, для перехода">Инструкция по созданию аккаунта</a>;</li>
          <li>Нажать на кнопку 'Играть';</li>
          <li>Выбрать режим, дождаться других художников и начать соревнование.</li>
        </ol>
        <p class="text-indent-modal">Так же есть возможность порисовать в режиме 'Тренировка' без регистрации аккаунта. <br>Вот шаги, которые нужно предпринять:</p>
        <ol>
          <li>Нажать на кнопку 'Играть';</li>
          <li>Выбрать режим 'Тренировка'.</li>
        </ol>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
      </div>
    </div>
  </div>
</div>

</template>

<style scoped>
.text-indent-modal{
  text-indent: 5px;
  text-align: justify;
}
</style>