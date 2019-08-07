<template>
	<div id="app">
		<!-- 球員基本資料區 -->
		<div class="my-1 mx-2 text-white bg-gray">
			<div class="container-fluid">
				<div class="row mb-1 justify-content-start align-items-center" style="position: relative;">
					<div style="background: url('https://stats.nba.com/media/img/teams/logos/HOU_logo.svg'); background-size: cover; background-position: center center ; width: 100%; height: 100%; position: absolute; opacity: .2;"></div>
					<div class="col-12 col-sm-auto">
						<img class="img-fluid" src="../assets/jamesHarden.png" />
					</div>
					<div class="col-12 col-sm-auto">
						<div
							class="row justify-content-center justify-content-sm-start align-items-end mb-2 no-gutters"
							style="flex-wrap:nowrap"
						>
							<div class="col-auto">
								<h1 class="font-italic number">#13</h1>
							</div>
							<div class="col-auto pb-1">
								<div class="ml-2">
									<div class="name">James</div>
									<div class="name">Harden</div>
								</div>
							</div>
						</div>
						<div class="mx-0 d-flex justify-content-center justify-content-sm-start">
							<img class="mr-2 logo" src="../assets/basketball.svg" />
							<span>G</span>
							<div class="mx-2 pb-0 vl"></div>
							<span>Houston Rocket</span>
						</div>
					</div>
				</div>
				<!-- 基本資料區 -->
				<div class="row no-gutters base-data-row">
					<!-- 如果v-for會用到兩種以上不同的方式則要用template -->
					<template v-for="(i, index) in 數值List">
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
			<div class="row no-gutters">
				<div class="col-12 col-md-4 mb-3">
					<ve-radar
						id="radarChartDiv"
						:radar="radars"
						:legend="radarLegend"
						:data="chartData"
						:settings="radarSettings"
						height="300px"
						width="auto"
						class="mr-1 bg-gray"
					></ve-radar>
				</div>
				<div class="col-12 col-md-8 mb-3" v-if="pointsData">
					<ve-line
						id="lineChartDiv"
						height="300px"
						width="auto"
						class="bg-gray"
						:textStyle="textStyles"
						:grid="grid"
						:visual-map="visualMap"
						:judge-width="true"
						:data="pointsData"
						:legend="legendSetting"
						:extend="chartExtend"
						:settings="chartSettings"
					></ve-line>
				</div>
				<div class="d-flex justify-content-center flex-wrap my-5" v-else>
					<b-spinner variant="custom-gray" label="Text Centered"></b-spinner>
				</div>
			</div>
			<div class="row justify-content-center mt-3">
				<div class="col-12">
					<b-table
						responsive
						:striped="true"
						:bordered="true"
						:borderless="true"
						:outlined="true"
						:small="true"
						:hover="true"
						:dark="true"
						:items="items"
						:fields="dataFields"
						class="detail-data"
					></b-table>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import { lineChart } from "@/assets/js/playerConfig.js";
	import playerData from "@/assets/playerData.json";

	export default {
		components: {},
		data() {
			return {
				...lineChart, //展開lineChart
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
				數值List: [
					{ title: "G", value: 80 },
					{ title: "PTS", value: 36.1 },
					{ title: "TRB", value: 6.6 },
					{ title: "AST", value: 7.5 },
					{ title: "FG%", value: 80.3 },
					{ title: "FG3%", value: 45.3 },
					{ title: "FT%", value: 88.6 },
					{ title: "eFG%", value: 54.3 },
					{ title: "PER", value: 30.2 },
					{ title: "WS", value: 21 }
				],
				dataFields: [
					"Season",
					"Age",
					"Tm",
					"Lg",
					"Pos",
					"G",
					"GS",
					"MP",
					"FG",
					"FGA",
					"FG%",
					"3P",
					"3PA",
					"3P%",
					"2P",
					"2PA",
					"2P%",
					{ key: "eFG%", label: "eFG%" },
					"FT",
					"FTA",
					"FT%",
					"ORB",
					"DRB",
					"TRB",
					"AST",
					"STL",
					"BLK",
					"TOV",
					"PF",
					"PTS"
				],
				items: playerData
			};
		}
	};
</script>

<style scoped lang="scss">
	@import "../scss/player.scss";
</style>
