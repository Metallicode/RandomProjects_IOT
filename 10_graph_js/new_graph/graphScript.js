var current_data;
var graphWidth; 
var graphMinHeight
var graphHeight;
var graph_start;
var length_after_zoom;
var canvas;
var ctx;
var logging = true;
var new_data_view;

$(function () {


    if (logging === true) log("init script");

    data_to_drow = [];
    graphWidth = $("#myCanvas").attr("width");
    graphHeight = $("#myCanvas").attr("height");
    $("#controles").css("width", graphWidth);
    graph_start = 0;
    graphMinHeight = 0;
    length_after_zoom = 0;
    canvas = document.getElementById("myCanvas");
    ctx = canvas.getContext("2d");

});

function log(message) {
    console.log(message);
}

function resetData() {
    if (logging === true) log("data reset"); 
    $("#zoom").val(1.0);
    $("#x_locator").val(0.0);
    current_data = createRandomData($("#new_data_length").val(), graphMinHeight, $("#new_data_amp").val());
    length_after_zoom = current_data.length;
    data = fit(current_data);
    drow(data);
}

function call_api() {

    newData = [];

    $.getJSON("https://raw.githubusercontent.com/Metallicode/RandomProjects_IOT/master/random_data_halpers/data.json", function (result) {
        $.each(result, function (i, field) {
            newData.push(field * 1);
            current_data = newData;
            length_after_zoom = current_data.length;
            data = fit(current_data);
            drow(data);
        });
    });



}

function locate_x(e) {
    if (logging === true) log("locate_x");
    graph_start = (Math.floor(current_data.length * e.target.value));
    viewChange(graph_start, length_after_zoom + graph_start);
}

function zoom_x(e) {
    if (logging === true) log("zoom_x");
    length_after_zoom = Math.floor(current_data.length * e.target.value);

    viewChange(graph_start, length_after_zoom + graph_start);
}

function viewChange(start, len) {

    new_data_view = [];

    if (len > current_data.length ) {
        len = current_data.length;
        start = current_data.length - length_after_zoom;

    }

    for (i = start; i < len; i++) {
        new_data_view.push(current_data[i]);
    }

    new_data_view = fit(new_data_view);
    drow(new_data_view);
}

function createRandomData(len, min = 0, max = graphHeight) {
    if (logging === true) log("createRandomData");
    dataarr = [];
    for (i = 0; i < len; i++) {
        dataarr.push(Math.random() * (max - min) + min);   
    }
    return dataarr;
}

function linspace(a, b, n) {
    if (typeof n === 'undefined') n = Math.max(Math.round(b - a) + 1, 1)
    if (n < 2) {
        return n === 1 ? [a] : []
    }
    var i, ret = Array(n)
    n--
    for (i = n; i >= 0; i--) {
        ret[i] = (i * b + (n - i) * a) / n
    }
    return ret
}

function scaleValue(value, from, to) {
    var scale = (to[1] - to[0]) / (from[1] - from[0]);
    var capped = Math.min(from[1], Math.max(from[0], value)) - from[0];
    return ~~(capped * scale + to[0]); //~~ is used as Math.floor
}

function normalize_y(dataArr) {

    if (logging === true) log("normalize_y");

    fixedArr = [];

    valueCheckArr = [];

    oldMax = Math.max(...dataArr); //... spread array to args

    oldMin = Math.min(...dataArr);

    console.log("max " + oldMax + " " + "min " + oldMin);

    for (var i = 0; i < dataArr.length; i++) {
        fixedArr.push(scaleValue(dataArr[i], [oldMin, oldMax], [graphMinHeight, graphHeight]) );
    }

    return fixedArr;
}

function calc_points_index(num_of_points) {
    if (logging === true) log("calc_points_index");

    points_index = linspace(0, graphWidth, num_of_points);

    floord_arr = [];

    for (i = 0; i < num_of_points; i++) {

        floord_arr.push(Math.floor(points_index[i]));

    }
    return floord_arr;
}

function fit(data_array) {

    if (logging === true) log("fit");
    data_to_drow = [];
    numOfPoints = data_array.length;
    data_array = normalize_y(data_array);

    if (numOfPoints < canvas.width) {

        graph_x_points = calc_points_index(numOfPoints);

        for (i = 0; i < data_array.length; i++) {
            data_to_drow.push({ x: graph_x_points[i], y: graphHeight - data_array[i] });
        }

    } else if (numOfPoints === canvas.width) {

        //TBD

    } else {

        //TBD

    }

    return data_to_drow;

}

function drow(data) {
    if (logging === true) log("drow");

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.beginPath();
    for (i = 0; i < data.length - 1; i++) {
        ctx.moveTo(data[i].x, data[i].y);
        ctx.lineTo(data[i + 1].x, data[i + 1].y);
        ctx.lineWidth = 1;
        ctx.strokeStyle = '#2fff00';
        ctx.lineCap = 'round';
        ctx.stroke();
    }

}