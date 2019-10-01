<template>
	<div class="map1">
        <div class="team-content">
            <div class="content-head" style="position: relative;display:flex; align-items: center;">
                <button @click="close" style="position: absolute;z-index:9999;top:5px;right:5px" ><v-icon style="font-size:30px">cancel</v-icon></button>
                <div style="background: url('https://stats.nba.com/media/img/teams/logos/HOU_logo.svg');background-size: cover; 
                    background-position: center center ; height:100%;width:100%;opacity: .1;position: absolute;"     >
                </div>
                <img src="https://stats.nba.com/media/img/teams/logos/HOU_logo.svg" alt="" height="100%;">
                <div style="color:white;font-size:44px;align-items:center;">
                    Houston Rocket
                </div>
            </div>
            <div style="display:flex;height:15%" >
                <template v-for="(i, index) in List">
					<div class="col-xs-3 col-sm-3 col-md-2" style="padding:2px" :key="index">
                        <div style="padding:10px;background:#666666;height:100%;color:white">
                            <div style="height:50%;text-align:left">{{i.title}}</div>
                            <div style="height:50%;">{{i.value}}</div>
                        </div>
                    </div>
				</template>
                <div id="selectYear" class="col-xs-12 col-sm-12 col-md-4" style="padding:2px">
                    <div style="background:#666666;height:100%"></div>
                </div>
                
            </div>
                <div id="selectYear1" class="col-xs-12 col-sm-12 col-md-4" style="">
                    <div style="background:#666666;height:80px;width:100%"></div>
                </div>
            <div style="display:flex;height:60% ;padding:0 2%;position: relative;" >
                
                <button @click="left" style="position: absolute;left:1px;top:calc(50% - 30px)" ><v-icon style="font-size:30px">arrow_back_ios</v-icon></button>
                    
                <button @click="right" style="position: absolute;right:1px;top:calc(50% - 30px)"><v-icon style="font-size:30px">arrow_forward_ios</v-icon></button>
                <template v-for="(i, index) in playerData">
                <div class="col-xs-12 col-sm-4 col-md-3" style="padding:10px" :key="index" v-if="index<4">
                    <div class="player-card" >
                        <div style="display:flex;align-items:center;height:40%;justify-content: space-around">
                            <img width="60%"  src="../assets/jamesHarden.png" />
                            <div >
                                <div>
                                    {{playerData[page+index].no}}
                                </div>
                                <div>
                                    {{playerData[page+index].player}}
                                </div>
                            </div>
                        </div>
                        <div style="display:flex;align-items:center;height:20%;justify-content: space-around">
                            <div class="col-md-4" style="padding:2px;color:white;height:100%">
                                <div style="background-color: #666666 ;padding:5px;height:100%">
                                    <div style="height:50%;text-align:left;">POS</div>
                                    <div style="height:50%;">{{playerData[page+index].pos}}</div>
                                </div>
                            </div>
                            <div class="col-md-4" style="padding:2px;color:white;height:100%">
                                <div style="background-color: #666666 ;padding:5px;height:100%">
                                <div style="height:50%;text-align:left;">HT</div>
                                <div style="height:50%;">{{playerData[page+index].ht}}</div>
                                </div>
                            </div>
                            <div class="col-md-4" style="padding:2px;color:white;height:100%">
                                <div style="background-color: #666666 ;padding:5px;height:100%">
                                <div style="height:50%;text-align:left;">WT</div>
                                <div style="height:50%;">{{playerData[page+index].wt}}</div>
                                </div>
                            </div>
                        </div>
                        <div style="display:flex;align-items:center;height:20%;justify-content: space-around">
                            <div class="col-md-6" style="padding:2px;color:white;height:100%">
                                <div style="background-color: #666666 ;padding:5px;height:100%">
                                    <div style="height:50%;text-align:left;">birthDate</div>
                                    <div style="height:50%;">{{playerData[page+index].birthDate}}</div>
                                </div>
                            </div>
                            <div class="col-md-3" style="padding:2px;color:white;height:100%">
                                <div style="background-color: #666666 ;padding:5px;height:100%">
                                <div style="height:50%;text-align:left;">HT</div>
                                <div style="height:50%;">{{playerData[page+index].ht}}</div>
                                </div>
                            </div>
                            <div class="col-md-3" style="padding:2px;color:white;height:100%">
                                <div style="background-color: #666666 ;padding:5px;height:100%">
                                <div style="height:50%;text-align:left;">exp</div>
                                <div style="height:50%;">{{playerData[page+index].exp}}</div>
                                </div>
                            </div>
                        </div>
                        <div style="display:flex;align-items:center;height:20%;justify-content: space-around">
                            <div class="col-md-12" style="padding:2px;color:white;height:100%">
                                <div style="background-color: #666666 ;padding:5px;height:100%">
                                <div style="height:50%;text-align:left;">college</div>
                                <div style="height:50%;">{{playerData[page+index].college}}</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                </template>

            </div>
            <div style="display:flex;height:100%;width:100%;" >
                <ve-histogram width="90%" height="100%" :textStyle="textStyles" :extend="series" :data="TeamData">
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
    import { barChart } from "@/assets/js/test.js";
	export default {
        components: {},
        props: ['userName','state'],
		data() {
			return {
                ...barChart,
                page:0,
                playerData :[
                    {
                        'no':3,
                        'player':'OG Anunoby',
                        'pos':'SF',
                        'ht':'6-8',
                        'wt':232,
                        'birthDate':'July 17, 1997',
                        'exp':1,
                        'college':'Indiana University'
                    },
                    {
                        'no':3,
                        'player':'OG Anunoby',
                        'pos':'SF',
                        'ht':'6-8',
                        'wt':232,
                        'birthDate':'July 17, 1997',
                        'exp':1,
                        'college':'Indiana University'
                    },
                    {
                        'no':3,
                        'player':'OG Anunoby',
                        'pos':'SF',
                        'ht':'6-8',
                        'wt':232,
                        'birthDate':'July 17, 1997',
                        'exp':1,
                        'college':'Indiana University'
                    },
                    {
                        'no':3,
                        'player':'OG Anunoby',
                        'pos':'SF',
                        'ht':'6-8',
                        'wt':232,
                        'birthDate':'July 17, 1997',
                        'exp':1,
                        'college':'Indiana University'
                    },{
                        'no':30,
                        'player':'OG Anunoby',
                        'pos':'SF',
                        'ht':'6-8',
                        'wt':232,
                        'birthDate':'July 17, 1997',
                        'exp':1,
                        'college':'Indiana University'
                    },
                    {
                        'no':33,
                        'player':'OG Anunoby',
                        'pos':'SF',
                        'ht':'6-8',
                        'wt':232,
                        'birthDate':'July 17, 1997',
                        'exp':1,
                        'college':'Indiana University'
                    },
                    {
                        'no':32,
                        'player':'OG Anunoby',
                        'pos':'SF',
                        'ht':'6-8',
                        'wt':232,
                        'birthDate':'July 17, 1997',
                        'exp':1,
                        'college':'Indiana University'
                    },
                    {
                        'no':43,
                        'player':'OG Anunoby',
                        'pos':'SF',
                        'ht':'6-8',
                        'wt':232,
                        'birthDate':'July 17, 1997',
                        'exp':1,
                        'college':'Indiana University'
                    }
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
					{ title: "排名", value: 80 },
					{ title: "戰績", value: 36.1 },
					{ title: "教練", value: 6.6 },
					{ title: "總管", value: 7.5 }
					
				]
			};
        },
        methods: {
            left(){
                if(this.page!=0){
                    this.page-=4;
                    console.log("0");
                }
                else{
                    console.log("1");
                }
            },
            right(){
                
                if(this.page+4!=this.playerData.length){
                    console.log("0");
                    this.page+=4;
                }
                
            },
            close(){
              this.$emit('close' , false);
            }
        }
	};
</script>