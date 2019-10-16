<template >

    <div style="height:100%;width:100%;">
      <div class="mvp-player">
        <div class="mvp-bg">
        </div>
        <div class="mvp-player-content">
            <img :src=player.pic_url alt="" height="100%">
        </div>
      </div>
      <div class="mvp-name">
        {{player.name}}
        <v-icon style="color:yellow" v-if="index==0">emoji_events</v-icon>
        <v-icon style="color:#d6d6d6" v-if="index==1">emoji_events</v-icon>
        <v-icon style="color:#c58354" v-if="index==2">emoji_events</v-icon>

      </div>
      <div class="mvp-radar" @mouseover="over()" @mouseleave="leave()">
        <ve-radar
          :radar="radars"
          :tooltip="tooltip"
          :legend="radarLegend"
          :data="chartData"
          :settings="radarSettings"
          height="100%"
          width="100%"
        ></ve-radar>
      </div>
      <div class="mvp-radar">
        <ve-line
          height="100%"
          width="100%"
          :textStyle="textStyles"
          :grid="grids"
          :visual-map="visualMaps"
          :judge-width="true"
          :data="pointsData"
          :legend="legendSetting"
          :extend="chartExtend"
          :settings="chartSettings"
        ></ve-line>
      </div>
    </div>
</template>

