<template>
  <div class="home ">
    <div class="banner">

    </div>
    <div class="content">
        <div class="content-padding">
          <div class="contenr-title">
            <div style="display:flex">N<div class="title-span"><span>ational</span></div><br></div>
            <div style="display:flex">B<div class="title-span"><span>asketball</span></div><br></div>
            <div style="display:flex">S<div class="title-span"><span>cout</span></div></div>
          </div>
          <a href="'/player'"><div class="content-bnt">
            →

          </div></a>
        </div>
    </div>
  </div>
</template>

<style>
  .home{
   position: relative;
   width: 100%;
   height: calc(100vh - 76px);
   background-color: rgb(0, 0, 0);
   display: flex;
   /* justify-content: center; */
  }
  .banner{
    position: absolute;
    width: 100%;
    height: 100%;
    background-image: url('../assets/56456456-1.jpg');
    background-size: cover;
    background-position: top center;
    opacity: .5;
    filter: grayscale(75%);
  }
  .content{
    position: absolute;
    width: 100%;
    height: 100%;
    padding: 4%;
  }
  .content-padding{
    position: relative;
    display: flex;
    width: 100%;
    height: 100%;
  }
  .contenr-title{
    position: absolute;
    text-align: left;
    color: white;
    font-size: 110px;
    font-weight: bold;
    line-height:normal;
    opacity: .75;
    padding: 1% 2%;
    bottom: 0;
    animation: contenr-title-in .5s .25s 1 ease-in backwards;
  }

  @keyframes contenr-title-in {
    from {
      opacity: 0;
      /* transform: translateY(-10px); */
    }
    to {
      opacity: .75;
    }
  }
  .contenr-title span{
    font-size: 90px;
  }
  .title-span{
    animation: title-in .75s .75s 1 ease-in backwards;
  }
  @keyframes title-in {
    from {
      opacity: 0;
      transform: translateX(-15px);
    }
    to {
      opacity: 1;
    }
  }
  .content-bnt{
    position: absolute;
    padding: 0 3%;
    font-size: 40px;
    border: 2px solid rgb(54, 91, 255);
    color: white;
    right:2%;
    bottom: 2%;
    opacity: .75;
    border-radius: 5px;
    transition:all .25s;
  }
  .content-bnt:hover{
    background: white;
    color: black;
    transition:all .25s;
  }
</style>


<script>
export default {
  name: 'home',
  components: {

  }
}
</script>
