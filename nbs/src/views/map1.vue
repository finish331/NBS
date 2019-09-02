<template>
	<div class="map1">
        <div class="team-content">
            <div class="content-head" style="position: relative;display:flex; align-items: center;">
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
					<div class="col-md-2" style="padding:2px" :key="index">
                        <div style="padding:10px;background:#666666;height:100%;color:white">
                            <div style="height:50%;text-align:left">{{i.title}}</div>
                            <div style="height:50%;">{{i.value}}</div>
                        </div>
                    </div>
				</template>
                <div class="col-md-4" style="padding:2px">
                    <div style="background:#666666;height:100%"></div>
                </div>
            </div>
        </div>
    </div>
</template>
<style >
    .map1{
        width: 100vw;
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
</style>
<script>
	export default {
		components: {},
		data() {
			return {	
				List: [
					{ title: "排名", value: 80 },
					{ title: "戰績", value: 36.1 },
					{ title: "教練", value: 6.6 },
					{ title: "總管", value: 7.5 }
					
				]
			};
		}
	};
</script>