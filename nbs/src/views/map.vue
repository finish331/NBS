<template>
	<div class="container">
		<ve-map :data="chartData" :settings="chartSettings"></ve-map>
	</div>
</template>

<script>
import usMap from '@/assets/custom.geo.json'
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
          mapOrigin: usMap
        }
      };
		},
		components: {},
		mounted() {}
	};
</script>

<style scoped lang="scss">
</style>
