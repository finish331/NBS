<template>
  <div class = "hello">
    <v-app id="inspire">
      <v-container fluid grid-list-xl class="select-filter">
        <v-layout wrap align-center>
          <v-flex xs12 sm6 md3 d-flex class="select-season">
            <v-select
              v-model="nowSelectSeason"
              :items="items"
              item-text="text"
              item-value="value"
              label="SEASON"
              outlined
              color="#F44336"
              height= 60px
            ></v-select>
          </v-flex>

          <v-flex xs12 sm6 md3 d-flex>
            <v-select
              :items="items"
              label="SEASON TYPE"
              outlined
            ></v-select>
          </v-flex>

          <v-flex xs12 sm6 md3 d-flex>
            <v-select
              :items="items"
              label="STAT CATEGORY"
              outlined
            ></v-select>
          </v-flex>

          <v-flex xs12 sm6 md3 d-flex>
            <v-select
              :items="items"
              label="STAT CATEGORY"
              outlined
            ></v-select>
          </v-flex>

        </v-layout>
      </v-container>
    </v-app>
  </div>
</template>

<script>
export default {
  components: {},
  data(){
    return{
      nowSelectSeason: { value: '2018-2019', text:'2018-2019' },
      items: [
        { value: '2018-2019', text:'2018-2019' },
        { value: '2017-2018', text:'2017-2018' },
        { value: '2016-2017', text:'2016-2017' }
      ],
    };
  },
  methods:{

  }
}
</script>

<style>
  .select-season{
    width: 300%;
  }
</style>

<style scoped>
  #inspire >>> .container{
    padding: 100px;
  }
</style>


