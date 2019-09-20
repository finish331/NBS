<script type="text/javascript" src="http://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script>

var myChart;
    $(function(){
        setEcharts();
    });

    function setEcharts(){
        myChart = echarts.init(document.getElementById('mainBar'));
        myChart.setOption({
            title: {
                text: 'ECharts\n入门示例',//主标题文本
                subtext: 12,//副标题文本
                show: true,//标题是否显示 默认为true
                x: 'left',//标题的位置 默认是left
            },
            tooltip: {
                left:"10px"
            },//鼠标放上面出现悬浮
            legend: {//图标
                data:['销量1'],
            },
            xAxis: {
                data: ["衬衫11111","羊毛衫111","雪纺衫111","裤子111","高跟鞋11","袜子111"],//x轴中的数据
                nameLocation:'middle',
                axisLabel : {
                    clickable:true,//并给图表添加单击事件  根据返回值判断点击的是哪里
                    interval : 0,
                    formatter : function(params){
                        var newParamsName = "";
                        var paramsNameNumber = params.length;
                        var provideNumber = 3;
//                            var rowNumber = Math.ceil(paramsNameNumber / provideNumber);
                        if (paramsNameNumber > provideNumber) {
                            var tempStr = "";

                            tempStr = params.substring(0, provideNumber);
                            newParamsName = tempStr+"..."



                        } else {
                            newParamsName = params;
                        }
                        return newParamsName
                    }

                }
            },
            yAxis: {
                type : 'value',
            },//在使用echarts.js的柱状图的时候一定要配置xAxis,yAxis,series这三个参数，如果是不想设置的话也要初始化可以将其设置为空JSON就可以了，要不然会出项报错，同时要保证在echarts.init之前的对象是有宽高的，要不然也会出现错误
            //name=legend.data的时候才能显示图例(销量)
            series: [{//echarts中必不可少的部分:用于指定图标的类型(饼图,柱状图)之类
                name: '销量1',
                type: 'bar',
                data: [5, 20, 36, 10, 10, 20]
            }]

        });
        myChart.on('click', function (params) {
            if(params.value){
                alert("单击了"+params.name+"柱状图");
            }else{
                alert("单击了"+params.name+"x轴标签");
            }
        });

    }
<script type="text/javascript" src="http://apps.bdimg.com/libs/echarts/2.1.9/source/echarts-all.js"></script>