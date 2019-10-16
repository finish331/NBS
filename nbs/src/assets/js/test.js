export const barChart = {
    textStyles: {
        color: "#fff",
        fontSize: 10,
        fontWeight: 800

      },
      xAxis:{
        data:['MP','FG','FGA','3P','3PA','2P','2PA','FT','FTA','ORB','DRB','TRB','AST','STL','BLK','TOV','PF','PTS'],
        axisLabel:{
          fontSize:10
        } 
      },
      series: {
        label: { show: true, position: "top" },
        itemStyle:{
            color: '#0fffe9',
            barBorderRadius: [3, 3, 0, 0]
        }
      }
}