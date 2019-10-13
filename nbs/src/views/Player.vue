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
							<span>{{player.position}}</span>
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
						:tooltip="tooltip"
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
						
					]
				},
				chartData: {
					columns: ["seasons", "PTS", "TRB", "AST", "BLK", "STL"],
					rows: [
						{
							seasons: "",
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
			
			this.items=[]
			var i
			var j
			var url
			var pointIndexTemp
			var pointTemp
			var temp={season:"",points:""}
			var test=[]
			var teamData={"Season": "","Age": "","Tm": "","Lg": "","Pos": "","G": "","GS": "","MP": "","FG": "","FGA": "","FG%": "","3P": "","3PA": "","3P%": "","2P": "","2PA": "","2P%": "","eFG%": "","FT": "","FTA": "","FT%": "","ORB": "","DRB": "","TRB": "","AST": "","STL": "","BLK": "","TOV": "","PF": "","PTS": ""}
			for(i=0;i<this.teamData.length;i++){
					if(this.player.team==this.teamData[i].name){
						url="url("+this.teamData[i].pic_url+")"
						document.getElementById('playerTeamLogo').style.backgroundImage = url
					}
				}
			if(this.player['data']!=undefined){
				for(i=0;i<Object.keys(this.player.data.PTS).length;i++){
					if(this.player.data['Season'][i]!=null&&this.player.data['Season'][i].search('season')==-1){
						if(i!=0&&this.player.data['Season'][i]!=this.player.data['Season'][i-1]){
							temp.season=this.player.data['Season'][i]
							this.pointsData.rows.push({season:temp.season,points:""})
						}
						else if(i==0){
							temp.season=this.player.data['Season'][i]
							this.pointsData.rows.push({season:temp.season,points:""})
						}
					}
					
					
					teamData.Season=this.player.data['Season'][i]
					teamData.Age=this.player.data['Age'][i]
					teamData.Tm=this.player.data['Tm'][i]
					teamData.Lg=this.player.data['Lg'][i]
					teamData.Pos=this.player.data['Pos'][i]
					teamData.G=this.player.data['G'][i]
					teamData.GS=this.player.data['GS'][i]
					teamData.MP=this.player.data['MP'][i]
					teamData.FG=this.player.data['FG'][i]
					teamData.FGA=this.player.data['FGA'][i]
					teamData['FG%']=Number(this.player.data['FG%'][i]).toFixed(2)
					teamData['3P']=this.player.data['3P'][i]
					teamData['3PA']=this.player.data['3PA'][i]
					teamData['3P%']=Number(this.player.data['3P%'][i]).toFixed(2)
					teamData['2P']=this.player.data['2P'][i]
					teamData['2PA']=this.player.data['2PA'][i]
					teamData['2P%']=Number(this.player.data['2P%'][i]).toFixed(2)
					teamData['eFG%']=Number(this.player.data['eFG%'][i]).toFixed(2)
					teamData.FT=this.player.data['FT'][i]
					teamData.FTA=this.player.data['FTA'][i]
					teamData['FT%']=Number(this.player.data['FT%'][i]).toFixed(2)
					teamData.ORB=this.player.data['ORB'][i]
					teamData.DRB=this.player.data['DRB'][i]
					teamData.TRB=this.player.data['TRB'][i]
					teamData.AST=this.player.data['AST'][i]
					teamData.STL=this.player.data['STL'][i]
					teamData.BLK=this.player.data['BLK'][i]
					teamData.TOV=this.player.data['TOV'][i]
					teamData.PF=this.player.data['PF'][i]
					teamData.PTS=this.player.data['PTS'][i]
					test.push({"Season": teamData.Season,"Age": teamData.Age,"Tm": teamData.Tm,"Lg": teamData.Lg,"Pos": teamData.Pos,"G": teamData.G,"GS": teamData.GS,"MP": teamData.MP,"FG": teamData.FG,"FGA": teamData.FGA,"FG%": teamData['FG%'],"3P": teamData['3P'],"3PA": teamData['3PA'],"3P%": teamData['3P%'],"2P": teamData['2P'],"2PA": teamData['2PA'],"2P%": teamData['2P%'],"eFG%": teamData['eFG%'],"FT": teamData['FT'],"FTA": teamData['FTA'],"FT%": teamData['FT%'],"ORB": teamData.ORB,"DRB": teamData.DRB,"TRB": teamData.TRB,"AST": teamData.AST,"STL": teamData.STL,"BLK": teamData.BLK,"TOV": teamData.TOV,"PF": teamData.PF,"PTS": teamData.PTS})
				}
				for(i=0;i<this.pointsData.rows.length;i++){
					pointTemp=0
					pointIndexTemp=0
					for(j=0;j<Object.keys(this.player.data['Season']).length;j++){
						if(this.pointsData.rows[i].season==this.player.data['Season'][j]){
							pointIndexTemp++
							if((this.player.data.PTS[j].toString()).search("Did Not Play")){
								pointTemp+=Number(this.player.data.PTS[j])
							}
						}
					}
					this.pointsData.rows[i].points=(pointTemp/pointIndexTemp).toFixed(1)
				}
				// console.log(this.pointsData.rows)

				this.items=test

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

				this.chartData.rows[0].seasons=this.player.data['Season'][Object.keys(this.player.data['Season']).length-2]
				this.level(this.player.data.PTS[Object.keys(this.player.data.PTS).length-2],this.player.data.TRB[Object.keys(this.player.data.TRB).length-2],this.player.data.AST[Object.keys(this.player.data.AST).length-2],this.player.data.BLK[Object.keys(this.player.data.BLK).length-2],this.player.data.STL[Object.keys(this.player.data.STL).length-2])
			}
			else if(this.player['college_data']!=undefined){
				for(i=0;i<Object.keys(this.player.college_data.PTS).length;i++){
                    if(this.player.college_data['Season'][i]!=null&&this.player.college_data['Season'][i].search('season')==-1){
                        if(i!=0&&this.player.college_data['Season'][i]!=this.player.college_data['Season'][i-1]){
                            temp.season=this.player.college_data['Season'][i]
                            this.pointsData.rows.push({season:temp.season,points:""})
                        }
                        else if(i==0){
                            temp.season=this.player.college_data['Season'][i]
                            this.pointsData.rows.push({season:temp.season,points:""})
                        }
                    }
                    
                    
                    teamData.Season=this.player.college_data['Season'][i]
                    teamData.Age=this.player.college_data['Age'][i]
                    teamData.Tm=this.player.college_data['Tm'][i]
                    teamData.Lg=this.player.college_data['Lg'][i]
                    teamData.Pos=this.player.college_data['Pos'][i]
                    teamData.G=this.player.college_data['G'][i]
                    teamData.GS=this.player.college_data['GS'][i]
                    teamData.MP=this.player.college_data['MP'][i]
                    teamData.FG=this.player.college_data['FG'][i]
                    teamData.FGA=this.player.college_data['FGA'][i]
                    teamData['FG%']=Number(this.player.college_data['FG%'][i]).toFixed(2)
                    teamData['3P']=this.player.college_data['3P'][i]
                    teamData['3PA']=this.player.college_data['3PA'][i]
                    teamData['3P%']=Number(this.player.college_data['3P%'][i]).toFixed(2)
                    teamData['2P']=this.player.college_data['2P'][i]
                    teamData['2PA']=this.player.college_data['2PA'][i]
                    teamData['2P%']=Number(this.player.college_data['2P%'][i]).toFixed(2)
                    teamData['eFG%']=Number(this.player.college_data['eFG%'][i]).toFixed(2)
                    teamData.FT=this.player.college_data['FT'][i]
                    teamData.FTA=this.player.college_data['FTA'][i]
                    teamData['FT%']=Number(this.player.college_data['FT%'][i]).toFixed(2)
                    teamData.ORB=this.player.college_data['ORB'][i]
                    teamData.DRB=this.player.college_data['DRB'][i]
                    teamData.TRB=this.player.college_data['TRB'][i]
                    teamData.AST=this.player.college_data['AST'][i]
                    teamData.STL=this.player.college_data['STL'][i]
                    teamData.BLK=this.player.college_data['BLK'][i]
                    teamData.TOV=this.player.college_data['TOV'][i]
                    teamData.PF=this.player.college_data['PF'][i]
                    teamData.PTS=this.player.college_data['PTS'][i]
                    test.push({"Season": teamData.Season,"Age": teamData.Age,"Tm": teamData.Tm,"Lg": teamData.Lg,"Pos": teamData.Pos,"G": teamData.G,"GS": teamData.GS,"MP": teamData.MP,"FG": teamData.FG,"FGA": teamData.FGA,"FG%": teamData['FG%'],"3P": teamData['3P'],"3PA": teamData['3PA'],"3P%": teamData['3P%'],"2P": teamData['2P'],"2PA": teamData['2PA'],"2P%": teamData['2P%'],"eFG%": teamData['eFG%'],"FT": teamData['FT'],"FTA": teamData['FTA'],"FT%": teamData['FT%'],"ORB": teamData.ORB,"DRB": teamData.DRB,"TRB": teamData.TRB,"AST": teamData.AST,"STL": teamData.STL,"BLK": teamData.BLK,"TOV": teamData.TOV,"PF": teamData.PF,"PTS": teamData.PTS})
                }
                for(i=0;i<this.pointsData.rows.length;i++){
                    pointTemp=0
                    pointIndexTemp=0
                    for(j=0;j<Object.keys(this.player.college_data['Season']).length;j++){
                        if(this.pointsData.rows[i].season==this.player.college_data['Season'][j]){
                            pointIndexTemp++
                            if(this.player.college_data.PTS[j]!="Did Not Play"){
                                pointTemp+=this.player.college_data.PTS[j]
                            }
                        }
                    }
                    this.pointsData.rows[i].points=(pointTemp/pointIndexTemp).toFixed(1)
                
                }

                this.items=test

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


                this.chartData.rows[0].seasons=this.player.college_data['Season'][Object.keys(this.player.college_data['Season']).length-2]
				this.level(this.player.college_data.PTS[Object.keys(this.player.college_data.PTS).length-2]/this.數值List[0].value,this.player.college_data.TRB[Object.keys(this.player.college_data.TRB).length-2]/this.數值List[0].value,this.player.college_data.AST[Object.keys(this.player.college_data.AST).length-2]/this.數值List[0].value,this.player.college_data.BLK[Object.keys(this.player.college_data.BLK).length-2]/this.數值List[0].value,this.player.college_data.STL[Object.keys(this.player.college_data.STL).length-2]/this.數值List[0].value)
			}
			
		},
		methods:{
			level(PTS,TRB,AST,BLK,STL){
				if(PTS>=0&&PTS<=3.7){
					this.chartData.rows[0].PTS=1
				}
				else if(PTS>3.7&&PTS<=6.9){
					this.chartData.rows[0].PTS=2
				}
				else if(PTS>6.9&&PTS<=11.7){
					this.chartData.rows[0].PTS=3
				}
				else if(PTS>17.7&&PTS<=32){
					this.chartData.rows[0].PTS=4
				}
				else{
					this.chartData.rows[0].PTS=5
				}
				
				if(TRB>=0&&TRB<=1.8){
					this.chartData.rows[0].TRB=1
				}
				else if(TRB>1.8&&TRB<=3){
					this.chartData.rows[0].TRB=2
				}
				else if(TRB>3&&TRB<=4.7){
					this.chartData.rows[0].TRB=3
				}
				else if(TRB>4.7&&TRB<=7.1){
					this.chartData.rows[0].TRB=4
				}
				else{
					this.chartData.rows[0].TRB=5
				}

				if(AST>=0&&AST<=0.6){
					this.chartData.rows[0].AST=1
				}
				else if(AST>0.6&&AST<=1.2){
					this.chartData.rows[0].AST=2
				}
				else if(AST>1.2&&AST<=2.4){
					this.chartData.rows[0].AST=3
				}
				else if(AST>2.4&&AST<=4.1){
					this.chartData.rows[0].AST=4
				}
				else{
					this.chartData.rows[0].AST=5
				}

				if(BLK>=0&&BLK<=0.1){
					this.chartData.rows[0].BLK=1
				}
				else if(BLK>0.1&&BLK<=0.3){
					this.chartData.rows[0].BLK=2
				}
				else if(BLK>0.3&&BLK<=0.5){
					this.chartData.rows[0].BLK=3
				}
				else if(BLK>0.5&&BLK<=0.9){
					this.chartData.rows[0].BLK=4
				}
				else{
					this.chartData.rows[0].BLK=5
				}

				if(STL>=0&&STL<=0.3){
					this.chartData.rows[0].STL=1
				}
				else if(STL>0.3&&STL<=0.6){
					this.chartData.rows[0].STL=2
				}
				else if(STL>0.6&&STL<=0.9){
					this.chartData.rows[0].STL=3
				}
				else if(STL>0.9&&STL<=1.3){
					this.chartData.rows[0].STL=4
				}
				else{
					this.chartData.rows[0].STL=5
				}
			},
			close(){
              this.$emit('close' , false);
            }
		}
	};
</script>

<style scoped lang="scss">
	@import "@/assets/scss/player.scss";
</style>
