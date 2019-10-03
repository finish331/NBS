<template>
<div class="champion px-5">
<<<<<<< HEAD
  <div class="col-sm-12 col-md-3 champion1" >
    <div class="col-md-12 rank-bg"  @mouseover="test(0)" @mouseout="test(1)">
      <div class="col-md-8 bgimg"></div>
      <div class="col-md-4 rank-percent">
        87%
=======
  <!-- 左半部 -->
  <div class="col-sm-12 col-md-3 champion-left">
    <div class="row ">
      <div class="col-md-12 test">
        <div class="col-md-8 bgimg">
        </div>
        <div class="col-md-4 test1">
          87%<br>
          Golden State Warriors
        </div>
>>>>>>> 9fc78a91cdce5c5562e3987a6dfa51d5841b0341
      </div>
      <div class="col-md-12 rank-team" v-bind:class="{'rank-team-in':isTeamIn,'rank-team-out':isTeamOut}">
          Golden State Warriors
      </div>
    </div>
    <div class="col-md-12 rank-bg"  @mouseover="test(0)" @mouseout="test(1)">
      <div class="col-md-8 bgimg"></div>
      <div class="col-md-4 rank-percent">
        87%
      </div>
      <div class="col-md-12 rank-team" v-bind:class="{'rank-team-in':isTeamIn,'rank-team-out':isTeamOut}">
          Golden State Warriors
      </div>
    </div>
    <div class="col-md-12 rank-bg"  @mouseover="test(0)" @mouseout="test(1)">
      <div class="col-md-8 bgimg"></div>
      <div class="col-md-4 rank-percent">
        87%
      </div>
      <div class="col-md-12 rank-team" >
          Golden State Warriors
      </div>
    </div>

    </div>
<<<<<<< HEAD
  <!-- </div> -->
  <div class="col-sm-12 col-md-9" style="display:flex">
=======
  </div>
  <!-- 右半部 -->
  <div class="col-sm-12 col-md-9 champion-right">
    <!-- 左邊隊伍 -->
>>>>>>> 9fc78a91cdce5c5562e3987a6dfa51d5841b0341
    <div class="col-sm-12 col-md-6 left-team">
      <!-- 球隊下拉選單 -->
      <div style="height:5%">
        <form >
          <select name="selectLeftTeam" id="selectLeftTeam" @change="print_value(0)">
            <option v-for="(i, index) in teamData" :key="index"  :value=index >{{i.name}}</option>
          </select>
        </form>
      </div>
      <!-- 球隊LOGO -->
      <div id="left-team-logo" @click="clickTeam('left')" style=""></div>

      <div style="display:flex;width:100%;height:10%">
        <div class="col player-btn" style="padding:0" v-for="(i, index) in leftTeam.player" :key="index">
          <div @click="clickPlayer(index,0)" style="height:100%;background-color: #272727;" v-if=i.state>{{i.name}}</div>
          <div @click="clickPlayer(index,0)" style="height:100%;" v-else>{{i.name}}</div>
        </div>
      </div>
      <!-- 圖表 -->
      <div style="width:100%;height:45%">
<<<<<<< HEAD
        <div v-if="leftTeam.isTeam">
          <ve-bar height="300px" :legend="radarLegend" :textStyle="textStyles" :data="leftTeamDate" :extend="leftseries">
          </ve-bar>
        </div>
        <div v-else>
          <div v-for="(i, index) in leftTeam.player" :key="index">
            <div v-if="i.state">
              <div>
                <ve-bar height="300px" :legend="radarLegend" :textStyle="textStyles" :data="leftPlayerData" :extend="leftseries">
=======
        <!-- 球隊圖表 -->
        <div style="width:100%;height:100%" v-if="leftTeam.isTeam">
          <ve-bar height="100%" :xAxis="xAxis" :legend="radarLegend" :textStyle="textStyles" :data="leftTeamDate" :extend="leftseries" >
          </ve-bar>
        </div>
        <!-- 球員圖表 -->
        <div style="width:100%;height:100%" v-else>
          <ve-bar height="100%" :xAxis="xAxis" :textStyle="textStyles" :data="leftPlayerData" :extend="leftseries" :legend="radarLegend">
