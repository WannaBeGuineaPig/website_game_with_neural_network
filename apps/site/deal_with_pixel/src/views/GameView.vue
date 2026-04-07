<script setup>

import router from '@/router';
import { ref, inject } from 'vue'

document.title = 'Deal With Pixel - Игра';

const windowHeigth = ref(window.innerHeight);
const windowWidth = ref(window.innerWidth * 0.8);
const $cookies = inject('$cookies');
const gameSetting = $cookies.get('gameSetting');

function resize() {
    windowHeigth.value = window.innerHeight;
    windowWidth.value = window.innerWidth * 0.8;

}
window.addEventListener('resize', resize);

</script>

<script>

export default{
    data() {
        return {
            mouse: { x:0, y:0},
            draw: false,
            canvas: null,
            ctx: null,
            isEraser: false,
            backgroundColorEraser: ref('white')
        }
    },

    methods: {
        startDrawing(e){
            if (e.touches == undefined){
                this.mouse.x = e.pageX - this.canvas.offsetLeft;
                this.mouse.y = e.pageY - this.canvas.offsetTop;
            }
            else{
                this.mouse.x = e.touches[0].clientX - this.canvas.offsetLeft;
                this.mouse.y = e.touches[0].clientY - this.canvas.offsetTop;    
            }
            this.draw = true;
            this.ctx.beginPath();
            this.ctx.moveTo(this.mouse.x, this.mouse.y);
        },

        drawing(e){
            if(this.draw == true){
                if (e.touches == undefined){
                    this.mouse.x = e.pageX - this.canvas.offsetLeft;
                    this.mouse.y = e.pageY - this.canvas.offsetTop;
                }
                else{
                    this.mouse.x = e.touches[0].clientX - this.canvas.offsetLeft;
                    this.mouse.y = e.touches[0].clientY - this.canvas.offsetTop;    
                }
                this.ctx.lineTo(this.mouse.x, this.mouse.y);
                this.ctx.stroke();
            }
        },

        stopDrawing(e) {
            this.mouse.x = e.pageX - this.canvas.offsetLeft;
            this.mouse.y = e.pageY - this.canvas.offsetTop;
            this.ctx.lineTo(this.mouse.x, this.mouse.y);
            this.ctx.stroke();
            this.ctx.closePath();
            this.draw = false;
        },

        stopDrawingTouch(e) {
            this.ctx.lineTo(this.mouse.x, this.mouse.y);
            this.ctx.stroke();
            this.ctx.closePath();
            this.draw = false;
        },

        clearCanvas(e){
            if(this.isEraser){
                this.backgroundColorEraser = 'white';
                this.ctx.globalCompositeOperation = 'source-over';
                this.isEraser = !this.isEraser;
            }
            this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        },

        leaveGame(e){
            const rangeInput = document.getElementById('sizeBrush');
            const rangeOutput = document.getElementById('sizeBrushValue');
            rangeInput.value = 1;
            rangeOutput.textContent = rangeInput.value;
            router.push('/');
        },

        changeEraserStatus(){
            if(this.isEraser){
                this.backgroundColorEraser = 'white';
                this.ctx.globalCompositeOperation = 'source-over';
            }
            else{
                this.backgroundColorEraser = 'greenyellow';
                this.ctx.globalCompositeOperation = 'destination-out';
            }
            this.isEraser = !this.isEraser;
        }
        
    },

    mounted(){
        this.canvas = document.getElementById("сanvasDrawing");
        this.ctx = this.canvas.getContext("2d");
        this.ctx.lineWidth = 1;
    }
}


</script>

<template>
    <div class="background-canvas position-absolute end-0 h-100"></div>
    <canvas 
    class="position-absolute end-0" 
    id="сanvasDrawing"  
    v-on:mousedown="startDrawing" 
    v-on:touchstart="startDrawing"
    v-on:mousemove="drawing" 
    v-on:touchmove="drawing"
    v-on:mouseup="stopDrawing"
    v-on:touchend="stopDrawingTouch" 
    v-on:mouseleave="() => this.draw = false"
    :width="windowWidth" 
    :height="windowHeigth"
    ></canvas>

    <div class="position-absolute start-0 bottom-0 h-75 d-flex flex-column align-items-center justify-content-center" style="width: 19%;">

        <button class="canvas-button d-flex align-self-center align-items-center justify-content-center" data-bs-toggle="modal" data-bs-target="#setTypeImage" title="Нажмите, для предсказания типа изображения">
            <img src="../assets/images/Info.svg" alt="">
        </button>

        <div class="w-100 d-flex flex-column justify-content-center gap-5" style="height: 70%;">
            
            <button class="canvas-button d-flex align-self-center align-items-center justify-content-center" data-bs-toggle="modal" data-bs-target="#setSizeBrush">
                <img src="../assets/images/PaintBrush.svg" alt="">
            </button>
            <button id="eraserBTN" class="canvas-button d-flex align-self-center align-items-center justify-content-center" v-on:click="changeEraserStatus" :style="{ backgroundColor: backgroundColorEraser}">
                <img src="../assets/images/Eraser.svg" alt="">
            </button>
            <button class="canvas-button d-flex align-self-center align-items-center justify-content-center" v-on:click="clearCanvas">
                <img src="../assets/images/Trash.svg" alt="">
            </button>
        </div>

        <button class="canvas-button d-flex align-self-center align-items-center justify-content-center" v-on:click="leaveGame" title="Нажмите, для выхода">
            <img src="../assets/images/Logout.svg" alt="">
        </button>

    </div>

</template>

<style scoped>
    
.background-canvas {
    width: 81%;
    background: url(../assets/images/canvasBackground.svg) white;
    background-size: cover;
    
}

.canvas-button{
    width: 80px;
    height: 80px;
    border-radius: 50%;
    border: 2px dashed black;
    background-color: white;
    transition: background-color 0.2s ease;
}

.canvas-button:hover{
    background-color: whitesmoke;
}

.canvas-button:active{
    background-color: wheat;
}

.canvas-button img{
    max-height: 80%;
}

@media (max-width: 500px){
    .canvas-button{
        width: 60px;
        height: 60px;
    }
}

@media (max-width: 400px){
    .canvas-button{
        width: 50px;
        height: 50px;
    }
}

</style>

