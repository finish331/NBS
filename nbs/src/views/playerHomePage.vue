<script src="https://code.jquery.com/jquery-3.4.1.js"></script>
<template>
    <div>
        <div style="width: 100%;z-index:9;position: absolute;background:#ffffff" v-if="showPlayer">
        <Player :player="playerData[playerIndex]" @close="parentClose"/>
    </div>
    <div class="playerHomePage px-5" >
        <div id="searchPlayer" class="col-sm-12 col-md-4 " style="width: 100%;height: 100%;padding: 2%;">
            <!-- 搜尋欄 -->
           <div class="search-player">
                    <!-- 搜尋 -->
                   <div style="width: 100%;height: 10%;">
                       <input v-model="playerName" placeholder="search" id="playerName" autocomplete="off">
                   </div>
                    <!-- 搜尋結果 -->
                   <div style="width: 100%;height: 90%;overflow: auto; box-shadow: 2px 2px 2px rgba(0, 0, 0, .2);">
                       <table style="width: 100%;max-height: 100%;background-color: #f1f1f1;">
                            <thead >
                                <tr>
                                    <th style="text-align: center;color:#fff">Player Name</th>
                                    <th style="text-align: center;color:#fff">Team</th>
                                </tr>
                            </thead>
                            <tbody v-for="(i, index) in playerData" :key="index">
                                <tr v-if="playerName.length<2">
                                    <td style="text-align: center;">{{i.name}}</td>
                                    <td style="text-align: center;">{{i.team}}</td>
                                </tr>
                                <tr v-else-if="playerName.length>=2&&i.name.match(RegExp(playerName))">
                                    <td style="text-align: center;">{{i.name}}</td>
                                    <td style="text-align: center;">{{i.team}}</td>
                                </tr>
                            </tbody>
                        </table>
                   </div>
            </div>
        </div>
        <div id="showPlayer" class="col-md-8" style="width: 100%;height: 100%;padding: 2%;">
            <div class="show-player">
                <div class="col-sm-4 col-md-3 player" v-for="(i, index) in playerData" :key="index">
                    <div style="height:80%;">
                        <img :src=i.pic_url alt="" style="height:100%">
                    </div>
                    <div @click="setPlayer(index)" style="cursor: pointer;">
                        {{i.name}}
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
    import Player from './Player'
	export default {
		components: {Player},
		data() {
            return {
                playerIndex:0,
                showPlayer:false,
                playerData:playerData,
                playerName:"",
                player:[
                    {name:"abbb",team:"TES"},
                    {name:"abbb",team:"TES"},
                    {name:"abbb",team:"TES"},
                    {name:"abbb",team:"TES"},
                    {name:"abbb",team:"TES"},
                    {name:"abbb",team:"TES"},
                    {name:"abbb",team:"TES"},
                    {name:"abbb",team:"TES"},
                    {name:"abbb",team:"TES"},
                    {name:"abbb",team:"TES"},
                    {name:"abbb",team:"TES"},
                    {name:"abbs",team:"TES"},
                    {name:"abbb",team:"TES"},
                    {name:"abbb",team:"TES"},
                    {name:"abbb",team:"TES"},
                    {name:"abbb",team:"TES"},
                    {name:"abbb",team:"TES"},
                    {name:"abbb",team:"TES"}
                ]
            }
        },
        mounted: function(){
                    //    this.test()
            if(window.innerWidth <=960){
                document.getElementById('showPlayer').style.display='none';
            }
        },
        methods:{
            // test(){
            //     var fs=require("fs");
            //     var temp
            //     for(var i=0;i<playerData.length;i++){
            //         if(playerData[i].pic_url!="https://stats.nba.com/media/img/league/nba-headshot-fallback.png"){     
            //             if(playerData[i].pic_url.search('latest')==-1){
            //                 console.log(playerData[i].name)
            //                 temp=playerData[i].pic_url.split("/",20)
            //                 this.playerData[i].pic_url="https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/"+temp[9]+"/"+temp[10]
            //             }                
            //         }           
            //     }
            //       var myJSON = JSON.stringify(this.playerData);
            //         fs.writeFile("./player.json", myJSON, "UTF8", function(err) {
            //             if (err) throw err;
            //             console.log("檔案寫入操作完成!");
            //         })
            //         console.log("檔案寫入操作中 ... ");
            // },
            setPlayer(index){
                this.playerIndex=index
                this.showPlayer=true
                // console.log(this.playerIndex)
            },
            parentClose(state){
                this.showPlayer=state // hello, parent
            }
        }
    }
</script>
<style >
    .player{
        height: 30%;
        width:100%;
    }
    .playerHomePage{
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
</style>
