<template>
  <div class="champion">
    <div class="col-md-4 champion1" style="height:100%">
        <div class="row " >
            <div class="col-md-12 test">
                <div class="col-md-8 bgimg">
                </div>
                <div  class="col-md-4 test1">
                    87%<br>

                    Golden State Warriors
                    
                </div>
            </div>
        </div>
        <div class="row " >
            <div class="col-md-12 test">
                <div class="col-md-8 bgimg">
                </div>
                <div  class="col-md-4 test1">
                    87%<br>

                    Golden State Warriors
                    
                </div>
            </div>
        </div>
        <div class="row " >
            <div class="col-md-12 test">
                <div class="col-md-8 bgimg"></div>
                <div  class="col-md-4 test1">
                    87%<br>

                    Golden State Warriors
                    
                </div>
            </div>
        </div>
        <div class="row " >
            <div class="col-md-12 test">
                <div class="col-md-8 bgimg">

                </div>
                <div  class="col-md-4 test1">
                    87%<br>

                    Golden State Warriors
                    
                </div>
            </div>
        </div>
        <div class="row " >
            <div class="col-md-12 test">
                <div class="col-md-8 bgimg">

                </div>
                <div  class="col-md-4 test1">
                    87%<br>

                    Golden State Warriors
                    
                </div>
            </div>
        </div>
        <div class="row " >
            <div class="col-md-12 test">
                <div class="col-md-8 bgimg">

                </div>
                <div  class="col-md-4 test1">
                    87%<br>

                    Golden State Warriors
                    
                </div>
            </div>
        </div>
        <div class="row " >
            <div class="col-md-12 test">
                <div class="col-md-8 bgimg">

                </div>
                <div  class="col-md-4 test1">
                    87%<br>

                    Golden State Warriors
                    
                </div>
            </div>
        </div>
    </div>
    <div class="col-md-8" style="display:flex">
        <div class="col-md-6 left-team">
            <div @click="clickTeam('left')" style=" cursor: pointer;width:100% ;height:40%;background: url('https://stats.nba.com/media/img/teams/logos/HOU_logo.svg');background-position: center;background-repeat: no-repeat;"></div>
            <div style="display:flex;width:100%;height:15%" >
                <div class="col player-btn" style="padding:0" v-for="(i, index) in leftTeam.player" :key="index">
                    <div @click="clickPlayer(index)" style="height:100%;background-color: #272727;" v-if=i.state>{{i.name}}</div>
                    <div @click="clickPlayer(index)" style="height:100%;" v-else>{{i.name}}</div>
                </div>
                
            </div>
            <div>
                <div  v-if="leftTeam.isTeam">
                    <div v-for="(i, index) in leftTeam.team" :key="index">{{i}}</div>
                </div>
                <div  v-else>
                    <div v-for="(i, index) in leftTeam.player" :key="index" >
                       <div v-if=i.state>
                           {{i.PTS}}
                           {{i.TRB}}
                           {{i.AST}}
                           {{i.BLK}}
                           {{i.STL}}
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-md-6 right-team">
            31
        </div>
    </div>
  </div>
</template>
<script>
	export default {
		components: {},
		data() {
			return {
				leftTeam: {
                    isTeam:true,
                    team:{aa:1,bc:0,sc:4,sassad:3,se:2},
					player: [
                        {state:false,name:"player1",PTS: 36.1,TRB: 6.6,AST: 7.5,BLK: 0.7,STL: 2.0},
                        {state:false,name:"player2",PTS: 36.1,TRB: 6,AST: 7.5,BLK: 0.7,STL: 2.0},
                        {state:false,name:"player3",PTS: 36.1,TRB: 7.6,AST: 7.5,BLK: 0.7,STL: 2.0},
                        {state:false,name:"player4",PTS: 36.1,TRB: 8.6,AST: 7.5,BLK: 0.7,STL: 2.0},
                        {state:false,name:"player5",PTS: 36.1,TRB: 96,AST: 7.5,BLK: 0.7,STL: 2.0}
                    ],

				}
			};
        },
        methods:{
            clickPlayer(i){
                this.leftTeam.isTeam=false;
               this.leftTeam.player[i].state=true;
                for(var j=0;j<this.leftTeam.player.length;j++){
                    if(i!==j){
                        this.leftTeam.player[j].state=false;
                    }
                }
             
            },
            clickTeam(text){
                this.leftTeam.isTeam=true;
   
                if(text==='left'){
                    for(var j=0;j<this.leftTeam.player.length;j++){
                        
                            this.leftTeam.player[j].state=false;
                        
                    }
               }
                
            }
        }
	};
</script>
<style>
    .champion{
        display: flex;
        height: calc(100vh - 76px);
        width: 100%;
    }
    .champion1{
        overflow: auto;
    }
    .test{
        display: flex;
        margin: 10px 0;
        padding: 0;
        /* height: 100%; */
        background: linear-gradient(to right,#1d1d1d,black);
        box-shadow: 5px 5px 5px rgb(29, 29, 29,.75);
    }
    .bgimg{
        width: 100%;
        height: 100%;
        background: url('../assets/GSW_logo.svg');
        background-position: center;
        background-size: 140%;
        background-repeat: no-repeat;
        opacity: .75;
    }
    .test1{
        /* padding: 5% 0; */
        color: white;
        font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 20px;
        font-weight: bold;
    }
    .left-team{
        color: white;
        background-color: #1d1d1d;
        border: 12px solid white;
    }
    .right-team{
        color: white;
        background-color: #1d1d1d;
        border: 12px solid white;
    }
    .player-btn{
        cursor: pointer;
    }
    .player-btn:hover{
        background-color: #272727;
    }
</style>