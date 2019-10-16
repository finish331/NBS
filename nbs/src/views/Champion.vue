<template>
  <div class="champion px-5">
    <!-- 左半部 -->
    <div class="col-sm-12 col-md-3 left-champion" style="padding-right:0;padding-left:0">
      <div style="height:10%;display:flex;align-items: center;justify-content: center">
        <div class="btn-team" @click="change()">{{content}}</div>
      </div>
      <div class="col-sm-12 col-md-12 champion-left">
        <div class="row" v-for="(i,key,index) in expectData['2018-19']" :key="index">
          <div class="col-md-12 test">
            <div class="col-md-6 bgimg"></div>
            <div class="col-md-6 test1" style="word-break: break-all;" v-if="content=='預測排名'">
              #{{index+1}}
              <br />
              {{key}}
            </div>
            <div class="col-md-6 test1" style="word-break: break-all;" v-if="content=='實際排名'">
              #{{index+1}}
              <br />
              {{i}}
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- 右半部 -->
    <div class="col-sm-12 col-md-9 champion-right">
      <!-- 左邊隊伍 -->
      <div class="col-sm-12 col-md-6 left-team">
        <!-- 球隊下拉選單 -->
        <div style="height:5%">
          <form style="height:100%">
            <select
              style="background:#2f2f2f;color:white;padding:0 12px"
              name="selectLeftTeam"
              id="selectLeftTeam"
              @change="print_value(0)"
            >
              <option v-for="(i, index) in teamData" :key="index" :value="index">{{i.name}}</option>
            </select>
          </form>
        </div>

        <!-- 球隊LOGO -->
        <div id="left-team-logo" style="height:30%" @click="clickTeam('left')"></div>

        <div style="display:flex;width:100%;height:20%;align-items:center;padding:0 5%">
          <div
            class="col player-btn"
            style="height:100%;padding:0;"
            v-for="(i, index) in leftTeam.player"
            :key="index"
          >
            <div
              @click="clickPlayer(index,0)"
              style="height:100%;width:100%;background-color: #272727;display:flex; align-items:center "
              v-if="i.state"
            >
              <div class="playerName">
                <div style="height:60%;display:flex; align-items:flex-end">
                  <img :src="i.pic_url" class="img-player" />
                </div>
                <div>
                  {{i.name.split(" ")[0]}}
                  <br />
                  {{i.name.split(" ")[1]}}
                </div>
              </div>
            </div>
            <div
              @click="clickPlayer(index,0)"
              style="height:100%;display:flex; align-items:center "
              v-else
            >
              <div class="playerName">
                <div style="height:60%;display:flex; align-items:flex-end">
                  <img :src="i.pic_url" class="img-player" />
                </div>
                <div>
                  {{i.name.split(" ")[0]}}
                  <br />
                  {{i.name.split(" ")[1]}}
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- 圖表 -->
        <div style="width:100%;height:45%">
          <!-- 球隊圖表 -->
          <div style="width:100%;height:100%;" v-if="leftTeam.isTeam">
            <ve-bar
              :yAxis="yAxis"
              height="100%"
              :xAxis="xAxis"
              :legend="radarLegend"
              :textStyle="textStyles"
              :data="leftTeamDate"
              :extend="leftseries"
            ></ve-bar>
          </div>
          <!-- 球員圖表 -->
          <div style="width:100%;height:100%" v-else>
            <ve-bar
              :yAxis="yAxis"
              height="100%"
              :xAxis="xAxis"
              :textStyle="textStyles"
              :data="leftPlayerData"
              :extend="leftseries"
              :legend="radarLegend"
            ></ve-bar>
          </div>
        </div>
      </div>
      <!-- 右邊隊伍 -->
      <div class="col-sm-12 col-md-6 right-team">
        <!-- 球隊下拉選單 -->
        <div style="height:5%">
          <form style="height:100%">
            <select
              style="background:#2f2f2f;
          color:white;padding:0 12px;"
              name="selectRightTeam"
              id="selectRightTeam"
              @change="print_value(1)"
            >
              <option v-for="(i, index) in teamData" :key="index" :value="index">{{i.name}}</option>
            </select>
          </form>
        </div>
        <!-- 球隊LOGO -->
        <div id="right-team-logo" style="height:30%" @click="clickTeam('right')"></div>

        <div style="display:flex;width:100%;height:20%;padding:0 5%">
          <div
            class="col player-btn"
            style="height:100%;padding:0;"
            v-for="(i, index) in rightTeam.player"
            :key="index"
          >
            <div
              @click="clickPlayer(index,1)"
              style="height:100%;background-color: #272727;display:flex; align-items:center;justify-content: center "
              v-if="i.state"
            >
              <div class="playerName">
                <div style="height:60%;display:flex; align-items:flex-end">
                  <img :src="i.pic_url" width="100%" class="img-player" />
                </div>
                <div>
                  {{i.name.split(" ")[0]}}
                  <br />
                  {{i.name.split(" ")[1]}}
                </div>
              </div>
            </div>
            <div
              @click="clickPlayer(index,1)"
              style="height:100%;display:flex; align-items:center; "
              v-else
            >
              <div class="playerName">
                <div style="height:60%;display:flex; align-items:flex-end">
                  <img :src="i.pic_url" class="img-player" />
                </div>
                <div>
                  {{i.name.split(" ")[0]}}
                  <br />
                  {{i.name.split(" ")[1]}}
                </div>
              </div>
            </div>
          </div>
        </div>

        <div style="width:100%;height:45%">
          <!-- 球隊圖表 -->
          <div style="width:100%;height:100%;" v-if="rightTeam.isTeam">
            <ve-bar
              height="100%"
              :xAxis="xAxiss"
              :textStyle="textStyles"
              :legend="radarLegend"
              :yAxis="yAxiss"
              :data="rightTeamDate"
              :settings="rightseries"
            ></ve-bar>
          </div>
          <!-- 球員圖表 -->
          <div style="width:100%;height:100%" v-else>
            <ve-bar
              height="100%"
              :xAxis="xAxiss"
              :textStyle="textStyles"
              :legend="radarLegend"
              :yAxis="yAxiss"
              :data="rightPlayerData"
              :settings="rightseries"
            ></ve-bar>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import {lineChart} from "@/assets/js/championConfig.js";
