export const lineChart = {
  chartSettings: {
    area: true,
    scale: [true, true], //基本值是否為0，true為否
    lineStyle: {
      width: 3
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
            color: "blue" // 0% 处的颜色
          },
          {
            offset: 1,
            color: "red" // 100% 处的颜色
          }
        ],
        global: false // 缺省为 false
      }
    }
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
  radars: {
    indicator: [
      { name: "PTS", max: 40 },
      { name: "TRB", max: 15 },
      { name: "AST", max: 13 },
      { name: "BLK", max: 3 },
      { name: "STL", max: 3 }
    ]
  },
  radarLegend: {
    show: false
  },
}

