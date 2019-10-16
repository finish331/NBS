<template>
  <div id="leader_data_table">
    <v-container fluid grid-list-md style="padding:4% 0">
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
          <!-- <v-toolbar dark color="#666666 darken-5" class="md-1 vtoolbar" > -->
          <div style="padding:2.5%;background:rgb(29, 29, 29);display:flex;align-items:center">
            <template>
              <v-layout wrap>
                <!-- <v-spacer></v-spacer> -->
                <v-flex lg4 md3 sm2 xs12 d-flex>
                  <v-select
                    dark
                    v-model="nowSelectSeason"
                    :items="seasonFilter"
                    label="SEASON"
                    flat
                    solo-inverted
                    hide-details
                    color="blue"
                    v-on:change="changeData"
                  ></v-select>
                </v-flex>
                <v-spacer></v-spacer>
                <v-flex lg4 md3 sm4 xs12>
                  <v-select
                    dark
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
                <v-btn-toggle dark v-model="sortDesc" mandatory style="background:rgb(29, 29, 29);">
                  <v-btn large depressed color="#666666" :value="false">
                    <v-icon>keyboard_arrow_up</v-icon>
                  </v-btn>
                  <v-btn large depressed color="#666666" :value="true">
                    <v-icon>keyboard_arrow_down</v-icon>
                  </v-btn>
                </v-btn-toggle>
                <!-- <v-spacer></v-spacer> -->
              </v-layout>
            </template>
          </div>
          <!-- </v-toolbar> -->
        </template>

        <template v-slot:default="props">
          <v-layout wrap>
            <!-- 利用迴圈的方式產生card -->
            <!-- :為v-bind簡寫 -->
            <v-flex v-for="item in props.items" :key="item.name" xs12 sm6 md3 lg2>
              <v-card @click="TestClick(item)">
                <v-card-title
                  class="subheading font-weight-bold"
                  style="font-size:20px;height:200px "
                >
                  <div style="height:40%;width:100%">{{item.name}}</div>
                  <div style="height:60%;width:100%">
                    <img :src="item.pic_url" height="100%" />
                  </div>
                </v-card-title>
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
                <v-btn dark text color="#666666" class="ml-2" v-on="on">
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

            <span class="mr-4 grey--text">Page {{ page }} of {{ numberOfPages }}</span>
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
    <div class="text-center" v-if="showPlayer">
      <v-dialog v-model="dialog" width="100%">
        <v-card>
          <Player :player="playerData[indexTemp]" @close="parentClose" />
        </v-card>
      </v-dialog>
    </div>
  </div>
</template>

