export const lineChart = {
  textStyles: {
    color: "white",
    fontSize: 10
  },
  leftseries: {
    label: { show: true, position: "insideTop" },
    itemStyle:{
        color: '#2690dd',
        barBorderRadius: [3, 0, 0, 3]
    },
    
  },
  rightseries: {
    label: { show: true, position: "insideTop" },
    itemStyle:{
        color: '#f74672',
        barBorderRadius: [0, 3, 3, 0]
    }
  },
  xAxis: {
    // show:false,
    inverse: true,
    axisLabel:{
      fontSize:10
    } 
  },
  radarLegend:{
    show:false
  }
}
