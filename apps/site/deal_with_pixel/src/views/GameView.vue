<script setup>

import { ref } from 'vue'

document.title = 'Deal With Pixel - Игра';

const windowHeigth = ref(window.innerHeight);
const windowWidth = ref(window.innerWidth * 0.8);


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
        }
    },

    methods: {
        startDrawing(e){
            this.mouse.x = e.pageX - this.canvas.offsetLeft;
            this.mouse.y = e.pageY - this.canvas.offsetTop;
            this.draw = true;
            this.ctx.beginPath();
            this.ctx.moveTo(this.mouse.x, this.mouse.y);
        },

        drawing(e){
            if(this.draw == true){
                this.mouse.x = e.pageX - this.canvas.offsetLeft;
                this.mouse.y = e.pageY - this.canvas.offsetTop;
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
        }
    },

    mounted(){
        this.canvas = document.getElementById("сanvasDrawing");
        this.ctx = this.canvas.getContext("2d");
    }
}


</script>

<template>
    <canvas class="position-absolute end-0" id="сanvasDrawing" v-on:touchend="" v-on:mousedown="startDrawing" v-on:mousemove="drawing" v-on:mouseup="stopDrawing" :width="windowWidth" :height="windowHeigth"></canvas>

</template>

<style scoped>
    
#сanvasDrawing {
    background-color: white;
    /* background: url(../assets/images/canvasBackground.svg);
    background-repeat: no-repeat; */
    
}

</style>

