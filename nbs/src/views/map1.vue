<template>
<div class="map1">
  <div class="team-content">
    <div class="content-head" style="position: relative;display:flex; align-items: center;">
      <button @click="close" style="position: absolute;z-index:9999;top:5px;right:5px">
        <v-icon style="font-size:30px">cancel</v-icon>
      </button>
      <div id="mapTeamLogo" style=";background-size: cover;
                    background-position: center center ; height:100%;width:100%;opacity: .1;position: absolute;">
      </div>
      <img :src=team.pic_url alt="" height="100%;">
      <div class="team-name-size" style="color:white;align-items:center;">
        {{team.name}}
      </div>
    </div>
    <div style="display:flex;height:20%">
      <template v-for="(i, index) in List">
        <div class="col-xs-3 col-sm-3 col-md-2" style="padding:2px" :key="index">
          <div style="padding:10px;background:#666666;height:100%;color:white">
            <div class="title-size" style="height:40%;text-align:left">{{i.title}}</div>
            <div class="value-size" style="height:60%;">{{i.value}}</div>
          </div>
        </div>
      </template>
      <div id="selectYear" class="col-xs-12 col-sm-12 col-md-4" style="padding:2px">
        <div style="padding:10px;background:#666666;height:100%;color:white">
          <div style="height:40%;text-align:left">賽季</div>
          <form style="height:60%;">
            <select name="selectSeason" id="selectSeason" @change="selectSeason()" >
              <option value="2018-19">2018-19</option>
              <option value="2017-18">2017-18</option>
              <option value="2016-17">2016-17</option>
              <option value="2015-16">2015-16</option>
              <option value="2014-15">2014-15</option>
              <option value="2013-14">2013-14</option>
              <option value="2012-13">2012-13</option>
              <option value="2011-12">2011-12</option>
              <option value="2010-11">2010-11</option>
              <option value="2009-10">2009-10</option>
            </select>
          </form>
        </div>
      </div>

    </div>
    <div id="selectYear1" class="col-xs-12 col-sm-12 col-md-4" style="">
      <div style="padding:10px;background:#666666;height:80px;color:white">
        <div class="title-size" style="height:40%;text-align:left">賽季</div>
          <form style="height:100%;">
            <select class="value-size" name="selectSeason" id="selectSeason1" @change="selectSeason1()" >
              <option value="2018-19">2018-19</option>
              <option value="2017-18">2017-18</option>
              <option value="2016-17">2016-17</option>
              <option value="2015-16">2015-16</option>
              <option value="2014-15">2014-15</option>
              <option value="2013-14">2013-14</option>
              <option value="2012-13">2012-13</option>
              <option value="2011-12">2011-12</option>
              <option value="2010-11">2010-11</option>
              <option value="2009-10">2009-10</option>
            </select>
          </form>
      </div>
    </div>
    <div style="display:flex;height:60% ;padding:0 2%;position: relative;">

      <button @click="left" style="z-index:999;position: absolute;left:1px;top:calc(50% - 30px)">
        <v-icon style="font-size:30px">arrow_back_ios</v-icon>
      </button>

      <button @click="right" style="z-index:999;position: absolute;right:1px;top:calc(50% - 30px)">
        <v-icon style="font-size:30px">arrow_forward_ios</v-icon>
      </button>
      <template v-for="(i, index) in playerData">
        <div id="showPlayer1" class="col-xs-12 col-sm-4 col-md-3" style="padding:10px" :key="index" v-if="index<page+4&&index>=page&&windowWidth>=960">
          <div class="player-card">
            <div style="display:flex;align-items:center;height:30%;justify-content: space-around">
              <img width="60%" :src=playerData[index].pic_url />
              <div>
                <div>
                  {{playerData[index].no}}
                </div>
                <div>
                  {{playerData[index].player}}
                </div>
              </div>
            </div>
            <div style="display:flex;align-items:center;height:20%;justify-content: space-around">
              <div class="col-md-4" style="padding:2px;color:white;height:100%">
                <div style="background-color: #666666 ;padding:5px;height:100%">
                  <div class="title-size" style="height:50%;text-align:left;">POS</div>
                  <div class="value-size" style="height:50%;f">{{playerData[index].pos}}</div>
                </div>
              </div>
              <div class="col-md-4" style="padding:2px;color:white;height:100%">
                <div style="background-color: #666666 ;padding:5px;height:100%">
                  <div class="title-size" style="height:50%;text-align:left;">HT</div>
                  <div class="value-size" style="height:50%;">{{playerData[index].ht}}</div>
                </div>
              </div>
              <div class="col-md-4" style="padding:2px;color:white;height:100%">
                <div style="background-color: #666666 ;padding:5px;height:100%">
                  <div class="title-size" style="height:50%;text-align:left;">WT</div>
                  <div class="value-size" style="height:50%;">{{playerData[index].wt}}</div>
                </div>
              </div>
            </div>
            <div style="display:flex;align-items:center;height:30%;justify-content: space-around">
              <div class="col-md-6" style="padding:2px;color:white;height:100%">
                <div style="background-color: #666666 ;padding:5px;height:100%">
                  <div class="title-size" style="height:50%;text-align:left;">BirthDate</div>
                  <div class="value-size" style="height:50%;">{{playerData[index].birthDate}}</div>
                </div>
              </div>
              <div class="col-md-3" style="padding:2px;color:white;height:100%">
                <div style="background-color: #666666 ;padding:5px;height:100%">
                  <div class="title-size" style="height:50%;text-align:left;">HT</div>
                  <div class="value-size" style="height:50%;">{{playerData[index].ht}}</div>
                </div>
              </div>
              <div class="col-md-3" style="padding:2px;color:white;height:100%">
                <div style="background-color: #666666 ;padding:5px;height:100%">
                  <div class="title-size" style="height:50%;text-align:left;">Exp</div>
                  <div class="value-size" style="height:50%;">{{playerData[index].exp}}</div>
                </div>
              </div>
            </div>
            <div style="display:flex;align-items:center;height:20%;justify-content: space-around">
              <div class="col-md-12" style="padding:2px;color:white;height:100%">
                <div style="background-color: #666666 ;padding:5px;height:100%">
                  <div class="title-size" style=" height:50%;text-align:left;">College</div>
                  <div class="value-size" style="height:50%;">{{playerData[index].college}}</div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div id="showPlayer2" class="col-sm-6 col-md-6" style="padding:10px" :key="index" v-if="index<page+2&&index>=page&&windowWidth<960&&windowWidth>=620">
          <div class="player-card">
            <div style="display:flex;align-items:center;height:30%;justify-content: space-around">
              <img width="50%" :src=playerData[index].pic_url />
              <div>
                <div style="font-size:16px">
                  {{playerData[index].no}}
                </div>
                <div style="font-size:16px">
                  {{playerData[index].player}}
                </div>
              </div>
            </div>
            <div style="display:flex;align-items:center;height:20%;justify-content: space-around">
              <div class="col-md-4" style="padding:2px;color:white;height:100%">
                <div style="background-color: #666666 ;padding:5px;height:100%">
                  <div class="title-size" style="height:50%;text-align:left;">POS</div>
                  <div class="value-size" style="height:50%;">{{playerData[index].pos}}</div>
                </div>
              </div>
              <div class="col-md-4" style="padding:2px;color:white;height:100%">
                <div style="background-color: #666666 ;padding:5px;height:100%">
                  <div class="title-size" style="height:50%;text-align:left;">HT</div>
                  <div class="value-size" style="height:50%;">{{playerData[index].ht}}</div>
                </div>
              </div>
              <div class="col-md-4" style="padding:2px;color:white;height:100%">
                <div style="background-color: #666666 ;padding:5px;height:100%">
                  <div class="title-size" style="height:50%;text-align:left;">WT</div>
                  <div class="value-size" style="height:50%;">{{playerData[index].wt}}</div>
                </div>
              </div>
            </div>
            <div style="display:flex;align-items:center;height:30%;justify-content: space-around">
              <div class="col-md-6" style="padding:2px;color:white;height:100%">
                <div style="background-color: #666666 ;padding:5px;height:100%">
                  <div class="title-size" style="height:50%;text-align:left;">BirthDate</div>
                  <div class="value-size" style="height:50%;">{{playerData[index].birthDate}}</div>
                </div>
              </div>
              <div class="col-md-3" style="padding:2px;color:white;height:100%">
                <div style="background-color: #666666 ;padding:5px;height:100%">
                  <div class="title-size" style="height:50%;text-align:left;">HT</div>
                  <div class="value-size" style="height:50%;">{{playerData[index].ht}}</div>
                </div>
              </div>
              <div class="col-md-3" style="padding:2px;color:white;height:100%">
                <div style="background-color: #666666 ;padding:5px;height:100%">
                  <div class="title-size" style="height:50%;text-align:left;">Exp</div>
                  <div class="value-size" style="height:50%;">{{playerData[index].exp}}</div>
                </div>
              </div>
            </div>
            <div style="display:flex;align-items:center;height:20%;justify-content: space-around">
              <div class="col-md-12" style="padding:2px;color:white;height:100%">
                <div style="background-color: #666666 ;padding:5px;height:100%">
                  <div class="title-size" style="height:50%;text-align:left;">College</div>
                  <div class="value-size" style="height:50%;">{{playerData[index].college}}</div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div id="showPlayer3" class="col-12 col-sm-12 col-md-12" style="padding:10px" :key="index" v-if="index<page+1&&index>=page&&windowWidth<620">
          <div class="player-card">
            <div style="display:flex;align-items:center;height:30%;justify-content: space-around">
              <img width="30%" style="min-width:148px" :src=playerData[index].pic_url />
              <div>
                <div style="font-size:12px">
                  {{playerData[index].no}}
                </div>
                <div style="font-size:12px">
                  {{playerData[index].player}}
                </div>
              </div>
            </div>
            <div style="display:flex;align-items:center;height:20%;justify-content: space-around">
              <div class="col-md-4" style="padding:2px;color:white;height:100%">
                <div style="background-color: #666666 ;padding:5px;height:100%">
                  <div class="title-size" style="height:50%;text-align:left;">POS</div>
                  <div class="value-size" style="height:50%;">{{playerData[index].pos}}</div>
                </div>
              </div>
              <div class="col-md-4" style="padding:2px;color:white;height:100%">
                <div style="background-color: #666666 ;padding:5px;height:100%">
                  <div class="title-size" style="height:50%;text-align:left;">HT</div>
                  <div class="value-size" style="height:50%;">{{playerData[index].ht}}</div>
                </div>
              </div>
              <div class="col-md-4" style="padding:2px;color:white;height:100%">
                <div style="background-color: #666666 ;padding:5px;height:100%">
                  <div class="title-size" style="height:50%;text-align:left;">WT</div>
                  <div class="value-size" style="height:50%;">{{playerData[index].wt}}</div>
                </div>
              </div>
            </div>
            <div style="display:flex;align-items:center;height:30%;justify-content: space-around">
              <div class="col-md-6" style="padding:2px;color:white;height:100%">
                <div style="background-color: #666666 ;padding:5px;height:100%">
                  <div class="title-size" style="height:50%;text-align:left;">BirthDate</div>
                  <div class="value-size" style="height:50%;">{{playerData[index].birthDate}}</div>
                </div>
              </div>
              <div class="col-md-3" style="padding:2px;color:white;height:100%">
                <div style="background-color: #666666 ;padding:5px;height:100%">
                  <div class="title-size" style="height:50%;text-align:left;">HT</div>
                  <div class="value-size" style="height:50%;">{{playerData[index].ht}}</div>
                </div>
              </div>
              <div class="col-md-3" style="padding:2px;color:white;height:100%">
                <div style="background-color: #666666 ;padding:5px;height:100%">
                  <div class="title-size" style="height:50%;text-align:left;">Exp</div>
                  <div class="value-size" style="height:50%;">{{playerData[index].exp}}</div>
                </div>
              </div>
            </div>
            <div style="display:flex;align-items:center;height:20%;justify-content: space-around">
              <div class="col-md-12" style="padding:2px;color:white;height:100%">
                <div style="background-color: #666666 ;padding:5px;height:100%">
                  <div class="title-size" style="height:50%;text-align:left;">College</div>
                  <div class="value-size" style="height:50%;">{{playerData[index].college}}</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </template>

    </div>
    <div style="display:flex;height:100%;width:100%;">
      <ve-histogram width="100%" height="100%" :textStyle="textStyles" :extend="series" :data="TeamData" :legend="legend">
      </ve-histogram>
    </div>
  </div>

