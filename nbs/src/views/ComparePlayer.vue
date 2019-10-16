
<template>
  <div class="compare" style="padding:2%">
    <div
      style="display:flex;justify-content: center;align-items:center;height:10%;font-size:20px;font-weight:800;filter: drop-shadow(3px 3px 3px rgba(0, 0, 0,.5));"
    >
      <div>
        <form style>
          <select
            style="background:#2f2f2f;color:white;padding:0 5px"
            name="selectMVPYear"
            id="selectMVPYear"
            @change="changeYear()"
          >
            <option
              v-for="(i,index) in year"
              :key="index"
              :value="i"
            >{{Number(i)-1}}&nbsp;-&nbsp;{{i}}</option>
          </select>
        </form>
      </div>&nbsp;MVP Predict
    </div>
    <swiper
      :options="swiperOption"
      style="height:76%;width:100%"
      :class="{MVPIn: showIn,MVPOut : showOut}"
    >
      <swiper-slide v-for="(i, index) in player" :key="index">
        <mvp :player="playerData[i]" :index="index" v-if="showIn" />
      </swiper-slide>
      <div class="swiper-pagination" slot="pagination"></div>
      <div class="swiper-button-prev swiper-button-blue" slot="button-prev"></div>
      <div class="swiper-button-next swiper-button-blue" slot="button-next"></div>
    </swiper>
    <div style="height:10%;display: flex; align-items: center;justify-content: center">
      <div class="mvp-btn" @click="change()">{{content}}</div>
    </div>
  </div>
</template>

<script>
import mvp from "./mvp";
import mvpData from "@/assets/json/pred_mvp_result.json";
import playerData from "@/assets/json/player.json";
export default {
  components: { mvp },
  data() {
    return {
      showIn: true,
      showOut: false,
      content: "預測排名",
      playerData: playerData,
      mvpData: mvpData,
      nowYear: "2019",
      year: ["2019", "2018", "2017", "2016"],
      swiperOption: {
        effect: "coverflow",
        grabCursor: true,
        centeredSlides: true,
        slidesPerView: "auto",
        initialSlide: 0,
        coverflowEffect: {
          rotate: -30,
          stretch: 0,
          depth: 100,
          modifier: 1,
          slideShadows: false
        },
        pagination: {
          el: ".swiper-pagination"
        },
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev"
        }
      },
      player: []
    };
  },
  methods: {
    changeYear() {
      this.swiperOption.initialSlide = 0;
      this.nowYear = document.getElementById("selectMVPYear").value;
      this.setPlayer();
        this.showOut=true
        setTimeout(this.setInF, 50);
        // this.showIn = false;
        setTimeout(this.setInT, 50);
    },
    change() {
      if (this.content == "預測排名") {
        this.content = "實際排名";
        this.setPlayer();
        this.showOut=true
        setTimeout(this.setInF, 50);
        // this.showIn = false;
        setTimeout(this.setInT, 50);
      } else {
        this.content = "預測排名";
        this.setPlayer();
        this.showOut=true
        setTimeout(this.setInF, 50);
        // this.showIn = false;
        setTimeout(this.setInT, 50);
      }
    },
    setInT() {
      // this.showOut=false;
      this.showIn = true;
    },
    setInF() {
      this.showOut=false;
      this.showIn = false;
    },
    setPlayer() {
      var i;
      var j;
      this.player = [];
      for (i = 0; i < this.mvpData[this.nowYear].length; i++) {
        for (j = 0; j < this.playerData.length; j++) {
          if (this.content == "預測排名") {
            if (
              this.mvpData[this.nowYear][i].pred_name == this.playerData[j].name
            ) {
              this.player.push(j);
            }
          } else {
            if (
              this.mvpData[this.nowYear][i].act_name == this.playerData[j].name
            ) {
              this.player.push(j);
            }
          }
        }
      }
      // console.log(this.player);
    }
  },
  mounted: function() {
    // console.log(this.mvpData)

    this.setPlayer();
  }
};
</script>

<style scoped>
.mvp-btn {
  cursor: pointer;
  width: 30%;
  height: 50%;
  border-radius: 5px;
  background: #3e3e3e;
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  transition: 0.1s all;
}
.mvp-btn:hover {
  background: #727272;
  transition: 0.1s all;
}
.compare {
  height: calc(100vh - 76px);
  padding: 2% 0;
}
.swiper-inner {
  width: 100%;
  height: 100%;
  /* padding-top: 50px;
    padding-bottom: 50px; */
}
.swiper-slide {
  /* background: black; */
  background: #3e3e3e;
  padding: 10px;
  border-radius: 5px;
  filter: drop-shadow(5px 5px 5px rgba(0, 0, 0, 0.5));
  width: 30%;
  height: calc(100% - 20px);
}
.swiper-button-blue {
  height: 23px !important;
  margin-top: -12px !important;
}
@media (max-width: 960px) {
  .swiper-slide {
    width: 60%;
    height: 100%;
  }
}
@media (max-width: 620px) {
  .swiper-slide {
    width: 100%;
    height: 100%;
  }
}
@keyframes MVPIn {
  from {
    transform: scale(0.5);
    opacity: 0;
  }
  to {
    transform: scale(1);
    opacity: 1;
  }
}
.MVPIn {
  /* opacity: 0.5; */
  /* opacity: 0; */
  animation: MVPIn .5s 1 forwards;
}
@keyframes MVPOut {
  from {
    transform: scale(1);
    opacity: 1;
  }
  to {
    transform: scale(0.5);
    opacity: 0;
  }
}
.MVPOut {
  /* opacity: 0.5; */
  animation: MVPOut .5s 1 forwards;
}
</style>
