<template>

	<div id="app" class="px-5">
		<!-- 球員基本資料區 -->
		<div class="my-1 mx-2 text-white global-bg-gray">
			<div class="container-fluid">
				<div class="row mb-1 justify-content-start align-items-center" style="position: relative;">
					<button @click="close" style="position: absolute;z-index:9999;top:5px;right:5px" ><v-icon style="font-size:30px">cancel</v-icon></button>
					<div id="playerTeamLogo" style=" background-size: cover; background-position: center center ; width: 100%; height: 100%; position: absolute; opacity: .2;">
					
					</div>
					<div class="col-12 col-sm-auto">
						<img class="img-fluid" :src=player.pic_url />
					</div>
					<div class="col-12 col-sm-auto">
						<div
							class="row justify-content-center justify-content-sm-start align-items-end mb-2 no-gutters"
							style="flex-wrap:nowrap"
						>
							<div class="col-auto">
								<h1 class="font-italic number">#{{player.number}}</h1>
							</div>
							<div class="col-auto pb-1">
								<div class="ml-2">
									<div class="name">{{player.name.split(" ")[0]}}</div>
									<div class="name">{{player.name.split(" ")[1]}}</div>
								</div>
							</div>
						</div>
						<div class="mx-0 d-flex justify-content-center justify-content-sm-start">
							<img class="mr-2 logo" src="../assets/basketball.svg" />
							<span>G</span>
							<div class="mx-2 pb-0 vl"></div>
							<span>{{player.team}}</span>
						</div>
					</div>
				</div>
				<!-- 基本資料區 -->
				<div class="row no-gutters base-data-row">
					<!-- 如果v-for會用到兩種以上不同的方式則要用template -->
					<template v-for="(i, index) in 數值List">
						<div class="col base-data" :key="index">
							<div class="title">{{ i.title }}</div>
							<div class="value">{{ i.value }}</div>
						</div>
						<div class="w-100" :key="'divider' + index" v-if="(index + 1) % 5 === 0"></div>
					</template>
				</div>
				<!-- 基本資料區 -->
			</div>
		</div>
		<!-- 球員進階數據 -->
		<div class="container my-3">
			<div class="row no-gutters">
				<div class="col-12 col-md-4 mb-3">
					<ve-radar
						id="radarChartDiv"
						:radar="radars"
						:legend="radarLegend"
						:data="chartData"
						:settings="radarSettings"
						height="300px"
						width="auto"
						class="mr-1 global-bg-gray"
					></ve-radar>
				</div>
				<div class="col-12 col-md-8 mb-3" v-if="pointsData">
					<ve-line
						id="lineChartDiv"
						height="300px"
						width="auto"
						class="global-bg-gray"
						:textStyle="textStyles"
						:grid="grid"
						:visual-map="visualMap"
						:judge-width="true"
						:data="pointsData"
						:legend="legendSetting"
						:extend="chartExtend"
						:settings="chartSettings"
					></ve-line>
				</div>
				<div class="d-flex justify-content-center flex-wrap my-5" v-else>
					<b-spinner variant="custom-gray" label="Text Centered"></b-spinner>
				</div>
			</div>
			<div class="row justify-content-center mt-3">
				<div class="col-12">
					<b-table
						responsive
						:striped="true"
						:bordered="true"
						:borderless="true"
						:outlined="true"
						:small="true"
						:hover="true"
						:dark="true"
						:items="items"
						:fields="dataFields"
						class="detail-data"
						table-class="global-bg-gray"
					></b-table>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import { lineChart } from "@/assets/js/playerConfig.js";
	import playerData from "@/assets/json/playerData.json";
	import teamData from "@/assets/json/team.json";
	export default {
		components: {},
		props: ['player'],
		data() {
			return {
				teamData:teamData,
				...lineChart, //展開lineChart
				pointsData: {
					columns: ["season", "points"],
					rows: [
						{ season: "2012-13", points: 5.0 },
						{ season: "2013-14", points: 20.7 },
						{ season: "2014-15", points: 21.0 },
						{ season: "2015-16", points: 25.1 },
						{ season: "2016-15", points: 27.0 }
					]
				},
				chartData: {
					columns: ["seasons", "PTS", "TRB", "AST", "BLK", "STL"],
					rows: [
						{
							seasons: "2018-19",
							PTS: '',
							TRB: '',
							AST: '',
							BLK: '',
							STL: ''
						}
					]
				},
				數值List: [
					{ title: "G", value:''},
					{ title: "PTS", value: ''},
					{ title: "TRB", value: '' },
					{ title: "AST", value: '' },
					{ title: "STL", value: ''},
					{ title: "BLK", value: ''},
					{ title: "FG%", value: ''},
					{ title: "3P%", value: ''},
					{ title: "FT%", value: ''},
					{ title: "Season", value: ''}
					
				],
				dataFields: [
					"Season",
					"Age",
					"Tm",
					"Lg",
					"Pos",
					"G",
					"GS",
					"MP",
					"FG",
					"FGA",
					"FG%",
					"3P",
					"3PA",
					"3P%",
					"2P",
					"2PA",
					"2P%",
					{ key: "eFG%", label: "eFG%" },
					"FT",
					"FTA",
					"FT%",
					"ORB",
					"DRB",
					"TRB",
					"AST",
					"STL",
					"BLK",
					"TOV",
					"PF",
					"PTS"
				],
				items: playerData
			};
		},
		mounted: function(){
			var i
			var url
			for(i=0;i<this.teamData.length;i++){
					if(this.player.team==this.teamData[i].name){
						url="url("+this.teamData[i].pic_url+")"
						document.getElementById('playerTeamLogo').style.backgroundImage = url
					}
				}
			if(this.player['data']!=undefined){
				

				this.數值List[0].value=this.player.data.G[Object.keys(this.player.data.G).length-2]
				this.數值List[1].value=this.player.data.PTS[Object.keys(this.player.data.PTS).length-2] 
				this.數值List[2].value=this.player.data.TRB[Object.keys(this.player.data.TRB).length-2] 
				this.數值List[3].value=this.player.data.AST[Object.keys(this.player.data.AST).length-2] 
				this.數值List[4].value=this.player.data.STL[Object.keys(this.player.data.STL).length-2]  
				this.數值List[5].value=this.player.data.BLK[Object.keys(this.player.data.BLK).length-2]  
				this.數值List[6].value=Number(this.player.data['FG%'][Object.keys(this.player.data['FG%']).length-2]).toFixed(2)
				this.數值List[7].value=Number(this.player.data['3P%'][Object.keys(this.player.data['3P%']).length-2]).toFixed(2)
				this.數值List[8].value=Number(this.player.data['FT%'][Object.keys(this.player.data['FT%']).length-2]).toFixed(2)
				this.數值List[9].value=this.player.data['Season'][Object.keys(this.player.data['Season']).length-2]

				this.chartData.rows[0].PTS=this.player.data.PTS[Object.keys(this.player.data.PTS).length-2]
				this.chartData.rows[0].TRB=this.player.data.TRB[Object.keys(this.player.data.TRB).length-2]
				this.chartData.rows[0].AST=this.player.data.AST[Object.keys(this.player.data.AST).length-2]
				this.chartData.rows[0].BLK=this.player.data.BLK[Object.keys(this.player.data.BLK).length-2]
				this.chartData.rows[0].STL=this.player.data.STL[Object.keys(this.player.data.STL).length-2]
			}
			else if(this.player['college_data']!=undefined){
				this.數值List[0].value=this.player.college_data.G[Object.keys(this.player.college_data.G).length-2]
				this.數值List[1].value=this.player.college_data.PTS[Object.keys(this.player.college_data.PTS).length-2] 
				this.數值List[2].value=this.player.college_data.TRB[Object.keys(this.player.college_data.TRB).length-2] 
				this.數值List[3].value=this.player.college_data.AST[Object.keys(this.player.college_data.AST).length-2] 
				this.數值List[4].value=this.player.college_data.STL[Object.keys(this.player.college_data.STL).length-2]  
				this.數值List[5].value=this.player.college_data.BLK[Object.keys(this.player.college_data.BLK).length-2]  
				this.數值List[6].value=Number(this.player.college_data['FG%'][Object.keys(this.player.college_data['FG%']).length-2]).toFixed(2)
				this.數值List[7].value=Number(this.player.college_data['3P%'][Object.keys(this.player.college_data['3P%']).length-2]).toFixed(2)
				this.數值List[8].value=Number(this.player.college_data['FT%'][Object.keys(this.player.college_data['FT%']).length-2]).toFixed(2)
				this.數值List[9].value=this.player.college_data['Season'][Object.keys(this.player.college_data['Season']).length-2]

				this.chartData.rows.PTS=this.player.college_data.PTS[Object.keys(this.player.college_data.PTS).length-2]
				this.chartData.rows.TRB=this.player.college_data.TRB[Object.keys(this.player.college_data.TRB).length-2]
				this.chartData.rows.AST=this.player.college_data.AST[Object.keys(this.player.college_data.AST).length-2]
				this.chartData.rows.BLK=this.player.college_data.BLK[Object.keys(this.player.college_data.BLK).length-2]
				this.chartData.rows.STL=this.player.college_data.STL[Object.keys(this.player.college_data.STL).length-2]
			}
			
		},
		methods:{
			close(){
              this.$emit('close' , false);
            }
		}
	};
</script>

<style scoped lang="scss">
	@import "@/assets/scss/player.scss";
</style>