</div>
</template>
<style >
#selectSeason {
  background: #888888;
	height: 80%;
	width: 80%;
	color: white;
	padding:0 3%;
}
#selectSeason1 {
  background: #888888;
	height: 60%;
	width: 80%;
	color: white;
	padding:0 3%;
}
.player-card {
  padding: 5px;
  height: 100%;
  background-color: #f0f0f0;
  box-shadow: 2px 2px 10px rgb(0, 0, 0, .3);
}

.map1 {
  width: 100%;
  height: calc(100vh - 76px);
  padding: 3%;

}

.team-content {
  overflow: auto;
  width: 100%;
  height: 100%;
  background-color: rgb(253, 253, 253);
  /* border-radius:2%;  */
  box-shadow: 10px 10px 20px rgba(0, 0, 0, .1);

}

.content-head {

  height: 25%;
  background-color: #666666;

}

#selectYear1 {
  display: none;
  padding: 2px;

}

#showPlayer2 {
  display: none
}

#showPlayer3 {
  display: none
}

@media (max-width:960px) {
  #selectYear {
    display: none;
  }

  #selectYear1 {
    display: inherit;
  }

  #showPlayer1 {
    display: none
  }

  #showPlayer2 {
    display: block
  }
}

.team-name-size {
  font-size: 44px;
}

