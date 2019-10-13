export const lineChart = {
  chartSettings: {

    area: true,
    scale: [true, true], //基本值是否為0，true為否
    smooth: true,
    lineStyle: {
      width: 5
    }
  },
  chartExtend: {
    series: {
      smooth: false
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
            color: "red" // 0% 處的顏色
          },
          {
            offset: 1,
            color: "red" // 100% 處顏色
          }
        ],
        global: false // 預設為 false
      }
    }
  },
  legendSetting: {
    show: false,
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
    right: 60,
    top: 50,
    bottom: 30
  },
  radars: {
    indicator: [
      { name: "PTS 得分", max: 5},
      { name: "TRB 籃板", max: 5 },
      { name: "AST 助攻", max: 5 },
      { name: "BLK 火鍋", max: 5 },
      { name: "STL 抄截", max: 5 }
    ],
    center: ['50%', '55%'],
    name: {
      color: "white",
      fontSize: 14
    }
  },
  radarLegend: {
    show: false
  },
  tooltip:{
    show:false
  }
}
