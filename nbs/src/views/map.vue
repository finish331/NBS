<template>
<<<<<<< HEAD
	<div class="container page-height px-5">
		<div class="row mh-100 vh-100 align-items-center" >
      <ve-map class="col" :extend="series" :legend="radarLegend" :events="{ click: clickHandler.bind(this, 1) }" width="100%" height="600px" :data="chartData" :settings="chartSettings"></ve-map>
    </div>
=======
	<div style="position: relative;">
    <div class="container page-height px-5" style="position: relative;">
      <div id="selectTeam" v-if=showSelectTeam>
        
        <div style="position: relative;height:100%;widht:100%;background:#f4f4f4;box-shadow:5px 5px 10px  rgb(29, 29, 29,.1);z-index:11;padding:5%">
          <button @click="close" style="position: absolute;z-index:9999;top:5px;right:5px" ><v-icon style="font-size:30px">cancel</v-icon></button>
          <div class="showTeam">
            <div  class="col-sm-4 col-md-3 team hover" v-for="(j, index1) in team[teamName]" :key="index1">
              <div   style="cursor: pointer;width:100%;height:0;padding-bottom:80%;position: relative;" >
                  <div v-for="(i, index) in teamData" :key="index">
                      <img @click="setTeam(index)" :teamIndex=index :src=i.pic_url alt="" style="width:80%;position: absolute;top:0px;left:10%;" v-if="j==i.name"> 
                  </div>
              </div>
              <div style="cursor: pointer;" >
                    {{j}}
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="row mh-100 vh-100 align-items-center" >
        <ve-map class="col"  :events="{ click: clickHandler.bind(this, 1) }" width="80%" height="600px" :data="chartData" :settings="chartSettings"></ve-map>
      </div>
    
>>>>>>> 9fc78a91cdce5c5562e3987a6dfa51d5841b0341
	</div>
  <div id="testttttt"  v-if="showTeam">
    <map1 :team="teamData[teamIndex]"  @close="parentClose"/>  
  </div>
  
  </div>
</template>

<script>
<<<<<<< HEAD
  import usMap from '@/assets/json/custom-map.json'
	import { mapChart } from "@/assets/js/map.js";
	export default {
		data() {
			return {
				...mapChart,
=======
  
  import usMap from '@/assets/json/custom-map.json';
  import map1 from './map1';
  import teamData from "@/assets/json/team.json";
	export default {
		data() {
			return {
        teamIndex:0,
        teamData:teamData,
        showTeam:false,
        showSelectTeam:false,
>>>>>>> 9fc78a91cdce5c5562e3987a6dfa51d5841b0341
        clickHandler (p, e) {
          // console.log(e.name)
          if(this.team[e.name]!=null){
            this.teamName=e.name
            this.showSelectTeam=true
          }
        },
        team:{
          'California':['Golden State Warriors','Los Angeles Clippers','Los Angeles Lakers','Sacramento Kings'],
          'Georgia':['Atlanta Hawks'],
          'Massachusetts':['Boston Celtics'],
          'New York':['Brooklyn Nets','New York Knicks'],
          'North Carolina':['Charlotte Hornets'],
          'Illinois':['Chicago Bulls'],
          'Ohio':['Cleveland Cavaliers'],
          'Texas':['Dallas Mavericks','Houston Rockets','San Antonio Spurs'],
          'Colorado':['Denver Nuggets'],
          'Michigan':['Detroit Pistons'],
          'Indiana':['Indiana Pacers'],
          'Tennessee':['Memphis Grizzlies'],
          'Florida':['Miami Heat','Orlando Magic'],
          'Wisconsin':['Milwaukee Bucks'],
          'Minnesota':['Minnesota Timberwolves'],
          'Louisiana':['New Orleans Pelicans'],
          'Oklahoma':['Oklahoma City Thunder'],
          'Pennsylvania':['Philadelphia 76ers'],
          'Arizona':['Phoenix Suns'],
          'Oregon':['Portland Trail Blazers'],
          'Utah':['Utah Jazz'],
          'Washington':['Washington Wizards']
        },
        teamName:'',
        chartData: {
          columns: ['位置', '球隊'],
          rows: [

          ]
        },
				radarLegend:{
					show:false
				},
        chartSettings: {
          mapOrigin: usMap,
          itemStyle: {
            areaColor: '#fafafa'
          },
          label: {
            show: false
          }
        }
      };
		},
		components: {
    },
    mounted() {
      
    },
    methods:{
<<<<<<< HEAD

=======
      parentClose(state){
          this.showTeam=state // hello, parent
      },
      close(){
          this.showSelectTeam=false
      },
       setTeam(index){
                this.teamIndex=index
                this.showSelectTeam=false
                this.showTeam=true
            },
>>>>>>> 9fc78a91cdce5c5562e3987a6dfa51d5841b0341
    }
  };


</script>

<style>
<<<<<<< HEAD
=======
  .team{
        
        margin-bottom: 20px;
        height: 30%;
        width:100%;
    }
  .showTeam{
    width: 100%;
    height: 100%;
    display: flex;
    flex-wrap: wrap;
  }
  #selectTeam{
    position: absolute;
    width: 100%;
    height: calc(100vh - 76px);
    padding: 5%;
    top:0;
    left:0;
    z-index:10;
  }
  #testttttt{
    width: 100%;
    position: absolute;
    top:0;
    /* padding: 5%; */
    /* display: none; */
  }
>>>>>>> 9fc78a91cdce5c5562e3987a6dfa51d5841b0341
  .page-height {
    height: calc(100vh - 80px);
  }
</style>
