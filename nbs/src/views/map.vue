<template>
	<div class="container page-height px-5">
		<div class="row mh-100 vh-100 align-items-center" >
      <ve-map class="col" :extend="series" :legend="radarLegend" :events="{ click: clickHandler.bind(this, 1) }" width="100%" height="600px" :data="chartData" :settings="chartSettings"></ve-map>
    </div>
	</div>
</template>

<script>
  import usMap from '@/assets/json/custom-map.json'
	import { mapChart } from "@/assets/js/map.js";
	export default {
		data() {
			return {
				...mapChart,
        clickHandler (p, e) {
          console.log(e.name)
          // document.getElementById('testttttt').style.display="block"
        },
        chartData: {
          columns: ['位置', '球隊'],
          rows: [

          ]
        },
				radarLegend:{
					show:false
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
    },
    mounted() {
    },
    methods:{

    }
  };


</script>

<style>
  .page-height {
    height: calc(100vh - 80px);
  }
</style>
