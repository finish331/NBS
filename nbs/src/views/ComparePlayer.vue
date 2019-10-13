<template>  
      <swiper :options="swiperOption">
        <swiper-slide>
            <Player  :player="playerData[0]" @close="parentClose"/>
        </swiper-slide>
        <swiper-slide>
             <Player  :player="playerData[1]" @close="parentClose"/>
        </swiper-slide>
        <swiper-slide> <Player  :player="playerData[2]" @close="parentClose"/></swiper-slide>
        <swiper-slide> <Player  :player="playerData[3]" @close="parentClose"/></swiper-slide>
        <swiper-slide> <Player  :player="playerData[4]" @close="parentClose"/></swiper-slide>
        <swiper-slide> <Player  :player="playerData[5]" @close="parentClose"/></swiper-slide>
        <swiper-slide> <Player  :player="playerData[6]" @close="parentClose"/></swiper-slide>
        <swiper-slide> <Player  :player="playerData[7]" @close="parentClose"/></swiper-slide>
        <swiper-slide> <Player  :player="playerData[8]" @close="parentClose"/></swiper-slide>
        <swiper-slide> <Player  :player="playerData[9]" @close="parentClose"/>0</swiper-slide>
        <div class="swiper-button-prev" slot="button-prev"></div>
        <div class="swiper-button-next" slot="button-next"></div>
      </swiper>
</template>

<script>
import Player from './Player'	
import playerData from "@/assets/json/player.json";
  export default {
      components: {Player},
    data() {
      return {
          playerData:playerData,
        swiperOption: {
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
          }
        }
      }
    }
  }
</script>