<script>
import teamData from "@/assets/json/team.json";
import { lineChart } from "@/assets/js/playerConfig.js";
export default {
  props: ["player", "index"],
  data() {
    return {
      grids: {
        top: 50,
        bottom: 30
      },
      ...lineChart,
      pointsData: {
        columns: ["season", "points"],
        rows: []
      },
      visualMaps: [
        {
          show: false,
          type: "continuous",
          splitNumber: 5,
          min: 0,
          max: 40,
          right: 0,
          top: "50%",
          precision: 1,
          inRange: {
            color: ["#63aabc", "#daf1f9", "#fb9935", "#b90b0b"]
          },
          textStyle: {
            color: "white"
          }
        }
      ],
      chartData: {
        columns: ["seasons", "PTS", "TRB", "AST", "BLK", "STL"],
        rows: [
          {
            seasons: "",
            PTS: "",
            TRB: "",
            AST: "",
            BLK: "",
            STL: ""
          }
        ]
      },
      radars: {
					indicator: [
					{ name: "PTS", max: 5},
					{ name: "TRB", max: 5 },
					{ name: "AST", max: 5 },
					{ name: "BLK", max: 5 },
					{ name: "STL", max: 5 }
					],
					center: ['50%', '55%'],
					name: {
					color: "white",
					fontSize: 12
					}
				},
      teamData: teamData
    };
  },
  mounted: function() {
    var i;
    var j;
    var url;
    var pointTemp;
    var pointIndexTemp;
    var temp1 = { season: "", points: "" };
    var temp = document.getElementsByClassName("mvp-bg");
    for (i = 0; i < this.teamData.length; i++) {
      if (this.player.team == this.teamData[i].name) {
        url = "url(" + this.teamData[i].pic_url + ")";
        temp[this.index].style.backgroundImage = url;
      }
    }
    for (i = 0; i < Object.keys(this.player.data.PTS).length; i++) {
      if (
        this.player.data["Season"][i] != null &&
        this.player.data["Season"][i].search("season") == -1
      ) {
        if (
          i != 0 &&
          this.player.data["Season"][i] != this.player.data["Season"][i - 1]
        ) {
          temp1.season = this.player.data["Season"][i];
          this.pointsData.rows.push({ season: temp1.season, points: "" });
        } else if (i == 0) {
          temp1.season = this.player.data["Season"][i];
          this.pointsData.rows.push({ season: temp1.season, points: "" });
        }
      }
    }
    for (i = 0; i < this.pointsData.rows.length; i++) {
      pointTemp = 0;
      pointIndexTemp = 0;
      for (j = 0; j < Object.keys(this.player.data["Season"]).length; j++) {
        if (this.pointsData.rows[i].season == this.player.data["Season"][j]) {
          pointIndexTemp++;
          if (this.player.data.PTS[j].toString().search("Did Not Play")) {
            pointTemp += Number(this.player.data.PTS[j]);
          }
        }
      }
      this.pointsData.rows[i].points = (pointTemp / pointIndexTemp).toFixed(1);
    }
    this.chartData.rows[0].seasons = this.player.data["Season"][
      Object.keys(this.player.data["Season"]).length - 2
    ];
    this.level(
      this.player.data.PTS[Object.keys(this.player.data.PTS).length - 2],
      this.player.data.TRB[Object.keys(this.player.data.TRB).length - 2],
      this.player.data.AST[Object.keys(this.player.data.AST).length - 2],
      this.player.data.BLK[Object.keys(this.player.data.BLK).length - 2],
      this.player.data.STL[Object.keys(this.player.data.STL).length - 2]
    );
    // console.log(this.playerData);
  },
  methods: {
    leave(){
				this.radars.indicator[0].name='PTS'
				this.radars.indicator[1].name='TRB'
				this.radars.indicator[2].name='AST'
				this.radars.indicator[3].name='BLK'
				this.radars.indicator[4].name='STL'
			},
			over(){
				this.radars.indicator[0].name='得分'
				this.radars.indicator[1].name='籃板'
				this.radars.indicator[2].name='助攻'
				this.radars.indicator[3].name='火鍋'
				this.radars.indicator[4].name='抄截'
				
			},
    level(PTS, TRB, AST, BLK, STL) {
      if(PTS==0){
					this.chartData.rows[0].PTS=0
				}
				else if(PTS>0&&PTS<=6.9){
					this.chartData.rows[0].PTS=1
				}
				else if(PTS>6.9&&PTS<=11.7){
					this.chartData.rows[0].PTS=2
				}
				else if(PTS>11.7&&PTS<=17.4){
					this.chartData.rows[0].PTS=3
				}
				else if(PTS>17.4&&PTS<=23.1){
					this.chartData.rows[0].PTS=3
				}
				else{
					this.chartData.rows[0].PTS=5
				}

				if(TRB==0){
					this.chartData.rows[0].TRB=0
				}
				else if(TRB>0&&TRB<=3){
					this.chartData.rows[0].TRB=1
				}
				else if(TRB>3&&TRB<=4.7){
					this.chartData.rows[0].TRB=2
				}
				else if(TRB>4.7&&TRB<=6.4){
					this.chartData.rows[0].TRB=3
				}
				else if(TRB>6.4&&TRB<=8.1){
					this.chartData.rows[0].TRB=4
				}
				else{
					this.chartData.rows[0].TRB=5
				}

				if(AST==0){
					this.chartData.rows[0].AST=0
				}
				else if(AST>0&&AST<=2.9){
					this.chartData.rows[0].AST=1
				}
				else if(AST>2.9&&AST<=4.6){
					this.chartData.rows[0].AST=2
				}
				else if(AST>4.6&&AST<=6.3){
					this.chartData.rows[0].AST=3
				}
				else if(AST>6.3&&AST<=8){
					this.chartData.rows[0].AST=4
				}
				else{
					this.chartData.rows[0].AST=5
				}

				if(BLK==0){
					this.chartData.rows[0].BLK=0
				}
				else if(BLK>0&&BLK<=0.3){
					this.chartData.rows[0].BLK=1
				}
				else if(BLK>0.3&&BLK<=0.7){
					this.chartData.rows[0].BLK=2
				}
				else if(BLK>0.7&&BLK<=1.1){
					this.chartData.rows[0].BLK=3
				}
				else if(BLK>1.1&&BLK<=1.5){
					this.chartData.rows[0].BLK=4
				}
				else{
					this.chartData.rows[0].BLK=5
				}

				if(STL==0){
					this.chartData.rows[0].STL=0
				}
				else if(STL>0&&STL<=0.3){
					this.chartData.rows[0].STL=1
				}
				else if(STL>0.3&&STL<=0.7){
					this.chartData.rows[0].STL=2
				}
				else if(STL>0.7&&STL<=1.1){
					this.chartData.rows[0].STL=3
				}
				else if(STL>1.1&&STL<=1.5){
					this.chartData.rows[0].STL=4
				}
				else{
					this.chartData.rows[0].STL=5
				}
    }
  }
};
</script>

<style >
.mvp-bg {
  width: 100%;
  height: 100%;
  /* background-image: url("https://stats.nba.com/media/img/teams/logos/ATL_logo.svg"); */
  background-size: cover;
  background-position: center;
  opacity: 0.5;
}
.mvp-player {
  position: relative;
  width: 100%;
  height: 20%;
  font-size: 20px;
  color: white;
  font-weight: 800;
  background: #666;
  /* padding:0 2%; */
}
.mvp-player-content {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
}
.mvp-name {
  display: flex;
  width: 100%;
  height: 5%;
  background: #1d1d1d;
  font-size: 20px;
  color: white;
  font-weight: 800;
  justify-content: center;
  align-items: center
}
@media (max-width:440px){
  .mvp-name {
  font-size: 14px;
  }
}
.mvp-radar {
  width: 100%;
  height: 35.5%;
  background: #666;
  margin-top: 2%;
}

</style>
