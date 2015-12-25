$(function () {
    var seriesOptions = [],
        seriesCounter = 0,
        names = ['youxi1', 'youxi2', 'youxi3'],
        // create the chart when all data is loaded
        createChart = function () {

            $('#container').highcharts('StockChart', {

                rangeSelector: {
                    selected: 4
                },
                xAxis: {
                    plotLines: [{
                        color: '#0200',
                        dashStyle: 'Dash',
                        width: 1.5,
                        value: 4.5,
                        zIndex: 5
                                }]

                },

                yAxis: {
                    labels: {
                        formatter: function () {
                            return (this.value > 0 ? ' + ' : '') + this.value + '%';
                        }
                    },
                    plotLines: [{
                        value: 0,
                        width: 2,
                        color: 'silver'
                    }]
                },

                plotOptions: {
                    series: {
                        compare: 'percent'
                    }
                },

                tooltip: {
                    pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.change}%)<br/>',
                    valueDecimals: 2
                },

                series: seriesOptions
            });
        };

    $.each(names, function (i, name) {

        $.getJSON('json/' + name.toLowerCase() + '-c.json',function (data) {
            //alert(name)
            seriesOptions[i] = {
                name: name,
                data: data
            };

            // As we're loading the data asynchronously, we don't know what order it will arrive. So
            // we keep a counter and create the chart when all the data is loaded.
            seriesCounter += 1;

            if (seriesCounter === names.length) {
                createChart();
            }
        });
    });
});