>>>>>>> 9fc78a91cdce5c5562e3987a6dfa51d5841b0341
                </ve-bar>
        </div>

      </div>
    </div>
    <!-- 右邊隊伍 -->
    <div class="col-sm-12 col-md-6 right-team">
      <!-- 球隊下拉選單 -->
      <div style="height:5%">
        <form >
          <select name="selectRightTeam" id="selectRightTeam" @change="print_value(1)">
            <option v-for="(i, index) in teamData" :key="index"  :value=index >{{i.name}}</option>
          </select>
        </form>
      </div>
      <!-- 球隊LOGO -->
      <div id="right-team-logo" @click="clickTeam('right')" ></div>

      <div style="display:flex;width:100%;height:10%">
        <div class="col player-btn" style="padding:0" v-for="(i, index) in rightTeam.player" :key="index">
          <div @click="clickPlayer(index,1)" style="height:100%;background-color: #272727;" v-if=i.state>{{i.name}}</div>
          <div @click="clickPlayer(index,1)" style="height:100%;" v-else>{{i.name}}</div>
        </div>
      </div>

      <div style="width:100%;height:45%">
<<<<<<< HEAD
        <div v-if="rightTeam.isTeam">
          <ve-bar height="300px"  :legend="radarLegend" :xAxis="xAxis" :textStyle="textStyles" :data="rightTeamDate" :extend="rightseries">
          </ve-bar>
        </div>
        <div v-else>
          <div v-for="(i, index) in rightTeam.player" :key="index">
            <div v-if="i.state">
              <div>
                <ve-bar height="300px" :legend="radarLegend" :xAxis="xAxis" :textStyle="textStyles" :data="rightPlayerData" :extend="rightseries">
                </ve-bar>
              </div>
            </div>
          </div>
=======
        <!-- 球隊圖表 -->
        <div style="width:100%;height:100%" v-if="rightTeam.isTeam">
          <ve-bar height="100%"  :textStyle="textStyles" :legend="radarLegend"  :data="rightTeamDate" :extend="rightseries">
          </ve-bar>
        </div>
        <!-- 球員圖表 -->
        <div style="width:100%;height:100%" v-else>
          <ve-bar height="100%"  :textStyle="textStyles" :legend="radarLegend"  :data="rightPlayerData" :extend="rightseries">
          </ve-bar>
>>>>>>> 9fc78a91cdce5c5562e3987a6dfa51d5841b0341
        </div>
      </div>
    </div>
  </div>
