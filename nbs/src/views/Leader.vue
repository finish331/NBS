<template>
  <div class = "hello">
    <v-app id="inspire">
      <v-container 
        fluid grid-list-xl 
        class="select-filter"
        style="padding:40px 100px"
      >
        <v-layout wrap align-center>
          <v-flex xs12 sm6 md3 d-flex class="select-season">
            <v-select
              v-model="nowSelectSeason"
              :items="seasonFilter"
              item-text="text"
              item-value="value"
              label="SEASON"
              outlined
              color="blue"
              height= 60px
            ></v-select>
          </v-flex>

          <v-flex xs12 sm6 md3 d-flex>
            <v-select
              v-model="nowSelectSeasonType"
              :items="seasonTypeFilter"
              item-text="text"
              item-value="value"
              label="SEASON TYPE"
              outlined
            ></v-select>
          </v-flex>

          <v-flex xs12 sm6 md3 d-flex>
            <v-select
              v-model="nowSelectStateCategory"
              :items="stateCategoryFilter"
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
      <DataTable/>
    </v-app>
  </div>
</template>

<script>
import DataTable from '../components/LeaderDataTable'
export default {
  components: {DataTable},
  data(){
    return{
      nowSelectSeason: { value: '2018-2019', text:'2018-2019' },
      seasonFilter: [
        { value: '2018-2019', text:'2018-2019' },
        { value: '2017-2018', text:'2017-2018' },
        { value: '2016-2017', text:'2016-2017' }
      ],
      nowSelectSeasonType: { value: '0', text:'Regular Season' },
      seasonTypeFilter: [
        { value: '0', text:'Regular Season' },
        { value: '1', text:'Playoffs' },
      ],
      nowSelectStateCategory: { value: '0', text:'PTS' },
      stateCategoryFilter: [
        { value: '0', text:'PTS' },
        { value: '1', text:'EFF' },
        { value: '2', text:'TOV' },
        { value: '3', text:'BLK' },
        { value: '4', text:'AST' },
        { value: '5', text:'STL' },
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


