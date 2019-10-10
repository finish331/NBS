<template>
	<div class="map1">
        <div class="team-content">
            <div class="content-head" style="position: relative;display:flex; align-items: center;">
                <button @click="close" style="position: absolute;z-index:9999;top:5px;right:5px" ><v-icon style="font-size:30px">cancel</v-icon></button>
                <div id="mapTeamLogo" style=";background-size: cover;
                    background-position: center center ; height:100%;width:100%;opacity: .1;position: absolute;"     >
                </div>
                <img :src=team.pic_url alt="" height="100%;">
                <div style="color:white;font-size:44px;align-items:center;">
                    {{team.name}}
                </div>
            </div>
            <div style="display:flex;height:20%" >
                <template v-for="(i, index) in List">
					<div class="col-xs-3 col-sm-3 col-md-2" style="padding:2px" :key="index">
                        <div style="padding:10px;background:#666666;height:100%;color:white">
                            <div style="height:40%;text-align:left">{{i.title}}</div>
                            <div style="height:60%;">{{i.value}}</div>
                        </div>
                    </div>
				</template>
                <div id="selectYear" class="col-xs-12 col-sm-12 col-md-4" style="padding:2px">
                    <div style="background:#666666;height:100%">123</div>
                </div>

            </div>
                <div id="selectYear1" class="col-xs-12 col-sm-12 col-md-4" style="">
                    <div style="background:#666666;height:80px;width:100%"></div>
                </div>
            <div style="display:flex;height:60% ;padding:0 2%;position: relative;" >

                <button @click="left" style="position: absolute;left:1px;top:calc(50% - 30px)" ><v-icon style="font-size:30px">arrow_back_ios</v-icon></button>

                <button @click="right" style="position: absolute;right:1px;top:calc(50% - 30px)"><v-icon style="font-size:30px">arrow_forward_ios</v-icon></button>
                <template v-for="(i, index) in playerData">
                <div class="col-xs-12 col-sm-4 col-md-3" style="padding:10px" :key="index" v-if="index<page+4&&index>=page">
                    <div class="player-card" >
                        <div style="display:flex;align-items:center;height:30%;justify-content: space-around">
                            <img width="60%"  :src=playerData[index].pic_url />
                            <div >
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
                                    <div style="height:50%;text-align:left;">POS</div>
                                    <div style="height:50%;font-size:16px">{{playerData[index].pos}}</div>
                                </div>
                            </div>
                            <div class="col-md-4" style="padding:2px;color:white;height:100%">
                                <div style="background-color: #666666 ;padding:5px;height:100%">
                                <div style="height:50%;text-align:left;">HT</div>
                                <div style="height:50%;font-size:16px">{{playerData[index].ht}}</div>
                                </div>
                            </div>
                            <div class="col-md-4" style="padding:2px;color:white;height:100%">
                                <div style="background-color: #666666 ;padding:5px;height:100%">
                                <div style="height:50%;text-align:left;">WT</div>
                                <div style="height:50%;font-size:16px">{{playerData[index].wt}}</div>
                                </div>
                            </div>
                        </div>
                        <div style="display:flex;align-items:center;height:30%;justify-content: space-around">
                            <div class="col-md-6" style="padding:2px;color:white;height:100%">
                                <div style="background-color: #666666 ;padding:5px;height:100%">
                                    <div style="height:50%;text-align:left;">BirthDate</div>
                                    <div style="height:50%;font-size:16px">{{playerData[index].birthDate}}</div>
                                </div>
                            </div>
                            <div class="col-md-3" style="padding:2px;color:white;height:100%">
                                <div style="background-color: #666666 ;padding:5px;height:100%">
                                <div style="height:50%;text-align:left;">HT</div>
                                <div style="height:50%;font-size:16px">{{playerData[index].ht}}</div>
                                </div>
                            </div>
                            <div class="col-md-3" style="padding:2px;color:white;height:100%">
                                <div style="background-color: #666666 ;padding:5px;height:100%">
                                <div style="height:50%;text-align:left;">Exp</div>
                                <div style="height:50%;font-size:16px">{{playerData[index].exp}}</div>
                                </div>
                            </div>
                        </div>
                        <div style="display:flex;align-items:center;height:20%;justify-content: space-around">
                            <div class="col-md-12" style="padding:2px;color:white;height:100%">
                                <div style="background-color: #666666 ;padding:5px;height:100%">
                                <div style="height:50%;text-align:left;">College</div>
                                <div style="height:50%;font-size:16px">{{playerData[index].college}}</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                </template>

            </div>
            <div style="display:flex;height:100%;width:100%;" >
                <ve-histogram width="100%" height="100%" :textStyle="textStyles" :extend="series" :data="TeamData">
                 </ve-histogram>
            </div>
        </div>

    </div>