</div>
</template>
<script>
import {lineChart} from "@/assets/js/championConfig.js";
import teamData from "@/assets/json/team.json";
export default {
  components: {},
  data() {
    return {
<<<<<<< HEAD
      isTeamIn:false,
      isTeamOut:false,
=======
      teamData:teamData,
>>>>>>> 9fc78a91cdce5c5562e3987a6dfa51d5841b0341
      ...lineChart,
      leftTeamDate: {
        columns: ['type', 'value'],
        rows: [{
            'type': 'PTS',
            'value': 3.1
          },
          {
            'type': 'TRB',
            'value': 3
          },
          {
            'type': 'AST',
            'value': 5.3
          },
          {
            'type': 'BLK',
            'value': 5
          },
          {
            'type': 'STL',
            'value': 1
          }
        ]
      },
      rightTeamDate: {
        columns: ['type', 'value'],
        rows: [{
            'type': 'PTS',
            'value': 3.1
          },
          {
            'type': 'TRB',
            'value': 3
          },
          {
            'type': 'AST',
            'value': 5.3
          },
          {
            'type': 'BLK',
            'value': 5
          },
          {
            'type': 'STL',
            'value': 1
          }
        ]
      },
      leftPlayerData: {
        columns: ['type', 'value'],
        rows: [{
            'type': 'PTS',
            'value': 36.1
          },
          {
            'type': 'TRB',
            'value': 3
          },
          {
            'type': 'AST',
            'value': 5.3
          },
          {
            'type': 'BLK',
            'value': 5
          },
          {
            'type': 'STL',
            'value': 1
          }
        ]
      },
      rightPlayerData: {
        columns: ['type', 'value'],
        rows: [{
            'type': 'PTS',
            'value': 36.1
          },
          {
            'type': 'TRB',
            'value': 3
          },
          {
            'type': 'AST',
            'value': 5.3
          },
          {
            'type': 'BLK',
            'value': 5
          },
          {
            'type': 'STL',
            'value': 1
          }
        ]
      },
      rightTeam: {
        isTeam: true,
         index: 0 ,
        img:teamData[0].pic_url,
        team: {
          aa: 1,
          bc: 9,
          sc: 4,
          sassad: 3,
          se: 2
        },
        player: [{
            state: false,
            name: "player1",
            PTS: 6.1,
            TRB: 6.6,
            AST: 7.5,
            BLK: 0.7,
            STL: 2.0
          },
          {
            state: false,
            name: "player2",
            PTS: 36.1,
            TRB: 6,
            AST: 7.5,
            BLK: 0.7,
            STL: 2.0
          },
          {
            state: false,
            name: "player3",
            PTS: 3.1,
            TRB: 7.6,
            AST: 7.5,
            BLK: 0.7,
            STL: 2.0
          },
          {
            state: false,
            name: "player4",
            PTS: 8.1,
            TRB: 8.6,
            AST: 7.5,
            BLK: 0.7,
            STL: 2.0
          },
          {
            state: false,
            name: "player5",
            PTS: 16.1,
            TRB: 96,
            AST: 7.5,
            BLK: 0.7,
            STL: 2.0
          }
        ],
      },
      leftTeam: {
        index: 0 ,
        img:teamData[0].pic_url,
        isTeam: true,
        team: {
          aa: 1,
          bc: 9,
          sc: 4,
          sassad: 3,
          se: 2
        },
        player: [{
            state: false,
            name: "player1",
            PTS: 6.1,
            TRB: 6.6,
            AST: 7.5,
            BLK: 0.7,
            STL: 2.0
          },
          {
            state: false,
            name: "player2",
            PTS: 36.1,
            TRB: 6,
            AST: 7.5,
            BLK: 0.7,
            STL: 2.0
          },
          {
            state: false,
            name: "player3",
            PTS: 3.1,
            TRB: 7.6,
            AST: 7.5,
            BLK: 0.7,
            STL: 2.0
          },
          {
            state: false,
            name: "player4",
            PTS: 8.1,
            TRB: 8.6,
            AST: 7.5,
            BLK: 0.7,
            STL: 2.0
          },
          {
            state: false,
            name: "player5",
            PTS: 16.1,
            TRB: 96,
            AST: 7.5,
            BLK: 0.7,
            STL: 2.0
          }
        ],
      }
    };
  },
  mounted: function(){
    this.clickTeam('left');
    this.clickTeam('right');
    var url="url("+this.rightTeam.img+")"
    document.getElementById('left-team-logo').style.backgroundImage = url
    document.getElementById('right-team-logo').style.backgroundImage = url
  },
  methods: {
<<<<<<< HEAD
    test(i){
      if(i==0){
        this.isTeamIn=true
        this.isTeamOut=false
      }
      else{
        this.isTeamIn=false
        this.isTeamOut=true
=======
    print_value(i){
      var url
      if(i==0){
        this.leftTeam.index=document.getElementById("selectLeftTeam").value
        this.leftTeam.img=teamData[this.leftTeam.index].pic_url
        url="url("+this.leftTeam.img+")"
        document.getElementById('left-team-logo').style.backgroundImage = url
      }
      else{
        this.rightTeam.index=document.getElementById("selectRightTeam").value
        this.rightTeam.img=teamData[this.rightTeam.index].pic_url
        url="url("+this.rightTeam.img+")"
        document.getElementById('right-team-logo').style.backgroundImage = url
>>>>>>> 9fc78a91cdce5c5562e3987a6dfa51d5841b0341
      }
    },
    clickPlayer(i, lr) {
      if (lr == 0) {
        this.leftTeam.isTeam = false;
        this.leftTeam.player[i].state = true;
        this.leftPlayerData.rows[0].value = this.leftTeam.player[i].PTS;
        this.leftPlayerData.rows[1].value = this.leftTeam.player[i].TRB;
        this.leftPlayerData.rows[2].value = this.leftTeam.player[i].AST;
        this.leftPlayerData.rows[3].value = this.leftTeam.player[i].BLK;
        this.leftPlayerData.rows[4].value = this.leftTeam.player[i].STL;
        for (var j = 0; j < this.leftTeam.player.length; j++) {
          if (i !== j) {
            this.leftTeam.player[j].state = false;
          }
        }
      } else {
        this.rightTeam.isTeam = false;
        this.rightTeam.player[i].state = true;
        this.rightPlayerData.rows[0].value = this.rightTeam.player[i].PTS;
        this.rightPlayerData.rows[1].value = this.rightTeam.player[i].TRB;
        this.rightPlayerData.rows[2].value = this.rightTeam.player[i].AST;
        this.rightPlayerData.rows[3].value = this.rightTeam.player[i].BLK;
        this.rightPlayerData.rows[4].value = this.rightTeam.player[i].STL;
        for (j = 0; j < this.rightTeam.player.length; j++) {
          if (i !== j) {
            this.rightTeam.player[j].state = false;
          }
        }
      }

    },
    clickTeam(text) {
      if (text === 'left') {
        this.leftTeam.isTeam = true;
        this.leftTeamDate.rows[0].value = this.leftTeam.team.aa;
        this.leftTeamDate.rows[1].value = this.leftTeam.team.bc;
        this.leftTeamDate.rows[2].value = this.leftTeam.team.sc;
        this.leftTeamDate.rows[3].value = this.leftTeam.team.sassad
        this.leftTeamDate.rows[4].value = this.leftTeam.team.se;

        for (var j = 0; j < this.leftTeam.player.length; j++) {

          this.leftTeam.player[j].state = false;

        }
      }
      else{
        this.rightTeam.isTeam = true;
        this.rightTeamDate.rows[0].value = this.rightTeam.team.aa;
        this.rightTeamDate.rows[1].value = this.rightTeam.team.bc;
        this.rightTeamDate.rows[2].value = this.rightTeam.team.sc;
        this.rightTeamDate.rows[3].value = this.rightTeam.team.sassad
        this.rightTeamDate.rows[4].value = this.rightTeam.team.se;

        for (j = 0; j < this.rightTeam.player.length; j++) {

          this.rightTeam.player[j].state = false;

        }
      }

    }
  }
};
</script>
<style>
#left-team-logo{
   cursor: pointer;
   width:100% ;
   height:40%;
   filter: drop-shadow(0px 0px 10px rgba(0, 0, 0, .5));
   background-size: contain;
   background-image:url(https://stats.nba.com/media/img/teams/logos/HOU_logo.svg);
   background-position: center;
   background-repeat: no-repeat;
}
#right-team-logo{
   cursor: pointer;
   width:100% ;
   height:40%;
   filter: drop-shadow(0px 0px 10px rgba(0, 0, 0, .5));
   background-size: contain;
   background-image:url(https://stats.nba.com/media/img/teams/logos/HOU_logo.svg);
   background-position: center;
   background-repeat: no-repeat;
}
#selectLeftTeam{
  background:#fff;
  color:#1d1d1d
}
#selectRightTeam{
  background:#fff;
  color:#1d1d1d
}
.champion {
  display: flex;
  height: calc(100vh - 76px);
  width: 100%;
}
.champion-left {
  height: calc(100vh - 76px);
  overflow: auto;
}
<<<<<<< HEAD
.rank-bg {
  position: relative;
=======
.champion-right{
  height: 100%;
  display:flex;
  
}
.test {
>>>>>>> 9fc78a91cdce5c5562e3987a6dfa51d5841b0341
  display: flex;
  margin: 10px 0;
  padding: 0;
  height: 80px;
  border-radius: 2px;
  background: linear-gradient(45deg, #1d1d1d 50%, #1d4289 100%);
  box-shadow: 2px 2px 10px rgb(29, 29, 29, .75);
}

.bgimg {
  width: 100%;
  background: url('../assets/GSW_logo.svg');
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  opacity: 1;
}
@keyframes rank-team-in {
  from {
    opacity: 0;
    bottom: -2px;
  }
  to {
    opacity: 1;
    bottom: 0;
    text-shadow:0 5px 10px black,0 0 10px black,0 0 10px black;
  }
}
@keyframes rank-team-out {
  from {
    opacity: 1;
    bottom: 0;
    text-shadow:0 5px 10px black,0 0 10px black,0 0 10px black;
  }
  to {
    opacity: 0;
    bottom: -2px;
  }
}
.rank-team-in{
  animation: rank-team-in  .5s  forwards;
}
.rank-team-out{
  animation: rank-team-out  .5s  forwards;
}
.rank-team{
text-shadow:0 5px 10px black,0 0 10px black,0 0 10px black;
  position: absolute;
  bottom: 0px;
  padding: 0;
  color: white;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-size: 20px;
  font-weight: bold;
  opacity: 1;
}
.rank-percent {
  display: flex;
  justify-content: center;
  align-items: center;
  padding:  0 0 20px 0;
  color: white;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-size: 24px;
  font-weight: bold;
}

.left-team {
  color: white;
  background-color: #1d1d1d;
<<<<<<< HEAD
  border: 12px solid white;
  height: calc(100vh - 76px);
  border-radius: 15px;
=======
  /* border: 12px solid white; */
  height: 100%;
>>>>>>> 9fc78a91cdce5c5562e3987a6dfa51d5841b0341
}

.right-team {
  color: white;
  background-color: #1d1d1d;
  /* border: 12px solid white; */
  height: 100%
}

.player-btn {
  cursor: pointer;
}

.player-btn:hover {
  background-color: #272727;
}
@media (max-width:960px){
  .champion {
    display: block;
  }
  .champion-left {
    height: 30vh;
  }
  .right-team{
    display: none;
  }
}
</style>
