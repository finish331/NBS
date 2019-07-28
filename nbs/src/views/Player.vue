<template>
	<div>
		<!-- 球員基本資料區 -->
		<div class="my-1 mx-2 bg-dark text-white">
			<div class="container-fluid mx-0 px-0">
				<div class="row pl-4 mb-1 justify-content-start align-items-center">
					<div class="col-auto">
						<img src="../assets/jamesHarden.png" />
					</div>
					<div class="col-auto">
						<div class="row justify-content-start align-items-end pt-2 mb-1" style="flex-wrap:nowrap">
							<h1 class="col-auto font-italic" id="number">#13</h1>
							<div class="col-auto px-0">
								<p class="name">James</p>
								<p class="name">Harden</p>
							</div>
						</div>
						<div class="mx-0 d-flex">
							<img id="logo" class="mr-2" src="../assets/basketball.svg" />
							<span>G</span>
							<div id="vl" class="mx-2 pb-0"></div>
							<span>Houston Rocket</span>
						</div>
					</div>
				</div>
				<!-- 基本資料區 -->
				<div class="row mx-0">
					<template v-for="(i, index) in 素質List">
						<div class="col base-data" :key="index">
							<div class="title">{{ i.title }}</div>
							<div class="value">{{ i.value }}</div>
						</div>
						<div class="w-100" :key="'divider' + index" v-if="(index + 1) % 5 === 0"></div>
					</template> 
				</div>
				<!-- 基本資料區 -->
			</div>
		</div>
		<!-- 球員進階數據 -->
		<div class="container my-3">
			<div class="row">
				<div id="radarChartDiv" class="col bg-dark px-0">
					<ve-radar
						:radar="radars"
						:legend="radarLegend"
						:data="chartData"
						:settings="radarSettings"
						height="300px"
						width="auto"
					></ve-radar>
				</div>
				<div id="lineChartDiv" class="col-8 bg-dark mx-1 px-0" v-if="pointsData">
					<ve-line
						height="300px"
						width="auto"
						:textStyle="textStyles"
						:grid="grid"
						:visual-map="visualMap"
						:judge-width="true"
						:data="pointsData"
						:legend="legendSetting"
						:settings="chartSettings"
					></ve-line>
				</div>
				<div class="d-flex justify-content-center flex-wrap my-5" v-else>
					<b-spinner variant="primary" label="Text Centered"></b-spinner>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import { lineChart } from '@/assets/js/config.js' 
	export default {
		components: {},
		data() {
			return {
				...lineChart,	
				pointsData: {
					columns: ["season", "points"],
					rows: [
						{ season: "2012-13", points: 5.0 },
						{ season: "2013-14", points: 20.7 },
						{ season: "2014-15", points: 21.0 },
						{ season: "2015-16", points: 25.1 },
						{ season: "2016-15", points: 27.0 }
					]
				},
				chartData: {
					columns: ["seasons", "PTS", "TRB", "AST", "BLK", "STL"],
					rows: [
						{
							seasons: "2018-19",
							PTS: 36.1,
							TRB: 6.6,
							AST: 7.5,
							BLK: 0.7,
							STL: 2.0
						}
					]
				},
				素質List: [
					{ title: 'G', value: 80 },
					{ title: 'PTS', value: 30.6 },
					{ title: 'TRB', value: 5.5 },
					{ title: 'AST', value: 6.2 },
					{ title: 'FG%', value: 80.3 },
					{ title: 'FG3%', value: 45.3 },
					{ title: 'FT%', value: 88.6 },
					{ title: 'eFG%', value: 54.3 },
					{ title: 'PER', value: 30.2 },
					{ title: 'WS', value: 21 }
				]
			};
		}
	};
</script>

<style scoped lang="scss">
@import '../css/player.scss'
</style>
