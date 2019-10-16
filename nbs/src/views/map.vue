<template>
  <div style="position: relative;width:100%;height:calc(100vh - 76px);padding:5%">
    <div style="position: relative;width:100%;height:100%">
      
      <div class="map-now align-items-center" style="height:100%;width:100%;padding-right:10%">
        <ve-map
          height="100%"
          width="100%"
          :visualMap="visualMap"
          :events="{ click: clickHandler.bind(this, 1),mouseover:test.bind(this,1) }"
          :tooltip="tooltip"
          :data="chartData"
          :settings="chartSettings"
          :legend="legend"
        ></ve-map>
      </div>
      <div class="map-rwd align-items-center" style="height:100%;width:100%;padding-right:10%">
        <ve-map
          height="100%"
          width="100%"
          :visualMap="visualMap"
          :events="{ click: clickHandler.bind(this, 1),mouseover:test.bind(this,1) }"
          :tooltip="tooltips"
          :data="chartData"
          :settings="chartSettings"
          :legend="legend"
        ></ve-map>
      </div>
    </div>
    <v-dialog v-model="dialog" width="100%">
        <v-card>
          <div
            style="overflow:auto;position: relative;max-height:100%;widht:100%;background:#f4f4f4;box-shadow:5px 5px 10px  rgb(29, 29, 29,.1);z-index:11;padding:5%"
          >
            <button @click="close" style="position: absolute;z-index:9999;top:5px;right:5px">
              <v-icon style="font-size:30px">cancel</v-icon>
            </button>
            <div class="showTeam">
              <div
                class="col-sm-4 col-md-3 team hover"
                v-for="(j, index1) in team[teamName]"
                :key="index1"
              >
                <div
                  style="cursor: pointer;width:100%;height:0;padding-bottom:80%;position: relative;"
                >
                  <div v-for="(i, index) in teamData" :key="index">
                    <img
                      @click="setTeam(index)"
                      :teamIndex="index"
                      :src="i.pic_url"
                      alt
                      style="width:80%;position: absolute;top:0px;left:10%;"
                      v-if="j==i.name"
                    />
                  </div>
                </div>
                <div v-for="(i, index) in teamData" :key="index">
                    <div @click="setTeam(index)" style="cursor: pointer;" v-if="j==i.name">{{j}}</div>
                  </div>
              </div>
            </div>
          </div>
        </v-card>
      </v-dialog>
    <v-dialog v-model="dialogTeam" width="100%" v-if="showTeam">
      <v-card>
        <!-- <div id="testttttt"  v-if="showTeam" :class={teamIn:showTeam}> -->
        <map1 :team="teamData[teamIndex]" @close="parentClose" />
        <!-- </div> -->
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import usMap from "@/assets/json/custom-map.json";
import map1 from "./map1";
import teamData from "@/assets/json/team.json";
export default {
  data() {
    return {
      dialogTeam: false,
      dialog: false,
      legend: {
        show: false
      },
      tooltips: {
        show: false
      },
      tooltip: {
        show: true,
        formatter: function(params) {
          return params.name;
        }
      },
      teamIndex: 0,
      teamData: teamData,
      showTeam: false,
      clickHandler(p, e) {
        // console.log(e.name)
        if (this.team[e.name] != null) {
          this.dialog = true;
          this.teamName = e.name;
          this.showSelectTeam = true;
        }
      },
      test(p, e) {
        if (this.team[e.name] != null) {
          // console.log(e.value);
        }
      },
      team: {
        California: [
          "Golden State Warriors",
          "Los Angeles Clippers",
          "Los Angeles Lakers",
          "Sacramento Kings"
        ],
        Georgia: ["Atlanta Hawks"],
        Massachusetts: ["Boston Celtics"],
        "New York": ["Brooklyn Nets", "New York Knicks"],
        "North Carolina": ["Charlotte Hornets"],
        Illinois: ["Chicago Bulls"],
        Ohio: ["Cleveland Cavaliers"],
        Texas: ["Dallas Mavericks", "Houston Rockets", "San Antonio Spurs"],
        Colorado: ["Denver Nuggets"],
        Michigan: ["Detroit Pistons"],
        Indiana: ["Indiana Pacers"],
        Tennessee: ["Memphis Grizzlies"],
        Florida: ["Miami Heat", "Orlando Magic"],
        Wisconsin: ["Milwaukee Bucks"],
        Minnesota: ["Minnesota Timberwolves"],
        Louisiana: ["New Orleans Pelicans"],
        Oklahoma: ["Oklahoma City Thunder"],
        Pennsylvania: ["Philadelphia 76ers"],
        Arizona: ["Phoenix Suns"],
        Oregon: ["Portland Trail Blazers"],
        Utah: ["Utah Jazz"],
        Washington: ["Washington Wizards"],
        Ontario: ["Toronto Raptors"]
      },
      teamName: "",
      chartData: {
        columns: ["位置", "value"],
        rows: [
          { 位置: "California", value: 1 },
          { 位置: "Georgia", value: 1 },
          { 位置: "Massachusetts", value: 1 },
          { 位置: "New York", value: 1 },
          { 位置: "North Carolina", value: 1 },
          { 位置: "Illinois", value: 1 },
          { 位置: "Ohio", value: 1 },
          { 位置: "Texas", value: 1 },
          { 位置: "Colorado", value: 1 },
          { 位置: "Michigan", value: 1 },
          { 位置: "Indiana", value: 1 },
          { 位置: "Tennessee", value: 1 },
          { 位置: "Florida", value: 1 },
          { 位置: "Wisconsin", value: 1 },
          { 位置: "Minnesota", value: 1 },
          { 位置: "Louisiana", value: 1 },
          { 位置: "Oklahoma", value: 1 },
          { 位置: "Pennsylvania", value: 1 },
          { 位置: "Arizona", value: 1 },
          { 位置: "Oregon", value: 1 },
          { 位置: "Utah", value: 1 },
          { 位置: "Washington", value: 1 },
          { 位置: "Ontario", value: 1 }
        ]
      },
      visualMap: {
        left: "right",
        min: 0,
        max: 1,
        inRange: {
          color: ["#aeaeae", "#eee"]
        },
        text: ["High", "Low"], // 文本，默认为数值文本
        show: false
      },
      chartSettings: {
        aspectScale: 1.8,
        zoom: 1.25,
        mapOrigin: usMap,
        itemStyle: {
          normal: {
            areaColor: "#aeaeae",
            color: "transparent"
          },
          emphasis: {
            label: {
              show: false
            },
            areaColor: "#7e7e7e"
          }
        },
        label: {
          show: false
        }
      }
    };
  },
  components: {
    map1
  },
  watch: {
            dialogTeam (val) {
            !val && setTimeout(this.setShowTeamF,250) 
            }
        },
  mounted() {},
  methods: {
    parentClose() {
      this.dialogTeam = false;
      // this.showTeam = true;
      // setTimeout(this.setDialogT,50)
    },
    close() {
      this.dialog = false;
    },
    setTeam(index) {
      this.teamIndex = index;
      this.dialog = false;
      this.showTeam = true;
      setTimeout(this.setDialogT,50)
      
    },
    setDialogT() {
      this.dialogTeam = true;
    },
    setShowTeamF(){
      this.showTeam =false
      this.dialog = true;
    }
  }
};
</script>

