<template>
  <div class = "hello">
    <v-app id="inspire">
      <v-container 
        fluid grid-list-xl 
        class="select-filter"
        style="padding:5% 0 0 0"
        v-if="$vuetify.breakpoint.mdAndDown"
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
              v-model="nowSelectStateCategory"
              :items="stateCategoryFilter"
              label="STAT CATEGORY"
              outlined
            ></v-select>
          </v-flex>
        </v-layout>
      </v-container>
      <!-- 將select的值帶入DataTable中，供grid篩選用 -->
      <DataTable :test="nowSelectSeason" :test2="nowSelectSeasonType" />
    </v-app>
  </div>
</template>

<script>
import DataTable from '../components/LeaderDataTable'
export default {
  components: {DataTable},
  data(){
    return{
      nowSelectSeason: '2018-19',
      seasonFilter: [
        { value: '2018-19', text:'2018-2019' },
        { value: '2017-18', text:'2017-2018' },
        { value: '2016-17', text:'2016-2017' }
      ],
      nowSelectSeasonType: '0',
      seasonTypeFilter: [
        { value: '0', text:'Regular Season' },
        { value: '1', text:'Playoffs' },
      ],
      nowSelectStateCategory: '0',
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

  #inspire {
    background-color: white;
  }
</style>

<style scoped>
  #inspire >>> .container{
  }
</style>