@media (max-width:620px) {
  .team-name-size {
    font-size: 28px;
  }

  .title-size {
    font-size: 14px
  }

  .value-size {
    font-size: 12px
  }

  #showPlayer2 {
    display: none
  }

  #showPlayer3 {
    display: block
  }
}
</style>
<script>
import player from "@/assets/json/player.json";
import {
  barChart
} from "@/assets/js/test.js";
export default {
  components: {},
  props: ['team'],
  data() {
    return {
      legend: {
        show: false
      },
      season: "2018-19",
      ...barChart,
      page: 0,
      windowWidth: 0,
      player: player,
      playerData: [

      ],
      TeamData: {
        columns: ['type', 'value'],
        rows: [{
            'type': 'MP',
            'value': this.team['2018-19'].stats['MP'][1]
          },
          {
            'type': 'FG',
            'value': this.team['2018-19'].stats['FG'][1]
          },
          {
            'type': 'FGA',
            'value': this.team['2018-19'].stats['FGA'][1]
          },
          {
            'type': '3P',
            'value': this.team['2018-19'].stats['3P'][1]
          },
          {
            'type': '3PA',
            'value': this.team['2018-19'].stats['3PA'][1]
          },
          {
            'type': '2P',
            'value': this.team['2018-19'].stats['2P'][1]
          },
          {
            'type': '2PA',
            'value': this.team['2018-19'].stats['2PA'][1]
          },
          {
            'type': 'FT',
            'value': this.team['2018-19'].stats['FT'][1]
          },
          {
            'type': 'FTA',
            'value': this.team['2018-19'].stats['FTA'][1]
          },
          {
            'type': 'ORB',
            'value': this.team['2018-19'].stats['ORB'][1]
          },
          {
            'type': 'DRB',
            'value': this.team['2018-19'].stats['DRB'][1]
          },
          {
            'type': 'TRB',
            'value': this.team['2018-19'].stats['TRB'][1]
          },
          {
            'type': 'AST',
            'value': this.team['2018-19'].stats['AST'][1]
          },
          {
            'type': 'STL',
            'value': this.team['2018-19'].stats['STL'][1]
          },
          {
            'type': 'BLK',
            'value': this.team['2018-19'].stats['BLK'][1]
          },
          {
            'type': 'TOV',
            'value': this.team['2018-19'].stats['TOV'][1]
          },
          {
            'type': 'PF',
            'value': this.team['2018-19'].stats['PF'][1]
          },
          {
            'type': 'PTS',
            'value': this.team['2018-19'].stats['PTS'][1]
          }
        ]
      },
      List: [{
          title: "排名",
          value: this.team['2018-19'].summary['Rank']
        },
        {
          title: "戰績",
          value: this.team['2018-19'].summary['Record']
        },
        {
          title: "教練",
          value: this.team['2018-19'].summary['Coach']
        },
        {
          title: "總管",
          value: this.team['2018-19'].summary['Executive']
        }

      ]
    };
  },
  methods: {
    selectSeason() {
      this.playerData = []
      this.season = document.getElementById("selectSeason").value
      this.List[0].value = this.team[this.season].summary['Rank']
      this.List[1].value = this.team[this.season].summary['Record']
      this.List[2].value = this.team[this.season].summary['Coach']
      this.List[3].value = this.team[this.season].summary['Executive']
      this.TeamData.rows[0].value = this.team[this.season].stats['MP'][1]
      this.TeamData.rows[1].value = this.team[this.season].stats['FG'][1]
      this.TeamData.rows[2].value = this.team[this.season].stats['FGA'][1]
      this.TeamData.rows[3].value = this.team[this.season].stats['3P'][1]
      this.TeamData.rows[4].value = this.team[this.season].stats['3PA'][1]
      this.TeamData.rows[5].value = this.team[this.season].stats['2P'][1]
      this.TeamData.rows[6].value = this.team[this.season].stats['2PA'][1]
      this.TeamData.rows[7].value = this.team[this.season].stats['FT'][1]
      this.TeamData.rows[8].value = this.team[this.season].stats['FTA'][1]
      this.TeamData.rows[9].value = this.team[this.season].stats['ORB'][1]
      this.TeamData.rows[10].value = this.team[this.season].stats['DRB'][1]
      this.TeamData.rows[11].value = this.team[this.season].stats['TRB'][1]
      this.TeamData.rows[12].value = this.team[this.season].stats['AST'][1]
      this.TeamData.rows[13].value = this.team[this.season].stats['STL'][1]
      this.TeamData.rows[14].value = this.team[this.season].stats['BLK'][1]
      this.TeamData.rows[15].value = this.team[this.season].stats['TOV'][1]
      this.TeamData.rows[16].value = this.team[this.season].stats['PF'][1]
      this.TeamData.rows[17].value = this.team[this.season].stats['PTS'][1]
      var i
      var j
      var pic_url

      var url = "url(" + this.team.pic_url + ")"
      document.getElementById('mapTeamLogo').style.backgroundImage = url


      for (i = 0; i < Object.keys(this.team[this.season].rosters['No.']).length; i++) {
        for (j = 0; j < this.player.length; j++) {
          if (this.team[this.season].rosters['Player'][i] == this.player[j].name) {
            pic_url = this.player[j].pic_url
          }
        }
        this.playerData.push({
          'pic_url': pic_url,
          'no': this.team[this.season].rosters['No.'][i],
          'player': this.team[this.season].rosters['Player'][i],
          'pos': this.team[this.season].rosters['Pos'][i],
          'ht': this.team[this.season].rosters['Ht'][i],
          'wt': this.team[this.season].rosters['Wt'][i],
          'birthDate': this.team[this.season].rosters['Birth Date'][i],
          'exp': this.team[this.season].rosters['Exp'][i],
          'college': this.team[this.season].rosters['College'][i]
        })

      }
    },
    selectSeason1() {
      this.playerData = []
      this.season = document.getElementById("selectSeason1").value
      this.List[0].value = this.team[this.season].summary['Rank']
      this.List[1].value = this.team[this.season].summary['Record']
      this.List[2].value = this.team[this.season].summary['Coach']
      this.List[3].value = this.team[this.season].summary['Executive']
      var i
      var j
      var pic_url

      var url = "url(" + this.team.pic_url + ")"
      document.getElementById('mapTeamLogo').style.backgroundImage = url


      for (i = 0; i < Object.keys(this.team[this.season].rosters['No.']).length; i++) {
        for (j = 0; j < this.player.length; j++) {
          if (this.team[this.season].rosters['Player'][i] == this.player[j].name) {
            pic_url = this.player[j].pic_url
          }
        }
        this.playerData.push({
          'pic_url': pic_url,
          'no': this.team[this.season].rosters['No.'][i],
          'player': this.team[this.season].rosters['Player'][i],
          'pos': this.team[this.season].rosters['Pos'][i],
          'ht': this.team[this.season].rosters['Ht'][i],
          'wt': this.team[this.season].rosters['Wt'][i],
          'birthDate': this.team[this.season].rosters['Birth Date'][i],
          'exp': this.team[this.season].rosters['Exp'][i],
          'college': this.team[this.season].rosters['College'][i]
        })

      }
    },
    left() {

      if (this.windowWidth >= 620 && this.windowWidth < 960) {
        if (this.page != 0) {
          this.page -= 2;
          // console.log("0");
        } else {
          // console.log("1");
        }
      } else if (this.windowWidth < 620) {
        if (this.page != 0) {
          this.page -= 1;
          // console.log("0");
        } else {
          // console.log("1");
        }
      } else {
        if (this.page != 0) {
          this.page -= 4;
          // console.log("0");
        } else {
          // console.log("1");
        }
      }

    },
    right() {

      if (this.windowWidth >= 620 && this.windowWidth < 960) {
        if (this.page + 2 < this.playerData.length) {
          // console.log("0");
          this.page += 2;
        }

      } else if (this.windowWidth < 620) {
        if (this.page + 1 < this.playerData.length) {
          // console.log("0");
          this.page += 1;
        }
      } else {
        if (this.page + 4 < this.playerData.length) {
          // console.log("0");
          this.page += 4;
        }

      }
    },
    close() {
      this.$emit('close', false);
    }
  },
  mounted() {

    this.windowWidth = window.innerWidth;
    var i
    var j
    var pic_url

    var url = "url(" + this.team.pic_url + ")"
    document.getElementById('mapTeamLogo').style.backgroundImage = url


    for (i = 0; i < Object.keys(this.team[this.season].rosters['No.']).length; i++) {
      for (j = 0; j < this.player.length; j++) {
        if (this.team[this.season].rosters['Player'][i] == this.player[j].name) {
          pic_url = this.player[j].pic_url
        }
      }
      this.playerData.push({
        'pic_url': pic_url,
        'no': this.team[this.season].rosters['No.'][i],
        'player': this.team[this.season].rosters['Player'][i],
        'pos': this.team[this.season].rosters['Pos'][i],
        'ht': this.team[this.season].rosters['Ht'][i],
        'wt': this.team[this.season].rosters['Wt'][i],
        'birthDate': this.team[this.season].rosters['Birth Date'][i],
        'exp': this.team[this.season].rosters['Exp'][i],
        'college': this.team[this.season].rosters['College'][i]
      })

    }
  }
};
</script>
