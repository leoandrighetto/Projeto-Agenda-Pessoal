import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

//Router
import router from './router/index.js'

//Vuetify
import vuetify from './vuetify/index.js'

//Pinia
import pinia from './pinia/index.js'

const app = createApp(App)

app.use(router)
app.use(vuetify)
app.use(pinia)
app.mount('#app')