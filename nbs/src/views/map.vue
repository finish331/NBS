<template>
	<div class="container page-height px-5">
		<div class="row mh-100 vh-100 align-items-center" >
      <ve-map class="col"  :events="{ click: clickHandler.bind(this, 1) }" width="80%" height="600px" :data="chartData" :settings="chartSettings"></ve-map>
    </div>
    <div id="testttttt" ><map1 /></div>
	</div>
</template>

<script>
  import usMap from '@/assets/json/custom-map.json'
  import map1 from './map1'
	export default {
		data() {
			return {
        clickHandler (p, e) {
          console.log(e.name)
          // document.getElementById('testttttt').style.display="block"
        },
        chartData: {
          columns: ['位置', '人口'],
          rows: [
            { '位置': '延庆区', '人口': 123 },
            { '位置': '密云区', '人口': 1223 },
            { '位置': '平谷区', '人口': 2123 },
            { '位置': '海淀区', '人口': 4123 }
          ]
        },
        chartSettings: {
          mapOrigin: usMap,
          itemStyle: {
            areaColor: '#fafafa'
          },
          label: {
            show: false
          }
        }
      };
		},
		components: {
      map1
    },
    mounted() {
    },
    methods:{
      test(){
        console.log('2')
      }
    }
  };
  

</script>

<style>
  #testttttt{
    display: none;
  }
  .page-height {
    height: calc(100vh - 80px);
  }
</style>
