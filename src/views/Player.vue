<template>
	<div class="container my-3">
		<div>
			<b-card-group deck>
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
						:title="titleSetting"
						:textStyle="textStyles" 
						:grid="grid"
						:visual-map="visualMap"
						:judge-width="true"
						:data="chartData"
						v-if="chartData"
						:legend="legendSetting"
					></ve-line>
					<div v-else>
						<b-spinner variant="primary" label="Text Centered"></b-spinner>
					</div>
				</b-card>
			</b-card-group>
		</div>
	</div>
</template>

<script>
	export default {
		components: {},
		data() { 
			return {
				legendSetting: {
					textStyle:{
						color: "white"
					}
				},
				titleSetting: {
					textStyle: {
						color: "white"
					}
				},
				textStyles: {
					color: "white"
				},
				visualMap: [
					{
						type: "piecewise",
						splitNumber: 5,
						min: 0,
						max: 40,
						right: 0,
						top: "50%"
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
							{ season: "2012-13", points: 19.0 },
							{ season: "2013-14", points: 20.7 },
							{ season: "2014-15", points: 21.0 },
							{ season: "2015-16", points: 25.1 },
							{ season: "2016-15", points: 27.0 }
						]
					};
				}, 2000);
			}
		}
	};
</script>

<style scoped lang="scss">
	.card-body {
		padding: 0px;
	}
</style>