<style>
.map-rwd {
  display: none;
}
@media (max-width: 991px) {
  .map-now {
    display: none;
  }
  .map-rwd {
    display: block;
  }
}
@keyframes teamIn {
  from {
    transform: scale(0.5);
  }
  to {
    transform: scale(1);
  }
}
.teamIn {
  font-size: 1.2rem;
  letter-spacing: 1px;
  font-weight: bold;
  line-height: 1.3;
  animation: teamIn 0.5s 1 backwards;
}
@keyframes teamOut {
  from {
    transform: scale(1);
  }
  to {
    transform: scale(0);
  }
}
.teamOut {
  font-size: 1.2rem;
  letter-spacing: 1px;
  font-weight: bold;
  line-height: 1.3;
  animation: teamOut 0.5s 1 backwards;
}
.team {
  /* margin-bottom: 20px; */
  /* height: 30%; */
  width: 100%;
}
.showTeam {
  width: 100%;
  height: 100%;
  display: flex;
  flex-wrap: wrap;
}
#selectTeam {
  position: absolute;
  width: 100%;
  height: calc(100vh - 76px);
  max-height: 100vh;
  padding: 5%;
  top: 0;
  left: 0;
  z-index: 10;
}
#testttttt {
  width: 100%;
  position: absolute;
  top: 0;
  /* padding: 5%; */
  /* display: none; */
}
.page-height {
  height: calc(100vh - 80px);
}
</style>
