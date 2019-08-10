import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Player from './views/Player.vue'
import Leader from './views/Leader.vue'
import CompareLeader from './views/ComparePlayer.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (about.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    // },
    {
      path: '/player',
      name: 'Player',
      component: Player
    },
    {
      path: '/leader',
      name: 'Leader',
      component: Leader
    },
    {
      path: '/compare',
      name: 'Compare',
      component: CompareLeader
    }
  ]
})
