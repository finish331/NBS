<script src="https://code.jquery.com/jquery-3.4.1.js"></script>
<template>
    <div >
        <div id="showPlayer" style="width: 100%;height:100%;z-index:9;position: absolute;background:#ffffff;" :class={playerIn:showPlayer} v-if="showPlayer">
        <Player  :player="playerData[playerIndex]" @close="parentClose"/>
    </div>
    <div class="playerHomePage px-5" >
        <div id="searchPlayer" class="col-sm-12 col-md-4 " style="width: 100%;height: 100%;padding: 2%;">
            <!-- 搜尋欄 -->
           <div class="search-player">
                    <!-- 搜尋 -->
                   <div style="width: 100%;height: 10%;">
                       <input v-model="playerName" placeholder="search" id="playerName" autocomplete="off" @input="test">
                   </div>
                    <!-- 搜尋結果 -->
                   <div style="width: 100%;height: 90%;overflow: auto; box-shadow: 2px 2px 2px rgba(0, 0, 0, .2);background-color: #f1f1f1;">
                       <table style="width: 100%;max-height: 100%;background-color: #f1f1f1;">
                            <thead >
                                <tr>
                                    <th style="text-align: center;color:#fff">Player Name</th>
                                    <th style="text-align: center;color:#fff">Team</th>
                                </tr>
                            </thead>
                            <tbody v-for="(i, index) in playerData" :key="index" >
                                <tr class="hover" @click="setPlayer(index)"  v-if="playerName.length<2" style="cursor: pointer;">
                                    <td style="text-align: center;">{{i.name}}</td>
                                    <td style="text-align: center;">{{i.team}}</td>
                                </tr>
                                <tr @click="setPlayer(index)"  v-else-if="playerName.length>=2&&i.name.match(RegExp(playerName))" style="cursor: pointer;">
                                    <td style="text-align: center;">{{i.name}}</td>
                                    <td style="text-align: center;">{{i.team}}</td>
                                </tr>
                            </tbody>
                        </table>
                   </div>
            </div>
        </div>
        <div id="showPlayer" class="col-md-8" style="width: 100%;height: 100%;padding: 2%;">
            <div class="show-player" >
                <div  class="col-sm-4 col-md-3 player hover" v-for="(i, index) in playerData" :key="index">
                    <div  @click="setPlayer(index)"  style="cursor: pointer;width:100%;height:0;padding-bottom:80%;position: relative;" >
                        <div v-for="(j, index1) in teamData" :key="index1">
                            <img   :src=j.pic_url alt="" style="width:50%;position: absolute;top:0px;left:0;opacity: 1;" v-if="i.team==j.name">
                        </div>
                        <img  :src=i.pic_url alt="" style="width:100%;position: absolute;bottom:3px;left:0">
                    </div>
                    <div  @click="setPlayer(index)" style="cursor: pointer;">
                        <span style="font-size:24px;text-shadow:0 0 1px #1d1d1d;font-weight:700">#{{i.number}}</span>{{i.name}}
                    </div>
                </div>
            </div>
        </div>
    </div>
    </div>
</template>

<script>
    window.onresize = (function(){
        var windowWidth =window.innerWidth;
        if(windowWidth <960){
            document.getElementById('showPlayer').style.display='none';
        }
        else{
            document.getElementById('showPlayer').style.display='block';
        }
    })
    import playerData from "@/assets/json/player.json";
    import teamData from "@/assets/json/team.json";
    import Player from './Player'
	export default {
		components: {Player},
		data() {
            return {
                playerIndex:0,
                showPlayer:false,
                notShowPlayer:true,
                teamData:teamData,
                playerData:playerData,
                playerName:""
            }
        },
        mounted: function(){
            if(window.innerWidth <=960){
                document.getElementById('showPlayer').style.display='none';
            }
        },
        methods:{
            test(){
                var temp = []
                this.playerDatatemp=temp
                if(this.playerName.length>=2){
                    for(var i=0;i<this.playerData.length;i++){
                        if(this.playerData[i].name.search(playerName.value)!=-1){
                            this.playerDatatemp.push(this.playerData[i])
                        }
                    }
                }
            },
            setPlayer(index){
                this.playerIndex=index
                this.showPlayer=true
                this.notShowPlayer=false
                // console.log(this.playerIndex)
            },
            parentClose(state){
              var temp = document.getElementById('showPlayer')
              temp.classList.add('playerOut')
              setTimeout(this.setPlayerShow, 500)
            },
            setPlayerShow(){
              this.showPlayer=false
            }
        }
    }
</script>
<style >
    .hover:hover{
        color: rgb(0, 132, 255);
    }
    .player{

        margin-bottom: 40px;
        height: 30%;
        width:100%;
    }
    .playerHomePage{
        font-size: 16px;
        font-weight: bolder;
        display: flex;
        height: calc(100vh - 76px);
        width: 100%;
        background-color: rgb(250, 250, 250);
    }
    .show-player{
        border-radius:3px;
        display: flex;
        flex-wrap: wrap;
        overflow: auto;
        width: 100%;
        height: 100%;
        background-color: #f1f1f1;
        padding: 5%;
        box-shadow: 2px 2px 2px rgba(0, 0, 0, .2);
    }
    .search-player{
        width: 100%;
        height: 100%;
        /* background-color: #f1f1f1; */
        /* padding: 5%; */
        /* box-shadow: 2px 2px 2px rgba(0, 0, 0, .2) */
    }
     .search-player input{
         width: 100%;
         font-size: 20px;
         background-color: white;
         border:2px rgb(201, 201, 201) solid;
         border-radius: 5px;
         margin:5% 0 ;
    }
     .search-player table{
         width: 100%;
         max-height: 100%;
         text-align: left;
    }
    .search-player  thead tr th{

        position:sticky;
        top:0;

        background-color: #1d1d1d  ;
    }
    .search-player tbody{
        overflow: auto;
        width: 100%;
        height: auto;
    }
    .search-player  th, td {
        padding: 10px;
    }
    @keyframes playerIn {
      from {
         transform: scale(0.2)
      }
      to {
          transform: scale(1)
      }
    }
    .playerIn {
    font-size: 1.2rem;
    letter-spacing: 1px;
    font-weight: bold;
    line-height: 1.3;
    animation: playerIn .5s 1 backwards;
    }
    @keyframes playerOut {
      from {
         transform: scale(1)
      }
      to {
          transform: scale(0)
      }
    }
    .playerOut {
      font-size: 1.2rem;
      letter-spacing: 1px;
      font-weight: bold;
      line-height: 1.3;
      animation: playerOut .5s 1 backwards;
    }
</style>
