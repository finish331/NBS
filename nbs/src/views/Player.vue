<template>
	<div>
		<div class="my-1 bg-dark text-white">
			<div class="container mx-3">
				<div class="row justify-content-start align-items-center">
					<div class="col-auto">
						<img src="../assets/jamesHarden.png" />
					</div>
					<div class="col-auto">
						<div class="row justify-content-start align-items-end pt-2 mb-1">
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
			</div>
		</div>
		<div class="container my-3">
			<div>
				<b-card
					img-src="http://lorempixel.com/250/300/sports"
					blank-color="grey"
					bg-variant="dark"
					text-variant="white"
					img-left
					class="mb-3"
				>
					<ve-line
						height="300px"
						width="auto"
						:textStyle="textStyles"
						:grid="grid"
						:visual-map="visualMap"
						:judge-width="true"
						:data="chartData"
						:legend="legendSetting"
						:settings="chartSettings"
						v-if="chartData"
					></ve-line>

					<div class="d-flex justify-content-center flex-wrap my-5" v-else>
						<b-spinner variant="primary" label="Text Centered"></b-spinner>
					</div>
				</b-card>
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
					scale: [true, true] //基本值是否為0，true為否
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
				chartData: null
			};
		},
		mounted() {
			this.fetchDataFromServer();
		},
		methods: {
			fetchDataFromServer() {
				setInterval(() => {
					this.chartData = {
						columns: ["season", "points"],
						rows: [
							{ season: "2012-13", points: 5.0 },
							{ season: "2013-14", points: 20.7 },
							{ season: "2014-15", points: 21.0 },
							{ season: "2015-16", points: 25.1 },
							{ season: "2016-15", points: 27.0 }
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
</style>
