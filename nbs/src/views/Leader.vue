<template>
  <div class = "hello">
    <v-app id="inspire">
      <v-container fluid grid-list-xl>
        <v-layout wrap align-center>
          <v-flex xs12 sm6 d-flex>
            <v-select
              :items="items"
              label="Standard"
            ></v-select>
          </v-flex>
        </v-layout>
      </v-container>
    </v-app>
  </div>
</template>

<script>
export default {
  components: {},
  data(){
    return{
      items: ['Foo', 'Bar', 'Fizz', 'Buzz'],
    };
  },
  methods:{

  }
}
</script>


