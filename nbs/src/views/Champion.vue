<template>
<div class="champion px-5">
  <div class="col-sm-12 col-md-3 champion1" >
    <div class="row ">
      <div class="col-md-12 test">
        <div class="col-md-8 bgimg">
        </div>
        <div class="col-md-4 test1">
          87%<br>
          Golden State Warriors
        </div>
      </div>
    </div>
    <div class="row ">
      <div class="col-md-12 test">
        <div class="col-md-8 bgimg">
        </div>
        <div class="col-md-4 test1">
          87%<br>
          Golden State Warriors
        </div>
      </div>
    </div>
    <div class="row ">
      <div class="col-md-12 test">
        <div class="col-md-8 bgimg"></div>
        <div class="col-md-4 test1">
          87%<br>

          Golden State Warriors

        </div>
      </div>
    </div>
    <div class="row ">
      <div class="col-md-12 test">
        <div class="col-md-8 bgimg">

        </div>
        <div class="col-md-4 test1">
          87%<br>

          Golden State Warriors

        </div>
      </div>
    </div>
    <div class="row ">
      <div class="col-md-12 test">
        <div class="col-md-8 bgimg">

        </div>
        <div class="col-md-4 test1">
          87%<br>

          Golden State Warriors

        </div>
      </div>
    </div>
    <div class="row ">
      <div class="col-md-12 test">
        <div class="col-md-8 bgimg">

        </div>
        <div class="col-md-4 test1">
          87%<br>

          Golden State Warriors

        </div>
      </div>
    </div>
    <div class="row ">
      <div class="col-md-12 test">
        <div class="col-md-8 bgimg">

        </div>
        <div class="col-md-4 test1">
          87%<br>

          Golden State Warriors

        </div>
      </div>
    </div>
  </div>
  <div class="col-sm-12 col-md-9" style="display:flex">
    <div class="col-sm-12 col-md-6 left-team">
      <div @click="clickTeam('left')" style=" cursor: pointer;width:100% ;height:40%;background: url('https://stats.nba.com/media/img/teams/logos/HOU_logo.svg');background-position: center;background-repeat: no-repeat;"></div>
      <div style="display:flex;width:100%;height:15%">
        <div class="col player-btn" style="padding:0" v-for="(i, index) in leftTeam.player" :key="index">
          <div @click="clickPlayer(index,0)" style="height:100%;background-color: #272727;" v-if=i.state>{{i.name}}</div>
          <div @click="clickPlayer(index,0)" style="height:100%;" v-else>{{i.name}}</div>
        </div>

      </div>
      <div style="width:100%;height:45%">
        <div v-if="leftTeam.isTeam">
          <ve-bar height="300px" :textStyle="textStyles" :data="leftTeamDate" :extend="leftseries">
          </ve-bar>
        </div>
        <div v-else>
          <div v-for="(i, index) in leftTeam.player" :key="index">
            <div v-if="i.state">
              <div>
                <ve-bar height="300px"  :textStyle="textStyles" :data="leftPlayerData" :extend="leftseries">
                </ve-bar>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="col-sm-12 col-md-6 right-team">
      <div @click="clickTeam('right')" style=" cursor: pointer;width:100% ;height:40%;background: url('https://stats.nba.com/media/img/teams/logos/HOU_logo.svg');background-position: center;background-repeat: no-repeat;"></div>
      <div style="display:flex;width:100%;height:15%">
        <div class="col player-btn" style="padding:0" v-for="(i, index) in rightTeam.player" :key="index">
          <div @click="clickPlayer(index,1)" style="height:100%;background-color: #272727;" v-if=i.state>{{i.name}}</div>
          <div @click="clickPlayer(index,1)" style="height:100%;" v-else>{{i.name}}</div>
        </div>

      </div>
      <div style="width:100%;height:45%">
        <div v-if="rightTeam.isTeam">
          <ve-bar height="300px" :xAxis="xAxis" :textStyle="textStyles" :data="rightTeamDate" :extend="rightseries">
          </ve-bar>
        </div>
        <div v-else>
          <div v-for="(i, index) in rightTeam.player" :key="index">
            <div v-if="i.state">
              <div>
                <ve-bar height="300px" :xAxis="xAxis" :textStyle="textStyles" :data="rightPlayerData" :extend="rightseries">
                </ve-bar>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>
<script>
import {
  lineChart
} from "@/assets/js/championConfig.js";
export default {
  components: {},
  data() {
    return {
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

  },
  methods: {
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
.champion {
  display: flex;
  height: calc(100vh - 76px);
  width: 100%;
}
.champion1 {
  height: calc(100vh - 76px);
  overflow: auto;
}



.test {
  display: flex;
  margin: 10px 0;
  padding: 0;
  /* height: 100%; */
  background: linear-gradient(to right, #1d1d1d, black);
  box-shadow: 5px 5px 5px rgb(29, 29, 29, .75);
}

.bgimg {
  width: 100%;
  height: 100%;
  background: url('../assets/GSW_logo.svg');
  background-position: center;
  background-size: 140%;
  background-repeat: no-repeat;
  opacity: .75;
}

.test1 {
  /* padding: 5% 0; */
  color: white;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-size: 20px;
  font-weight: bold;
}

.left-team {
  color: white;
  background-color: #1d1d1d;
  border: 12px solid white;
  height: calc(100vh - 76px);
}

.right-team {
  color: white;
  background-color: #1d1d1d;
  border: 12px solid white;
  height: calc(100vh - 76px);
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
  .champion1 {
    height: 30vh;
  }
  .right-team{
    display: none;
  }
}
</style>
