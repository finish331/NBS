<template>
  <div class = "hello">
    <div class="selectFilter">
      <el-select v-model="value" placeholder="Select" class="col-md-2" name="selectSeason">
        <el-option 
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>

      <el-select v-model="value" placeholder="Select" class="col-md-2">
        <el-option 
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>

      <el-select v-model="value" placeholder="Select" class="col-md-2">
        <el-option 
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>

      <el-select v-model="value" placeholder="Select" class="col-md-2">
        <el-option 
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
    </div>
  </div>
</template>

<script>
export default {
  components: {},
  data(){
    return{
      options:[
        {value: 'Value1', label:'Option1'},
        {value: 'Value2', label:'Option2'},
        {value: 'Value3', label:'Option3'},
        {value: 'Value4', label:'Option4'},
      ],
      value:''
    };
  },
  methods:{

  }
}
</script>

<style>
  .selectFilter{
    padding-top: 5%;
  }
</style>


<style scoped>
  .selectFilter >>> .el-input__inner{
    height: 60px !important;
    font-size: 20px;
    color: #1570b5;
  }
</style>


