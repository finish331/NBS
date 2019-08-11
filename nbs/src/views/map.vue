<template>
	<div class="container page-height">
		<div class="row mh-100 vh-100 align-items-center" >
      <ve-map class="col" height="600px" :data="chartData" :settings="chartSettings"></ve-map>
    </div>
	</div>
</template>

<script>
  import usMap from '@/assets/json/custom-map.json'
	export default {
		data() {
			return {
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
		components: {},
		mounted() {}
	};
</script>

<style scoped lang="scss">
  .page-height {
    height: calc(100vh - 80px);
  }
</style>
