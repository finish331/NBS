<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
      For a guide and recipes on how to configure / customize this project,<br> check out the
      <a href="https://cli.vuejs.org"
         target="_blank"
         rel="noopener">vue-cli documentation</a>.
    </p>
    <h3>Installed CLI Plugins</h3>
    <ul>
      <li>
        <a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel"
           target="_blank"
           rel="noopener">babel</a>
      </li>
      <li>
        <a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint"
           target="_blank"
           rel="noopener">eslint</a>
      </li>
    </ul>
    <h3>Essential Links</h3>
    <ul>
      <li>
        <a href="https://vuejs.org"
           target="_blank"
           rel="noopener">Core Docs</a>
      </li>
      <li>
        <a href="https://forum.vuejs.org"
           target="_blank"
           rel="noopener">Forum</a>
      </li>
      <li>
        <a href="https://chat.vuejs.org"
           target="_blank"
           rel="noopener">Community Chat</a>
      </li>
      <li>
        <a href="https://twitter.com/vuejs"
           target="_blank"
           rel="noopener">Twitter</a>
      </li>
      <li>
        <a href="https://news.vuejs.org"
           target="_blank"
           rel="noopener">News</a>
      </li>
    </ul>
    <h3>Ecosystem</h3>
    <ul>
      <li>
        <a href="https://router.vuejs.org"
           target="_blank"
           rel="noopener">vue-router</a>
      </li>
      <li>
        <a href="https://vuex.vuejs.org"
           target="_blank"
           rel="noopener">vuex</a>
      </li>
      <li>
        <a href="https://github.com/vuejs/vue-devtools#vue-devtools"
           target="_blank"
           rel="noopener">vue-devtools</a>
      </li>
      <li>
        <a href="https://vue-loader.vuejs.org"
           target="_blank"
           rel="noopener">vue-loader</a>
      </li>
      <li>
        <a href="https://github.com/vuejs/awesome-vue"
           target="_blank"
           rel="noopener">awesome-vue</a>
      </li>
    </ul>
    <el-button type="primary"
               @click="getName">{{buttonText}}</el-button>
    <el-input v-model="inpContent"></el-input>
  </div>
</template>

<script>
import { db } from '../db'
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data () {
    return {
      buttonText: '123',
      inpContent: 'Test'
    }
  },
  methods: {
    getName () {
      this.$http.get('/api/test/testWhere', {
        params:{
          ID: '12345'
        }
      })
        .then((res) => {
          console.log('res',res) 
          this.inpContent = res.data.data2.date
        })
    },
    firebaseTest (){
      // db.collection('movies').doc('新世紀福爾摩').set({
      //   name: "新世紀福爾摩斯",
      //   date: "2010",
      //   desctiption: "本劇改編自阿瑟·柯南·道爾爵士家喻戶曉的推理小說，一位脾氣古怪的大偵探在現代倫敦的街頭悄悄巡行，四處搜尋線索。",
      //   actors: ["班尼迪克·康柏拜區", "馬丁·費曼"]
      // });
      console.log('success');
      db.collection('movies').doc('新世紀福爾摩').get().then(function(doc){
        console.log(doc.data().date);
      })
      
    }
  },
  firestore(){
    return {
     
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
