import App from './App'

import uView from '@/uni_modules/uview-ui'
// import { Form, Field, CellGroup } from 'vant'
Vue.use(uView)
// #ifndef VUE3
import Vue from 'vue'

import tmVuetify from "./tm-vuetify";
Vue.use(tmVuetify)

Vue.config.productionTip = false
App.mpType = 'app'
const app = new Vue({
    ...App
})




app.$mount()
// app.use(Form)
// #endif

// #ifdef VUE3
import { createSSRApp } from 'vue'
export function createApp() {
  const app = createSSRApp(App)
  return {
    app
  }
}
// #endif