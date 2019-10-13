<template>
  <div class = "hello px-5">
    <v-app id="inspire">
      <v-container
        fluid grid-list-xl
        class="select-filter"
        style="padding:5% 0 0 0"
        v-if="$vuetify.breakpoint.mdAndDown"
      >
        <v-layout wrap align-center>
          <!-- <v-flex xs12 sm6 md3 d-flex class="select-season">
            <v-select
              v-model="nowSelectSeason"
              :items="seasonFilter"
              item-text="text"
              item-value="value"
              label="SEASON"
              outlined
              color="blue"
              height= 60px
              v-on:change="changeData"
            ></v-select>
          </v-flex> -->

          <!-- <v-flex xs12 sm6 md3 d-flex>
            <v-select
              v-model="nowSelectSeasonType"
              :items="seasonTypeFilter"
              item-text="text"
              item-value="value"
              label="SEASON TYPE"
              outlined
            ></v-select>
          </v-flex> -->

          <!-- <v-flex xs12 sm6 md3 d-flex>
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
          </v-flex> -->
          <!-- <v-flex lg2 md3>
            <v-select
              v-model="sortBy"
              flat
              solo-inverted
              hide-details
              :items="keys"
              prepend-inner-icon="search"
              label="Sort by"
            ></v-select>
          </v-flex> -->
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
        { value: 'Career', text:'Career' },
        { value: '2018-19', text:'2018-2019' },
        { value: '2017-18', text:'2017-2018' },
        { value: '2016-17', text:'2016-2017' },
        { value: '2015-16', text:'2015-2016' },
        { value: '2014-15', text:'2014-2015' },
        { value: '2013-14', text:'2013-2014' },
        { value: '2012-13', text:'2012-2013' },
        { value: '2011-12', text:'2011-2012' },
        { value: '2010-11', text:'2010-2011' },
        { value: '2009-10', text:'2009-2010' },
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
    changeData(){
      // console.log(this.nowSelectSeason)
    }
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