<style>
.vtoolbar {
  padding: 2.5%;
}
@media (max-width: 599px) {
  .vtoolbar {
    padding: 15% 2.5%;
  }
}
</style>
<script>
import playerData from "@/assets/json/player.json";
import Player from "../views/Player";
export default {
  components: { Player },
  // 接來自父層傳遞的參數
  props: ["test", "test2"],
  mounted: function() {
    // console.log(this.test);
    this.changeData();
  },
  data() {
    return {
      indexTemp: "",
      showPlayer: false,
      name: "",
      dialog: false,
      itemsPerPageArray: [6, 12, 18],
      search: "",
      filter: {},
      sortDesc: false,
      page: 1,
      itemsPerPage: 6,
      sortBy: "name",
      keys: ["PTS", "TRB", "AST", "3PA", "3P%", "2PA", "2P%"],
      // Select的資料
      nowSelectSeason: "Career",
      seasonFilter: [
        { value: "Career", text: "Career" },
        { value: "2018-19", text: "2018-2019" },
        { value: "2017-18", text: "2017-2018" },
        { value: "2016-17", text: "2016-2017" },
        { value: "2015-16", text: "2015-2016" },
        { value: "2014-15", text: "2014-2015" },
        { value: "2013-14", text: "2013-2014" },
        { value: "2012-13", text: "2012-2013" },
        { value: "2011-12", text: "2011-2012" },
        { value: "2010-11", text: "2010-2011" },
        { value: "2009-10", text: "2009-2010" }
      ],
      nowSelectSeasonType: { value: "0", text: "Regular Season" },
      seasonTypeFilter: [
        { value: "0", text: "Regular Season" },
        { value: "1", text: "Playoffs" }
      ],
      nowSelectStatCategory: { value: "0", text: "PTS" },
      statCategoryFilter: [
        { value: "0", text: "PTS" },
        { value: "1", text: "EFF" },
        { value: "2", text: "TOV" },
        { value: "3", text: "BLK" },
        { value: "4", text: "AST" },
        { value: "5", text: "STL" }
      ],
      dialogItem: [],
      items: [],
      temp: [],
      playerData: playerData
    };
  },
  watch: {
    dialog(val) {
      !val && setTimeout(this.setShowPlayerF, 250);
    }
  },
  computed: {
    numberOfPages() {
      return Math.ceil(this.items.length / this.itemsPerPage);
    },
    // 把Name以外的屬性列出來
    filteredKeys() {
      return this.keys.filter(key => key !== "Name");
    },
    cloneLeaderSelect: {
      get: function() {
        return this.nowSelectSeason;
      },
      set: function(a) {
        this.nowSelectSeason = a;
      }
    }
  },
  methods: {
    changeData() {
      this.items = [];
      // console.log(this.nowSelectSeason)
      this.temp = [];
      var dataTemp = [];
      var i;
      var j;
      var state;
      var index;
      var indexTemp;
      var temp1;
      var temp2;
      var temp3;
      var temp4;
      var temp5;
      var temp6;
      var temp7;
      for (i = 0; i < this.playerData.length; i++) {
        index = 0;
        temp1 = 0;
        temp2 = 0;
        temp3 = 0;
        temp4 = 0;
        temp5 = 0;
        temp6 = 0;
        temp7 = 0;
        state = 0;
        if (this.playerData[i]["data"] != undefined) {
          for (
            j = 0;
            j < Object.keys(this.playerData[i].data.Season).length;
            j++
          ) {
            if (this.playerData[i].data.Season[j] == this.nowSelectSeason) {
              state = 1;
              indexTemp = i;
              index++;
              temp1 += Number(this.playerData[i].data.PTS[j]);
              temp2 += Number(this.playerData[i].data.TRB[j]);
              temp3 += Number(this.playerData[i].data.AST[j]);
              temp4 += Number(this.playerData[i].data["3PA"][j]);
              temp5 += Number(this.playerData[i].data["3P%"][j]);
              temp6 += Number(this.playerData[i].data["2PA"][j]);
              temp7 += Number(this.playerData[i].data["2P%"][j]);
            }
          }
          if (state == 1) {
            dataTemp.push({
              pic_url: this.playerData[i].pic_url,
              name: this.playerData[i].name,
              Season: this.nowSelectSeason,
              PTS: (temp1 / index).toFixed(1),
              TRB: (temp2 / index).toFixed(1),
              AST: (temp3 / index).toFixed(1),
              "3PA": (temp4 / index).toFixed(1),
              "3P%": ((temp5 / index)*100).toFixed(1) +'%',
              "2PA": (temp6 / index).toFixed(1),
              "2P%": ((temp7 / index)*100).toFixed(1) +'%',
              index: indexTemp
            });
          }
        }
      }
      // console.log(dataTemp)
      for (i = 0; i < dataTemp.length; i++) {
        if (dataTemp[i].PTS == "NaN") {
          dataTemp.splice(i--, 1);
        }
      }
      // console.log(dataTemp)
      this.temp = dataTemp;

      // console.log(this.temp)
    },
    nextPage() {
      if (this.page + 1 <= this.numberOfPages) this.page += 1;
    },
    formerPage() {
      if (this.page - 1 >= 1) this.page -= 1;
    },
    updateItemsPerPage(number) {
      this.itemsPerPage = number;
    },
    FilterPlayerData() {
      for (var key in this.temp) {
        // if(this.nowSelectSeason == this.temp[key].Season){
        this.items.push(this.temp[key]);
        // }
      }
      // console.log(this.items)
      return this.items;
    },
    TestClick(output) {
      this.dialog = true;
      this.dialogItem = output;
      this.name = output.name;
      this.indexTemp = output.index;
      this.showPlayer=true
                setTimeout(this.setDialogT,50)
      // console.log(this.name);
    },
   parentClose(){
                this.dialog=false
            },
            setDialogT(){
              this.dialog=true
            },
            setShowPlayerF(){
              this.showPlayer=false
            }
  }
};
</script>
