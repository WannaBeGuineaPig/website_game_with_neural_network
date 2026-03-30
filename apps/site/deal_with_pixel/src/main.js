import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import VueCookies from 'vue-cookies';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import './assets/styles/base.css'

const app = createApp(App)

app.use(router)
app.use(VueCookies, { expires: '7d' });

app.mount('#app')
