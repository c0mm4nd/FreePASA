'use strict'

import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App.vue'

import axios from 'axios'
Vue.prototype.$http = axios
// import utils from "./utils"

Vue.use(ElementUI)

var vm = new Vue({
  el: '#app',
  render: h => h(App),
})

