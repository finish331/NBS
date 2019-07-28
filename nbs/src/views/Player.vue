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
						<div class="row justify-content-start mx-0">
							<img id="logo" class="mr-2" src="../assets/basketball.svg" />
							<span>G</span>
							<div id="vl" class="mx-2 pb-0"></div>
							<span>Houston Rocket</span>
						</div>
					</div>
				</div>
				<!-- 基本資料區 -->
				<div class="row mx-0">
					<div class="col baseDataDiv">
						<p class="title">G</p>
						<p class="mb-1">78</p>
					</div>
					<div class="col baseDataDiv">
						<p class="title">PTS</p>
						<p class="mb-1">36.1</p>
					</div>
					<div class="col baseDataDiv">
						<p class="title">TRB</p>
						<p class="mb-1">6.6</p>
					</div>
					<div class="col baseDataDiv">
						<p class="title">AST</p>
						<p class="mb-1">7.5</p>
					</div>
					<div class="col baseDataDiv">
						<p class="title">FG%</p>
						<p class="mb-1">44.2</p>
					</div>
				</div>
				<div class="row mx-0">
					<div class="col baseDataDiv">
						<p class="title">FG3%</p>
						<p class="mb-1">36.8</p>
					</div>
					<div class="col baseDataDiv">
						<p class="title">FT%</p>
						<p class="mb-1">87.9</p>
					</div>
					<div class="col baseDataDiv">
						<p class="title">eFG%</p>
						<p class="mb-1">54.1</p>
					</div>
					<div class="col baseDataDiv">
						<p class="title">PER</p>
						<p class="mb-1">30.6</p>
					</div>
					<div class="col baseDataDiv">
						<p class="title">WS</p>
						<p class="mb-1">15.2</p>
					</div>
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
	export default {
		components: {},
		data() {
			return {
				chartSettings: {
					area: true,
					scale: [true, true], //基本值是否為0，true為否
					lineStyle: {
						width: 3
					}
				},
				radarSettings: {
					areaStyle: {
						color: {
							type: "radial",
							x: 0.5,
							y: 0.5,
							r: 0.5,
							colorStops: [
								{
									offset: 0,
									color: "blue" // 0% 处的颜色
								},
								{
									offset: 1,
									color: "red" // 100% 处的颜色
								}
							],
							global: false // 缺省为 false
						}
					}
				},
				legendSetting: {
					textStyle: {
						color: "white",
						fontSize: 14
					}
				},
				textStyles: {
					color: "white",
					fontSize: 14
				},
				visualMap: [
					{
						type: "continuous",
						splitNumber: 5,
						min: 0,
						max: 40,
						right: 0,
						top: "50%",
						precision: 1,
						inRange: {
							color: ["#63aabc", "#daf1f9", "#fb9935", "#b90b0b"]
						},
						textStyle: {
							color: "white"
						}
					}
				],
				grid: {
					right: 60
				},
				pointsData: null,
				radars: {
					indicator: [
						{ name: "PTS", max: 40 },
						{ name: "TRB", max: 15 },
						{ name: "AST", max: 13 },
						{ name: "BLK", max: 3 },
						{ name: "STL", max: 3 }
					]
				},
				chartData: null,
				radarLegend: {
					show: false
				}
			};
		},
		mounted() {
			this.fetchDataFromServer();
		},
		methods: {
			fetchDataFromServer() {
				setInterval(() => {
					this.pointsData = {
						columns: ["season", "points"],
						rows: [
							{ season: "2012-13", points: 5.0 },
							{ season: "2013-14", points: 20.7 },
							{ season: "2014-15", points: 21.0 },
							{ season: "2015-16", points: 25.1 },
							{ season: "2016-15", points: 27.0 }
						]
					};
					this.chartData = {
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
					};
				}, 1500);
			}
		}
	};
</script>

<style scoped lang="scss">
	.card-body {
		padding: 0px;
	}

	.name {
		line-height: 0.3rem;
		font-size: 1.2rem;
		letter-spacing: 1px;
		font-weight: bold;
	}

	#number {
		font-size: 3rem;
		line-height: 2.5rem;
	}

	#vl {
		border-left: 2px solid white;
		height: 1rem;
	}

	span {
		line-height: 1rem;
	}

	#logo {
		height: 1rem;
		width: auto;
	}

	.title {
		text-align: start;
		margin-bottom: 0;
	}

	.baseDataDiv {
		height: fit-content;
		line-height: 1.2rem;
		margin-top: 0;
		border: 1.5px white solid;
	}

	#radarChartDiv {
		border-radius: 5px 0 0 5px;
	}

	#lineChartDiv {
		border-radius: 0 5px 5px 0;
	}
</style>
