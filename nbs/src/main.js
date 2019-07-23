import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import VCharts from 'v-charts'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import 'vue-loading-overlay/dist/vue-loading.css'

Vue.use(BootstrapVue)
Vue.use(VCharts)
Vue.use(ElementUI)

Vue.config.productionTip = false
Vue.prototype.$http = axios

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