</template>
<style >
    .player-card{
        padding: 5px;
        height: 100%;
        background-color: #f0f0f0;
        box-shadow: 2px 2px 10px rgb(0, 0, 0,.3);
    }
    .map1{
        width: 100%;
        height: calc(100vh - 76px);
        padding: 5%;

    }
    .team-content{
        overflow: auto;
         width: 100%;
        height:100%;
        background-color: rgb(253, 253, 253);
        /* border-radius:2%;  */
        box-shadow:10px 10px 20px rgba(0, 0, 0, .1);

    }
    .content-head{

        height: 25%;
        background-color: #666666 ;

    }
    #selectYear1{
        display:none;
        padding:2px;

    }
    @media (max-width:960px){
        #selectYear{
            display:none;
        }
        #selectYear1{
            display:inherit;
        }
    }
</style>
<script>
    import player from "@/assets/json/player.json";
    import { barChart } from "@/assets/js/test.js";
	export default {
        components: {},
        props: ['team'],
		data() {
			return {
                ...barChart,
                page:0,
                player:player,
                playerData :[

                ],
                 TeamData: {
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
                        'type': 'BLK',
                        'value': 5
                    },
                    {
                        'type': 'BLK',
                        'value': 5
                    },
                    {
                        'type': 'BLK',
                        'value': 5
                    },
                    {
                        'type': 'STL',
                        'value': 1
                    },
                    {
                        'type': 'STL',
                        'value': 1
                    },
                    {
                        'type': 'STL',
                        'value': 1
                    }
                    ]
                },
				List: [
					{ title: "排名", value: this.team['2018-19'].summary['Rank'] },
					{ title: "戰績", value: this.team['2018-19'].summary['Record'] },
					{ title: "教練", value: this.team['2018-19'].summary['Coach'] },
					{ title: "總管", value: this.team['2018-19'].summary['Executive'] }

				]
			};
        },
        methods: {
            left(){
                if(this.page!=0){
                    this.page-=4;
                    // console.log("0");
                }
                else{
                    // console.log("1");
                }
            },
            right(){
                if(this.page+4<this.playerData.length){
                    // console.log("0");
                    this.page+=4;
                }

            },
            close(){
              this.$emit('close' , false);
            }
        },
         mounted() {
            var i
            var j
            var pic_url

            var url="url("+this.team.pic_url+")"
            document.getElementById('mapTeamLogo').style.backgroundImage = url


            for(i=0;i<Object.keys(this.team['2018-19'].rosters['No.']).length;i++){
                for(j=0;j<this.player.length;j++){
                    if(this.team['2018-19'].rosters['Player'][i]==this.player[j].name){
                        pic_url=this.player[j].pic_url
                    }
                }
               this.playerData.push({
                        'pic_url':pic_url,
                        'no':this.team['2018-19'].rosters['No.'][i],
                        'player':this.team['2018-19'].rosters['Player'][i],
                        'pos':this.team['2018-19'].rosters['Pos'][i],
                        'ht':this.team['2018-19'].rosters['Ht'][i],
                        'wt':this.team['2018-19'].rosters['Wt'][i],
                        'birthDate':this.team['2018-19'].rosters['Birth Date'][i],
                        'exp':this.team['2018-19'].rosters['Exp'][i],
                        'college':this.team['2018-19'].rosters['College'][i]
                    })

            }
        }
	};
</script>
