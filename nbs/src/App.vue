<template>
	<div id="app">
		<b-navbar toggleable="lg" type="dark" style="background:#1d1d1d">
			<b-navbar-brand v-bind:to="'/'">
				<img src="./assets/brand.png" height="50px" />
			</b-navbar-brand>

			<b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

			<b-collapse id="nav-collapse" is-nav>
				<b-navbar-nav>
					<b-nav-item v-bind:to="'/playerHomePage'">Player</b-nav-item>
				</b-navbar-nav>
				<b-navbar-nav>
					<b-nav-item v-bind:to="'/map'">Team</b-nav-item>
				</b-navbar-nav>
				<b-navbar-nav>
					<b-nav-item v-bind:to="'/leader'">Leader</b-nav-item>
				</b-navbar-nav>
				<b-navbar-nav>
					<b-nav-item v-bind:to="'/champion'">Champion</b-nav-item>
				</b-navbar-nav>
				

				<b-navbar-nav>
					<b-nav-item v-bind:to="'/compare'">MVP</b-nav-item>
				</b-navbar-nav>
				<!-- Right aligned nav items -->
				<b-navbar-nav class="ml-auto">
					<!-- <b-nav-form>
						<b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
						<b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
					</b-nav-form> -->

					<!-- <b-nav-item-dropdown text="Lang" right>
						<b-dropdown-item href="#">EN</b-dropdown-item>
						<b-dropdown-item href="#">ES</b-dropdown-item>
						<b-dropdown-item href="#">RU</b-dropdown-item>
						<b-dropdown-item href="#">FA</b-dropdown-item>
					</b-nav-item-dropdown> -->

					<!-- <b-nav-item-dropdown right>
						Using 'button-content' slot
						<template slot="button-content">
							<em>User</em>
						</template>
						<b-dropdown-item href="#">Profile</b-dropdown-item>
						<b-dropdown-item href="#">Sign Out</b-dropdown-item>
					</b-nav-item-dropdown> -->
				</b-navbar-nav>
			</b-collapse>
		</b-navbar>
		<div >
			<router-view />
		</div>
	</div>
</template>

<script>
	export default {
		components: {},
		data() {
			return {
			};
		},
		mounted() {
			// console.log(`仔入好了`);
		}
	};
</script>

<style lang="scss">
	@import "node_modules/bootstrap/scss/bootstrap";
	@import "node_modules/bootstrap-vue/src/index.scss";

	$blue-define: #444b5c !default;
	$define: $blue-define !default;

	#app {
		font-family: "Avenir", Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		text-align: center;
	}
</style>