import teamData from "@/assets/json/team.json";
import expectData from "@/assets/json/expect.json";

import playerData from "@/assets/json/player.json";
export default {
  components: {},
  data() {
    return {
      content: "預測排名",
      expectData:expectData,
      xAxiss:[
        {
          axisLabel:{
                fontSize:10
              }
        }
      ],
      playerData:playerData,
      teamData:teamData,
      ...lineChart,
      yAxiss: [
        {
            offset:4,
            data: ['抄截','火鍋','助攻','籃板','得分'],
        }],
        yAxis: [
        {
          offset:5,
          position: 'right',
            data: ['STL','BLK','AST','TRB','PTS'],
        }],
      leftTeamDate: {
        columns: ['type', 'value'],
        rows: [{
            'type': 'STL',
            'value': 3.1
          },
          {
            'type': 'BLK',
            'value': 3
          },
          {
            'type': 'AST',
            'value': 5.3
          },
          {
            'type': 'TRB',
            'value': 5
          },
          {
            'type': 'PTS',
            'value': 1
          }
        ]
      },
      rightTeamDate: {
        columns: ['type', 'value'],
        rows: [{
            'type': '抄截',
            'value': 3.1
          },
          {
            'type': '火鍋',
            'value': 3
          },
          {
            'type': '助攻',
            'value': 5.3
          },
          {
            'type': '籃板',
            'value': 5
          },
          {
            'type': '得分',
            'value': 1
          }
        ]
      },
      leftPlayerData: {
        columns: ['type', 'value'],
        rows: [{
            'type': 'STL',
            'value': 3.1
          },
          {
            'type': 'BLK',
            'value': 3
          },
          {
            'type': 'AST',
            'value': 5.3
          },
          {
            'type': 'TRB',
            'value': 5
          },
          {
            'type': 'PTS',
            'value': 1
          }
        ]
      },
      rightPlayerData: {
        columns: ['type', 'value'],
        rows: [{
            'type': '抄截',
            'value': 3.1
          },
          {
            'type': '火鍋',
            'value': 3
          },
          {
            'type': '助攻',
            'value': 5.3
          },
          {
            'type': '籃板',
            'value': 5
          },
          {
            'type': '得分',
            'value': 1
          }
        ]
      },
      rightTeam: {
        isTeam: true,
        index: 0 ,
        img:teamData[0].pic_url,
        team: {
          se: teamData[0]['2018-19']['stats']['STL'][1],
          sassad: teamData[0]['2018-19']['stats']['BLK'][1],
          sc: teamData[0]['2018-19']['stats']['AST'][1],
          bc: teamData[0]['2018-19']['stats']['TRB'][1],
          aa: teamData[0]['2018-19']['stats']['PTS'][1]
        },
        player: [{
            pic_url:'',
            state: false,
            name: "player1",
            PTS: 6.1,
            TRB: 6.6,
            AST: 7.5,
            BLK: 0.7,
            STL: 2.0
          },
          {
            pic_url:'',

            state: false,
            name: "player2",
            PTS: 36.1,
            TRB: 6,
            AST: 7.5,
            BLK: 0.7,
            STL: 2.0
          },
          {
            pic_url:'',
            state: false,
            name: "player3",
            PTS: 3.1,
            TRB: 7.6,
            AST: 7.5,
            BLK: 0.7,
            STL: 2.0
          },
          {
            pic_url:'',
            state: false,
            name: "player4",
            PTS: 8.1,
            TRB: 8.6,
            AST: 7.5,
            BLK: 0.7,
            STL: 2.0
          },
          {
            pic_url:'',

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
          se: teamData[0]['2018-19']['stats']['STL'][1],
          sassad: teamData[0]['2018-19']['stats']['BLK'][1],
          sc: teamData[0]['2018-19']['stats']['AST'][1],
          bc: teamData[0]['2018-19']['stats']['TRB'][1],
          aa: teamData[0]['2018-19']['stats']['PTS'][1]
        },
        player: [{
          pic_url:'',

            state: false,
            name: "player1",
            PTS: 6.1,
            TRB: 6.6,
            AST: 7.5,
            BLK: 0.7,
            STL: 2.0
          },
          {
            pic_url:'',

            state: false,
            name: "player2",
            PTS: 36.1,
            TRB: 6,
            AST: 7.5,
            BLK: 0.7,
            STL: 2.0
          },
          {
            pic_url:'',

            state: false,
            name: "player3",
            PTS: 3.1,
            TRB: 7.6,
            AST: 7.5,
            BLK: 0.7,
            STL: 2.0
          },
          {
            pic_url:'',

            state: false,
            name: "player4",
            PTS: 8.1,
            TRB: 8.6,
            AST: 7.5,
            BLK: 0.7,
            STL: 2.0
          },
          {
            pic_url:'',

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
    // console.log(Object.keys(this.expectData['2018-19']))
    this.changeImg()
    // console.log(this.teamData[0]['2018-19']['stats']['PTS'][1])
    this.clickTeam('left');
    this.clickTeam('right');
    var url="url("+this.rightTeam.img+")"
    document.getElementById('left-team-logo').style.backgroundImage = url
    document.getElementById('right-team-logo').style.backgroundImage = url
    this.leftplayer()
     this.rightplayer()
    // console.log(leftPlayerTemp)
  },
  methods: {
    
    change(){
      if(this.content=='預測排名'){
        this.content='實際排名'
        this.changeImg()
      }
      else{
        this.content='預測排名'
        this.changeImg()
      }
      
    },
    changeImg(){
       var temp=document.getElementsByClassName('bgimg')   
        var i
        var j
        var tempURL
        // console.log(this.content);
        
        for(i=0;i<Object.keys(this.expectData['2018-19']).length;i++){
          for(j=0;j<this.teamData.length;j++){
            if(this.content=='預測排名'){

                  if(this.teamData[j].name==Object.keys(this.expectData['2018-19'])[i]){
                  tempURL="url("+this.teamData[j].pic_url+")"
                  temp[i].style.backgroundImage = tempURL
              }
            }
            else if(this.content=='實際排名'){


              if(this.teamData[j].name==this.expectData['2018-19'][Object.keys(this.expectData['2018-19'])[i]]){
                tempURL="url("+this.teamData[j].pic_url+")"
                temp[i].style.backgroundImage = tempURL
              }
            }
          }
        }
    },
    leftplayer(){
      var leftPlayerTemp=[]
      var i
      var j
      for(i=0;i<Object.keys(this.teamData[this.leftTeam.index]['2018-19'].rosters.Player).length;i++){
        leftPlayerTemp.push({pic_url:'',name:this.teamData[this.leftTeam.index]['2018-19'].rosters.Player[i],MP:0,PTS:0, TRB: 0, AST: 0, BLK: 0, STL: 0})
      }

      for(i=0;i<this.playerData.length;i++){
        for(j=0;j<Object.keys(this.teamData[this.leftTeam.index]['2018-19'].rosters.Player).length;j++){
          if(this.playerData[i].name==this.teamData[this.leftTeam.index]['2018-19'].rosters.Player[j]){
            if(this.playerData[i]['data']!=undefined){
              leftPlayerTemp[j].pic_url=this.playerData[i].pic_url
              leftPlayerTemp[j].MP=this.playerData[i]['data'].MP[Object.keys(this.playerData[i]['data'].MP).length-2]
              leftPlayerTemp[j].PTS=this.playerData[i]['data'].PTS[Object.keys(this.playerData[i]['data'].PTS).length-2]
              leftPlayerTemp[j].TRB=this.playerData[i]['data'].TRB[Object.keys(this.playerData[i]['data'].TRB).length-2]
              leftPlayerTemp[j].AST=this.playerData[i]['data'].AST[Object.keys(this.playerData[i]['data'].AST).length-2]
              leftPlayerTemp[j].BLK=this.playerData[i]['data'].BLK[Object.keys(this.playerData[i]['data'].BLK).length-2]
              leftPlayerTemp[j].STL=this.playerData[i]['data'].STL[Object.keys(this.playerData[i]['data'].STL).length-2]
            }
          }
        }
      }

      var temp
      for(i=0;i<leftPlayerTemp.length;i++){
        for(j=i+1;j<leftPlayerTemp.length;j++){
          if(leftPlayerTemp[i].MP<leftPlayerTemp[j].MP){
            temp=leftPlayerTemp[i]
            leftPlayerTemp[i]=leftPlayerTemp[j]
            leftPlayerTemp[j]=temp
          }
        }
    }
    for(i=0;i<5;i++){
      this.leftTeam.player[i].pic_url=leftPlayerTemp[i].pic_url
      this.leftTeam.player[i].name=leftPlayerTemp[i].name
      this.leftTeam.player[i].PTS=leftPlayerTemp[i].PTS
      this.leftTeam.player[i].TRB=leftPlayerTemp[i].TRB
      this.leftTeam.player[i].AST=leftPlayerTemp[i].AST
      this.leftTeam.player[i].BLK=leftPlayerTemp[i].BLK
      this.leftTeam.player[i].STL=leftPlayerTemp[i].STL

    }
    },
    rightplayer(){
    var rightPlayerTemp=[]
    var i
    var j
    for(i=0;i<Object.keys(this.teamData[this.rightTeam.index]['2018-19'].rosters.Player).length;i++){
      rightPlayerTemp.push({pic_url:'',name:this.teamData[this.rightTeam.index]['2018-19'].rosters.Player[i],MP:0,PTS:0, TRB: 0, AST: 0, BLK: 0, STL: 0})
    }

    for(i=0;i<this.playerData.length;i++){
      for(j=0;j<Object.keys(this.teamData[this.rightTeam.index]['2018-19'].rosters.Player).length;j++){
        if(this.playerData[i].name==this.teamData[this.rightTeam.index]['2018-19'].rosters.Player[j]){
          if(this.playerData[i]['data']!=undefined){
            rightPlayerTemp[j].pic_url=this.playerData[i].pic_url
            rightPlayerTemp[j].MP=this.playerData[i]['data'].MP[Object.keys(this.playerData[i]['data'].MP).length-2]
            rightPlayerTemp[j].PTS=this.playerData[i]['data'].PTS[Object.keys(this.playerData[i]['data'].PTS).length-2]
            rightPlayerTemp[j].TRB=this.playerData[i]['data'].TRB[Object.keys(this.playerData[i]['data'].TRB).length-2]
            rightPlayerTemp[j].AST=this.playerData[i]['data'].AST[Object.keys(this.playerData[i]['data'].AST).length-2]
            rightPlayerTemp[j].BLK=this.playerData[i]['data'].BLK[Object.keys(this.playerData[i]['data'].BLK).length-2]
            rightPlayerTemp[j].STL=this.playerData[i]['data'].STL[Object.keys(this.playerData[i]['data'].STL).length-2]
          }
        }
      }
    }
    var temp
    for(i=0;i<rightPlayerTemp.length;i++){
      for(j=i+1;j<rightPlayerTemp.length;j++){
        if(rightPlayerTemp[i].MP<rightPlayerTemp[j].MP){
          temp=rightPlayerTemp[i]
          rightPlayerTemp[i]=rightPlayerTemp[j]
          rightPlayerTemp[j]=temp
        }
      }
    }
    for(i=0;i<5;i++){
      this.rightTeam.player[i].pic_url=rightPlayerTemp[i].pic_url
      this.rightTeam.player[i].name=rightPlayerTemp[i].name
      this.rightTeam.player[i].PTS=rightPlayerTemp[i].PTS
      this.rightTeam.player[i].TRB=rightPlayerTemp[i].TRB
      this.rightTeam.player[i].AST=rightPlayerTemp[i].AST
      this.rightTeam.player[i].BLK=rightPlayerTemp[i].BLK
      this.rightTeam.player[i].STL=rightPlayerTemp[i].STL

    }
    },
    print_value(i){
      var url
      if(i==0){
        this.leftTeam.index=document.getElementById("selectLeftTeam").value
        this.leftplayer()
        this.leftTeam.team.aa=this.teamData[this.leftTeam.index]['2018-19']['stats']['PTS'][1]
        this.leftTeam.team.bc=this.teamData[this.leftTeam.index]['2018-19']['stats']['TRB'][1]
        this.leftTeam.team.sc=this.teamData[this.leftTeam.index]['2018-19']['stats']['AST'][1]
        this.leftTeam.team.sassad=this.teamData[this.leftTeam.index]['2018-19']['stats']['BLK'][1]
        this.leftTeam.team.se=this.teamData[this.leftTeam.index]['2018-19']['stats']['STL'][1]
        this.clickTeam('left')
        this.leftTeam.img=teamData[this.leftTeam.index].pic_url
        url="url("+this.leftTeam.img+")"
        document.getElementById('left-team-logo').style.backgroundImage = url
      }
      else{
        this.rightTeam.index=document.getElementById("selectRightTeam").value
        this.rightplayer()
        this.rightTeam.team.aa=this.teamData[this.rightTeam.index]['2018-19']['stats']['PTS'][1]
        this.rightTeam.team.bc=this.teamData[this.rightTeam.index]['2018-19']['stats']['TRB'][1]
        this.rightTeam.team.sc=this.teamData[this.rightTeam.index]['2018-19']['stats']['AST'][1]
        this.rightTeam.team.sassad=this.teamData[this.rightTeam.index]['2018-19']['stats']['BLK'][1]
        this.rightTeam.team.se=this.teamData[this.rightTeam.index]['2018-19']['stats']['STL'][1]
        this.clickTeam('right')
        this.rightTeam.img=teamData[this.rightTeam.index].pic_url
        url="url("+this.rightTeam.img+")"
        document.getElementById('right-team-logo').style.backgroundImage = url
      }
    },
    clickPlayer(i, lr) {
      if (lr == 0) {
        this.leftTeam.isTeam = false;
        this.leftTeam.player[i].state = true;
        this.leftPlayerData.rows[0].value = this.leftTeam.player[i].STL;
        this.leftPlayerData.rows[1].value = this.leftTeam.player[i].BLK;
        this.leftPlayerData.rows[2].value = this.leftTeam.player[i].AST;
        this.leftPlayerData.rows[3].value = this.leftTeam.player[i].TRB;
        this.leftPlayerData.rows[4].value = this.leftTeam.player[i].PTS;
        for (var j = 0; j < this.leftTeam.player.length; j++) {
          if (i !== j) {
            this.leftTeam.player[j].state = false;
          }
        }
      } else {
        this.rightTeam.isTeam = false;
        this.rightTeam.player[i].state = true;
        this.rightPlayerData.rows[0].value = this.rightTeam.player[i].STL;
        this.rightPlayerData.rows[1].value = this.rightTeam.player[i].BLK;
        this.rightPlayerData.rows[2].value = this.rightTeam.player[i].AST;
        this.rightPlayerData.rows[3].value = this.rightTeam.player[i].TRB;
        this.rightPlayerData.rows[4].value = this.rightTeam.player[i].PTS;
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
        this.leftTeamDate.rows[0].value = this.leftTeam.team.se;
        this.leftTeamDate.rows[1].value = this.leftTeam.team.sassad;
        this.leftTeamDate.rows[2].value = this.leftTeam.team.sc;
        this.leftTeamDate.rows[3].value = this.leftTeam.team.bc
        this.leftTeamDate.rows[4].value = this.leftTeam.team.aa;

        for (var j = 0; j < this.leftTeam.player.length; j++) {

          this.leftTeam.player[j].state = false;

        }
      }
      else{
        this.rightTeam.isTeam = true;
        this.rightTeamDate.rows[0].value = this.rightTeam.team.se;
        this.rightTeamDate.rows[1].value = this.rightTeam.team.sassad;
        this.rightTeamDate.rows[2].value = this.rightTeam.team.sc;
        this.rightTeamDate.rows[3].value = this.rightTeam.team.bc
        this.rightTeamDate.rows[4].value = this.rightTeam.team.aa;

        for (j = 0; j < this.rightTeam.player.length; j++) {

          this.rightTeam.player[j].state = false;

        }
      }

    }
  }
};
</script>
<style>
.left-champion{
  height: 100%;
}
.btn-team {
  cursor: pointer;
  width: 100%;
  height: 50%;
  border-radius: 5px;
  background: #3e3e3e;
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  transition: 0.1s all;
}
.btn-team:hover {
  background: #727272;
  transition: 0.1s all;
}
.img-player {
  width: 100%;
  max-height: 100%;
}
#left-team-logo {
  cursor: pointer;
  width: 100%;
  height: 40%;
  filter: drop-shadow(0px 0px 10px rgba(0, 0, 0, 0.5));
  background-size: contain;
  background-image: url(https://stats.nba.com/media/img/teams/logos/HOU_logo.svg);
  background-position: center;
  background-repeat: no-repeat;
}
#right-team-logo {
  cursor: pointer;
  width: 100%;
  height: 40%;
  filter: drop-shadow(0px 0px 10px rgba(0, 0, 0, 0.5));
  background-size: contain;
  background-image: url(https://stats.nba.com/media/img/teams/logos/HOU_logo.svg);
  background-position: center;
  background-repeat: no-repeat;
}
#selectLeftTeam {
  background: #fff;
  color: #1d1d1d;
  height: 100%;
}
#selectRightTeam {
  background: #fff;
  color: #1d1d1d;
  height: 100%;
}
.champion {
  display: flex;
  height: calc(100vh - 76px);
  width: 100%;
}
.champion-left {
  width: 100%;
  padding: 0;
  height: 90%;
  overflow: auto;
}
.champion-right {
  height: 100%;
  display: flex;
}
.test {
  display: flex;
  margin: 10px 0;
  padding: 0;
  /* height: 100%; */
  background: linear-gradient(to right, #1d1d1d, black);
  box-shadow: 5px 5px 5px rgb(29, 29, 29, 0.75);
}

.bgimg {
  width: 100%;
  /* background: url('../assets/GSW_logo.svg'); */
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  opacity: 1;
}

.test1 {
  /* padding: 5% 0; */
  color: white;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  font-size: 10px;
  font-weight: bold;
}

.left-team {
  color: white;
  background-color: #1d1d1d;
  /* border: 12px solid white; */
  padding: 2% 0;
  height: 100%;
}

.right-team {
  color: white;
  background-color: #1d1d1d;
  padding: 2% 0;
  /* border: 12px solid white; */
  height: 100%;
}

.player-btn {
  cursor: pointer;
}

.player-btn:hover {
  background-color: #272727;
}
@media (max-width: 960px) {
  .champion {
    display: block;
  }
  .left-champion {
    height: 90vh;
  }
  .left-team {
    display: none;
  }
}
.playerName {
  padding: 3%;
  font-size: 10px;
  height: 100%;
  word-break: break-all;
}
@media (max-width: 430px) {
  .playerName {
    font-size: 10px;
  }
  #selectLeftTeam {
    background: #fff;
    color: #1d1d1d;
    font-size: 10px;
  }
  #selectRightTeam {
    background: #fff;
    color: #1d1d1d;
    font-size: 10px;
  }
}
</style>