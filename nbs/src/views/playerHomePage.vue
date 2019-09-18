<script src="https://code.jquery.com/jquery-3.4.1.js"></script>
<template>
    <div class="playerHomePage px-5">
        <div id="searchPlayer" class="col-sm-12 col-md-4 " style="width: 100%;height: 100%;padding: 2%;">
           <div class="search-player">
                   <div style="width: 100%;height: 10%;">
                       <input v-model="playerName" placeholder="search" id="playerName" autocomplete="off">
                   </div>
                   <div style="width: 100%;height: 90%;overflow: auto;">
                       <table style="width: 100%;max-height: 100%;">
                        <thead>
                            <tr>
                                <th style="color:#fff">Player Name</th>
                                <th style="text-align: center;color:#fff">Team</th>
                            </tr>
                        </thead>
                        <tbody v-for="(i, index) in player" :key="index">
                            <tr v-if="playerName.length<2">
                                <td >{{i.name}}</td>
                                <td style="text-align: center;">{{i.team}}</td>
                            </tr>
                            <tr v-else-if="playerName.length>=2&&i.name.match(RegExp(playerName))">
                                <td >{{i.name}}</td>
                                <td style="text-align: center;">{{i.team}}</td>
                            </tr>
                        </tbody>
                        </table>
                   </div>
            </div>
        </div>
        <div id="showPlayer" class="col-md-8" style="width: 100%;height: 100%;padding: 2%;">
            <div class="show-player">
                <div class="row" style="width: 100%;height: 33%;">
                    <div class="col-md-3">
                       
                    </div>
                    <div class="col-md-3">

                    </div>
                    <div class="col-md-3">
    
                    </div>
                    <div class="col-md-3">

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
	export default {
		components: {},
		data() {
            return {
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
            console.log(window.innerWidth);
            if(window.innerWidth <=960){
                document.getElementById('showPlayer').style.display='none';
            }
        },
        methods:{
           
        }
    }
</script>
<style >
    .playerHomePage{
        display: flex;
        height: calc(100vh - 76px);
        width: 100%;
        background-color: #fafafa;
    }
    .show-player{
        width: 100%;
        height: 100%;
        background-color: #f1f1f1;
        padding: 5%;
        box-shadow: 2px 2px 2px rgba(0, 0, 0, .2)
    }
    .search-player{
        width: 100%;
        height: 100%;
        background-color: #f1f1f1;
        padding: 5%;
        box-shadow: 2px 2px 2px rgba(0, 0, 0, .2)
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
    .search-player  thead{
        
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
