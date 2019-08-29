import Vue from 'vue'
import Router from 'vue-router'
import TestView from './components/HelloWorld.vue'
import Home from './views/Home.vue'
import Player from './views/Player.vue'
import Leader from './views/Leader.vue'
import Champion from './views/Champion.vue'
import CompareLeader from './views/ComparePlayer.vue'
import Map from './views/map.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/test',
      name: 'test',
      component: TestView
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
      path :'/Champion',
      name :'Champion',
      component:Champion
    },
    {
      path: '/compare',
      name: 'Compare',
      component: CompareLeader
    },
    {
      path: '/map',
      name: 'Map',
      component: Map
    }
  ]
})
