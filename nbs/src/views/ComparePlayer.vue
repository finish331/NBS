
<template>
      <div class="compare" style="padding:2%"> 
        <div style="display:flex;justify-content: center;align-items:center;height:10%;font-size:20px;font-weight:800;filter: drop-shadow(3px 3px 3px rgba(0, 0, 0,.5));">
          2018-2019 MVP Predict
        </div>
        <swiper :options="swiperOption" style="height:80%;width:100%">
          <swiper-slide v-for="(i, index) in player" :key="index"><mvp :player="playerData[i]" :index="index"/></swiper-slide>
          <div class="swiper-pagination " slot="pagination"></div>
          <div class="swiper-button-prev swiper-button-blue" slot="button-prev" ></div>
          <div class="swiper-button-next swiper-button-blue" slot="button-next"></div>
        </swiper>
      </div>
</template>

<script>
  import mvp from './mvp'
  import mvpData from "@/assets/json/mvp.json";
  import playerData from "@/assets/json/player.json";
  export default {
    components: {mvp},
    data() {
      return {
        playerData:playerData,
        mvpData:mvpData,
        swiperOption: {
          effect: 'coverflow',
          grabCursor: true,
          centeredSlides: true,
          slidesPerView: 'auto',
          coverflowEffect: {
            rotate: -30,
            stretch: 0,
            depth: 100,
            modifier: 1,
            slideShadows : false
          },
          pagination: {
            el: '.swiper-pagination'
          },
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
          }
        },
        player:[]
      }
    },
    mounted: function(){
      var i
      var j
      for(i=0;i<this.mvpData.length;i++){
        for(j=0;j<this.playerData.length;j++){
          if(this.mvpData[i].name==this.playerData[j].name){
            this.player.push(j)
          }
        }
      }
    }
  }
</script>

<style scoped>
    .compare{
      height: calc(100vh - 76px);
      padding:2% 0;
    }
  .swiper-inner {
    width: 100%;
    height: 100%;
    /* padding-top: 50px;
    padding-bottom: 50px; */
  }
  .swiper-slide {
    /* background: black; */
    background:#3e3e3e;
    padding:10px;
    border-radius: 5px;
    filter: drop-shadow(5px 5px 5px rgba(0, 0, 0,.5));
    width: 30%;
    height: 100%;
  }
  .swiper-button-blue{
  height: 23px!important;
  margin-top: -12px!important;
  }
  @media (max-width:960px) {
    .swiper-slide {
      width: 60%;
      height: 100%;
    }
  }
  @media (max-width:620px) {
    .swiper-slide {
      width: 100%;
      height: 100%;
    }
  }
</style>
