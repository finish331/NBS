import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import VCharts from 'v-charts'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import ElementUI from 'element-ui'
import VueFirestore from 'vue-firestore'
import 'element-ui/lib/theme-chalk/index.css'
import 'vue-loading-overlay/dist/vue-loading.css'
import vuetify from './plugins/vuetify';
import '@/assets/scss/global.scss'
import 'firebase/firestore'

Vue.use(BootstrapVue)
Vue.use(VCharts)
Vue.use(ElementUI)
Vue.use(VueFirestore)

Vue.config.productionTip = false
Vue.prototype.$http = axios

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
