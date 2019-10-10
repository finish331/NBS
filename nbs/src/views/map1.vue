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
                    <div style="padding:10px;background:#666666;height:100%;color:white">
                        <div style="height:40%;text-align:left">賽季</div>
                         <form >
                            <select name="selectSeason" id="selectSeason" @change="selectSeason()" style="background:#fff;height:100%;color:black;width:50%">
                                <option value="2018-19" >2018-19</option>
                                <option value="2017-18" >2017-18</option>
                                <option value="2016-17" >2016-17</option>
                                <option value="2015-16" >2015-16</option>
                                <option value="2014-15" >2014-15</option>
                                <option value="2013-14" >2013-14</option>
                                <option value="2012-13" >2012-13</option>
                                <option value="2011-12" >2011-12</option>
                                <option value="2010-11" >2010-11</option>
                                <option value="2009-10" >2009-10</option>
                            </select>
                        </form>
                    </div>
                </div>

            </div>
                <div id="selectYear1" class="col-xs-12 col-sm-12 col-md-4" style="">
                    <div style="padding:10px;background:#666666;height:80px;color:white">
                        <div style="height:40%;text-align:left">賽季</div>
                         <form >
                            <select name="selectSeason" id="selectSeason1" @change="selectSeason1()" style="background:#fff;height:100%;color:black;width:50%">
                                <option value="2018-19" >2018-19</option>
                                <option value="2017-18" >2017-18</option>
                                <option value="2016-17" >2016-17</option>
                                <option value="2015-16" >2015-16</option>
                                <option value="2014-15" >2014-15</option>
                                <option value="2013-14" >2013-14</option>
                                <option value="2012-13" >2012-13</option>
                                <option value="2011-12" >2011-12</option>
                                <option value="2010-11" >2010-11</option>
                                <option value="2009-10" >2009-10</option>
                            </select>
                        </form>
                    </div>
                </div>
            <div style="display:flex;height:60% ;padding:0 2%;position: relative;" >

                <button @click="left" style="z-index:999;position: absolute;left:1px;top:calc(50% - 30px)" ><v-icon style="font-size:30px">arrow_back_ios</v-icon></button>

                <button @click="right" style="z-index:999;position: absolute;right:1px;top:calc(50% - 30px)"><v-icon style="font-size:30px">arrow_forward_ios</v-icon></button>
                <template v-for="(i, index) in playerData">
                <div id="showPlayer1" class="col-xs-12 col-sm-4 col-md-3" style="padding:10px" :key="index" v-if="index<page+4&&index>=page&&windowWidth>=960">
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
                <div id="showPlayer2" class="col-sm-6 col-md-6" style="padding:10px" :key="index" v-if="index<page+2&&index>=page&&windowWidth<960&&windowWidth>=620">
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
                 <div id="showPlayer3" class="col-12 col-sm-12 col-md-12" style="padding:10px" :key="index" v-if="index<page+2&&index>=page&&windowWidth<620">
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
    #showPlayer2{
            display: none
        }
        #showPlayer3{
            display: none
        }
    @media (max-width:960px){
        #selectYear{
            display:none;
        }
        #selectYear1{
            display:inherit;
        }
        #showPlayer1{
            display: none
        }
        #showPlayer2{
            display: block
        }
    }
    @media (max-width:620px){
        #showPlayer2{
            display: none
        }
        #showPlayer3{
            display: block
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
                season:"2018-19",
                ...barChart,
                page:0,
                windowWidth:0,
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
            selectSeason(){
                this.playerData=[]
                this.season=document.getElementById("selectSeason").value
                this.List[0].value=this.team[this.season].summary['Rank']
                this.List[1].value=this.team[this.season].summary['Record']
                this.List[2].value=this.team[this.season].summary['Coach']
                this.List[3].value=this.team[this.season].summary['Executive']
                var i
                var j
                var pic_url

                var url="url("+this.team.pic_url+")"
                document.getElementById('mapTeamLogo').style.backgroundImage = url


                for(i=0;i<Object.keys(this.team[this.season].rosters['No.']).length;i++){
                    for(j=0;j<this.player.length;j++){
                        if(this.team[this.season].rosters['Player'][i]==this.player[j].name){
                            pic_url=this.player[j].pic_url
                        }
                    }
                this.playerData.push({
                            'pic_url':pic_url,
                            'no':this.team[this.season].rosters['No.'][i],
                            'player':this.team[this.season].rosters['Player'][i],
                            'pos':this.team[this.season].rosters['Pos'][i],
                            'ht':this.team[this.season].rosters['Ht'][i],
                            'wt':this.team[this.season].rosters['Wt'][i],
                            'birthDate':this.team[this.season].rosters['Birth Date'][i],
                            'exp':this.team[this.season].rosters['Exp'][i],
                            'college':this.team[this.season].rosters['College'][i]
                        })

                }
            },
             selectSeason1(){
                this.playerData=[]
                this.season=document.getElementById("selectSeason1").value
                this.List[0].value=this.team[this.season].summary['Rank']
                this.List[1].value=this.team[this.season].summary['Record']
                this.List[2].value=this.team[this.season].summary['Coach']
                this.List[3].value=this.team[this.season].summary['Executive']
                var i
                var j
                var pic_url

                var url="url("+this.team.pic_url+")"
                document.getElementById('mapTeamLogo').style.backgroundImage = url


                for(i=0;i<Object.keys(this.team[this.season].rosters['No.']).length;i++){
                    for(j=0;j<this.player.length;j++){
                        if(this.team[this.season].rosters['Player'][i]==this.player[j].name){
                            pic_url=this.player[j].pic_url
                        }
                    }
                this.playerData.push({
                            'pic_url':pic_url,
                            'no':this.team[this.season].rosters['No.'][i],
                            'player':this.team[this.season].rosters['Player'][i],
                            'pos':this.team[this.season].rosters['Pos'][i],
                            'ht':this.team[this.season].rosters['Ht'][i],
                            'wt':this.team[this.season].rosters['Wt'][i],
                            'birthDate':this.team[this.season].rosters['Birth Date'][i],
                            'exp':this.team[this.season].rosters['Exp'][i],
                            'college':this.team[this.season].rosters['College'][i]
                        })

                }
            },
            left(){

                    if(this.windowWidth >=620&&this.windowWidth <960){
                        if(this.page!=0){
                            this.page-=2;
                            // console.log("0");
                        }
                        else{
                                // console.log("1");
                        }
                    }
                    else if(this.windowWidth <620){
                        if(this.page!=0){
                            this.page-=1;
                            // console.log("0");
                        }
                        else{
                                // console.log("1");
                        }
                    }
                    else{
                        if(this.page!=0){
                            this.page-=4;
                            // console.log("0");
                        }
                        else{
                                // console.log("1");
                        }
                    }

            },
            right(){
                
                    if(this.windowWidth >=620&&this.windowWidth <960){
                        if(this.page+2<this.playerData.length){
                    // console.log("0");
                            this.page+=2;
                        }

                    }
                    else if(this.windowWidth <620){
                        if(this.page+1<this.playerData.length){
                    // console.log("0");
                            this.page+=1;
                        }
                    }
                    else{
                        if(this.page+4<this.playerData.length){
                    // console.log("0");
                    this.page+=4;
                }

                    }             
            },
            close(){
              this.$emit('close' , false);
            }
        },
         mounted() {
             
            this.windowWidth =window.innerWidth;
            var i
            var j
            var pic_url

            var url="url("+this.team.pic_url+")"
            document.getElementById('mapTeamLogo').style.backgroundImage = url


            for(i=0;i<Object.keys(this.team[this.season].rosters['No.']).length;i++){
                for(j=0;j<this.player.length;j++){
                    if(this.team[this.season].rosters['Player'][i]==this.player[j].name){
                        pic_url=this.player[j].pic_url
                    }
                }
               this.playerData.push({
                        'pic_url':pic_url,
                        'no':this.team[this.season].rosters['No.'][i],
                        'player':this.team[this.season].rosters['Player'][i],
                        'pos':this.team[this.season].rosters['Pos'][i],
                        'ht':this.team[this.season].rosters['Ht'][i],
                        'wt':this.team[this.season].rosters['Wt'][i],
                        'birthDate':this.team[this.season].rosters['Birth Date'][i],
                        'exp':this.team[this.season].rosters['Exp'][i],
                        'college':this.team[this.season].rosters['College'][i]
                    })

            }
        }
	};
</script>
