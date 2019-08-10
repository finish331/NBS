<template>
  <div id="leader_data_table">
    <v-container
      fluid
      grid-list-md
      style="padding:4% 0"
    >
      <v-data-iterator
        :items="items"
        :items-per-page.sync="itemsPerPage"
        :page="page"
        :search="search"
        :custom-filter="FilterPlayerData"
        :sort-by="sortBy.toUpperCase()"
        :sort-desc="sortDesc"
        hide-default-footer
      >
        <template v-slot:header>
          <v-toolbar
            dark
            color="#666666 darken-5"
            class="mb-1"
          >
            <v-text-field
              v-model="search"
              clearable
              flat
              solo-inverted
              hide-details
              prepend-inner-icon="search"
              label="Search"
            ></v-text-field>
            <template v-if="$vuetify.breakpoint.lgAndUp">  
              <v-spacer></v-spacer>
              <v-flex lg2 md3 d-flex>
                <v-select
                  v-model="nowSelectSeason"
                  :items="seasonFilter"
                  label="SEASON"
                  flat
                  outlined
                  hide-details
                  color="red"
                ></v-select>
              </v-flex>
              <v-spacer></v-spacer>
              <v-flex lg2 md3 d-flex>
                <v-select
                  v-model="nowSelectSeasonType"
                  :items="seasonTypeFilter"
                  label="SEASON TYPE"
                  flat
                  outlined
                  hide-details
                ></v-select>
              </v-flex>
              <v-spacer></v-spacer>
              <v-flex lg2 md3 d-flex>
                <v-select
                  v-model="nowSelectStatCategory"
                  :items="statCategoryFilter"
                  label="STAT CATEGORY"
                  flat
                  outlined
                  hide-details
                ></v-select>
              </v-flex>
              <v-spacer></v-spacer>
              <v-flex lg2 md3>
                <v-select
                  v-model="sortBy"
                  flat
                  solo-inverted
                  hide-details
                  :items="keys"
                  prepend-inner-icon="search"
                  label="Sort by"
                ></v-select>
              </v-flex>

              <v-spacer></v-spacer>
              <v-btn-toggle
                v-model="sortDesc"
                mandatory
              >
                <v-btn
                  large
                  depressed
                  color="#666666"
                  :value="false"
                >
                  <v-icon>keyboard_arrow_up</v-icon>
                </v-btn>
                <v-btn
                  large
                  depressed
                  color="#666666"
                  :value="true"
                >
                  <v-icon>arrow_downward</v-icon>
                </v-btn>
              </v-btn-toggle>
            </template>
          </v-toolbar>
        </template>
  
        <template v-slot:default="props">
          <v-layout
            wrap
          >
          <!-- 利用迴圈的方式產生card -->
          <!-- :為v-bind簡寫 -->
            <v-flex
              v-for="item in props.items"
              :key="item.name"
              xs12
              sm6
              md3
              lg2
            >
              <v-card @click="TestClick(item)">
                <v-card-title class="subheading font-weight-bold">James Harden</v-card-title>
                <!-- 分隔線 -->
                <v-divider></v-divider>
                <!-- 產生屬性 -->
                <v-list dense>
                  <v-list-item
                    v-for="(key, index) in filteredKeys"
                    :key="index"
                    :color="sortBy === key ? `blue lighten-4` : `white`"
                  >
                    <v-list-item-content>{{ key }}:</v-list-item-content>
                    <v-list-item-content class="align-end">{{ item[key.toUpperCase()] }}</v-list-item-content>
                  </v-list-item>
                </v-list>
              </v-card>
            </v-flex>
          </v-layout>
        </template>
  
        <template v-slot:footer>
          <v-layout mt-2 wrap align-center justify-center>
            <span class="grey--text">Items per page</span>
            <v-menu offset-y>
              <template v-slot:activator="{ on }">
                <v-btn
                  dark
                  text
                  color="#666666"
                  class="ml-2"
                  v-on="on"
                >
                  {{ itemsPerPage }}
                  <v-icon>keyboard_arrow_down</v-icon>
                </v-btn>
              </template>
              <v-list>
                <v-list-item
                  v-for="(number, index) in itemsPerPageArray"
                  :key="index"
                  @click="updateItemsPerPage(number)"
                >
                  <v-list-item-title>{{ number }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
  
            <v-spacer></v-spacer>
  
            <span
              class="mr-4
              grey--text"
            >
              Page {{ page }} of {{ numberOfPages }}
            </span>
            <v-btn
              fab
              dark
              color="#666666 darken-3"
              class="mr-1"
              @click="formerPage"
              style="height:40px; width:40px"
            >
              <v-icon>keyboard_arrow_left</v-icon>
            </v-btn>
            <v-btn
              fab
              dark
              color="#666666 darken-3"
              class="ml-1"
              @click="nextPage"
              style="height:40px; width:40px"
            >
              <v-icon>keyboard_arrow_right</v-icon>
            </v-btn>
          </v-layout>
        </template>
      </v-data-iterator>
    </v-container>
    <!-- 球員彈跳視窗 -->
    <div class="text-center">
      <v-dialog
        v-model="dialog"
        width="500"
      >
        <v-card>
          <v-card-title class="subheading font-weight-bold">James Harden</v-card-title>
          <!-- 分隔線 -->
          <v-divider></v-divider>
          <!-- 產生屬性 -->
          <v-list dense>
            <v-list-item
              v-for="(key, index) in filteredKeys"
              :key="index"
              :color="sortBy === key ? `blue lighten-4` : `white`"
            >
              <v-list-item-content>{{ key }}:</v-list-item-content>
              <v-list-item-content class="align-end">{{ dialogItem[key.toUpperCase()] }}</v-list-item-content>
            </v-list-item>
          </v-list>
        </v-card>
        <!-- <v-card :item="dialogItem">
          <v-card-title
            class="headline grey lighten-2"
            primary-title
          >
            {{dialogItem.name}}
          </v-card-title>
  
          <v-card-text>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
          </v-card-text>
  
          <v-divider></v-divider>
  
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="primary"
              text
              @click="dialog = false"
            >
              I accept
            </v-btn>
          </v-card-actions>
        </v-card> -->
      </v-dialog>
    </div>
  </div>
</template>

<script>
import playerData from "@/assets/playerData.json";

export default {
  components: {},
  // 接來自父層傳遞的參數
  props:['test','test2'],
  mounted: function(){
    console.log(this.test);
    console.log(this.test2);
  },
  data(){
    return{
      dialog: false,
      itemsPerPageArray: [6, 12, 18],
      search: '',
      filter: {},
      sortDesc: false,
      page: 1,
      itemsPerPage: 6,
      sortBy: 'name',
      keys: [
        'Season',
        'AGE',
        'PTS',
        'TRB',
        'AST',
        '3PA',
        '3P%',
        '2PA',
        '2P%',
      ],
      // Select的資料
      nowSelectSeason: '2018-19',
      seasonFilter: [
        { value: '2018-19', text:'2018-2019' },
        { value: '2017-18', text:'2017-2018' },
        { value: '2016-17', text:'2016-2017' }
      ],
      nowSelectSeasonType: { value: '0', text:'Regular Season' },
      seasonTypeFilter: [
        { value: '0', text:'Regular Season' },
        { value: '1', text:'Playoffs' },
      ],
      nowSelectStatCategory: { value: '0', text:'PTS' },
      statCategoryFilter: [
        { value: '0', text:'PTS' },
        { value: '1', text:'EFF' },
        { value: '2', text:'TOV' },
        { value: '3', text:'BLK' },
        { value: '4', text:'AST' },
        { value: '5', text:'STL' },
      ],
      dialogItem:[],
      items:[],
      temp: playerData
    };
  },
  computed:{
    numberOfPages () {
      return Math.ceil(this.items.length / this.itemsPerPage)
    },
    // 把Name以外的屬性列出來
    filteredKeys () {
      return this.keys.filter(key => key !== `Name`)
    },
    cloneLeaderSelect: {
      get: function(){
        return this.nowSelectSeason;
      },
      set: function(a){
        this.nowSelectSeason = a
      }

    }
  },
  methods:{
    nextPage () {
      if (this.page + 1 <= this.numberOfPages) this.page += 1
    },
    formerPage () {
      if (this.page - 1 >= 1) this.page -= 1
    },
    updateItemsPerPage (number) {
      this.itemsPerPage = number
    },
    FilterPlayerData (){
      for(var key in this.temp){
        // if(this.nowSelectSeason == this.temp[key].Season){
          this.items.push(this.temp[key])
        // }
      }
      console.log(this.items)
      return this.items
    },
    TestClick(output){
      this.dialog = true;
      this.dialogItem = output;
      console.log(this.dialogItem);
    }
    
  }
}
</script>



