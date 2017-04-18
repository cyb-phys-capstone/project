<<<<<<< HEAD
//google.charts.load('current', {'packages':['corechart', 'line']});
=======
google.charts.load('current', {'packages':['corechart', 'line']});
>>>>>>> 6ceca417e573e6689a17f92f700e67a516c9652b
google.charts.setOnLoadCallback(function(){drawGraphDefault()});

function selectTime () {

    var timeChosen = {timestamp : $('#id_timeStamps').val()};
<<<<<<< HEAD

    loadForm (timeChosen);
}
/*
=======
    
    loadFormNREL (timeChosen);
}

>>>>>>> 6ceca417e573e6689a17f92f700e67a516c9652b
function filterTime (dateObj) {
    var times = document.getElementById("id_timeStamps").children;
    var newTimes = [];
    for(i = 0; i < times.length; i++) {
        var tempTime = new Date(times[i].value);

        if( tempTime.getMonth() === dateObj.getMonth() &&
            tempTime.getDate() === dateObj.getDate() &&
            tempTime.getFullYear() === dateObj.getFullYear()
        ){
            times[i].style.display = "block";
            newTimes.push(times[i]);
        }else{
            times[i].style.display = "none";
        }
    }

    if( newTimes.length > 0){
        newTimes[0].selected = true;
    }
}
<<<<<<< HEAD
*/

/*
=======

>>>>>>> 6ceca417e573e6689a17f92f700e67a516c9652b
$('#datetimepicker12').datetimepicker({
    inline: true,
    sideBySide: true
}).on('dp.change', function(e) {
    var date = new Date($('#datetimepicker12').datetimepicker("date")._d);
    filterTime(date);
    selectTime();
    getGraphData();
});
<<<<<<< HEAD
*/

function loadForm (timestamp) {
    $.get('/nrel_view', timestamp, function(response){
=======


function loadFormNREL (timestamp) {
    $.get('/NREL_view', timestamp, function(response){
>>>>>>> 6ceca417e573e6689a17f92f700e67a516c9652b
        $("#NREL_data_viewer").replaceWith(response);

        var list = document.getElementsByClassName("nrel-attr");
        for(i = 0; i < list.length; i++) {
            list[i].setAttribute("disabled", "true");
        }
    });
}

function getTimeStamp () {
    return $('#id_timeStamps').val();
}

function getDataId (name) {
    console.log("getting: " + name);

    var dataId = "";

    if(name === "GHI"){
        dataId = "ghi";
    }else if(name === "DNI") {
        dataId = "dni";
    }else if(name === "DHI") {
        dataId =  "dhi";
    }else if(name === "Air Temp.") {
        dataId = "air_temp";
    }else if(name === "Rel. Humid") {
        dataId = "rel_humid";
    }else if(name === "Wind Speed") {
        dataId = "wind_speed";
    }else if(name === "Wind Dir.") {
        dataId = "wind_dir";
    }else if(name === "Station Pressure") {
        dataId = "station_pressure";
    }

    return dataId;
}
<<<<<<< HEAD
/*
=======

>>>>>>> 6ceca417e573e6689a17f92f700e67a516c9652b
function getGraphData () {

    var selection = document.getElementById("data_select").children;
    var attribute;
    var row;
    for(i = 0; i < selection.length; i++) {
        if(selection[i].selected === true ) {
            attribute = getDataId(selection[i].innerHTML);
        }
    }

    var graphData = [];
    var currentTime = new Date(getTimeStamp());

    for (i = 0; i < data_NREL.length; i++) {
        var tempTime = new Date(data_NREL[i].fields["timestamp"]);
        if( currentTime.getDate() === tempTime.getDate() &&
            currentTime.getMonth() === tempTime.getMonth() &&
            currentTime.getFullYear() === tempTime.getFullYear()
        ){

            var dataSet = [];
            dataSet.push(tempTime);
            dataSet.push(data_NREL[i].fields[attribute]);
            if(currentTime.getTime() === tempTime.getTime()){
                row = i;
                console.log(row);
            }
            graphData.push(dataSet);
        }

    }

    drawGraph(attribute, graphData, row);
}
<<<<<<< HEAD
*/
=======

>>>>>>> 6ceca417e573e6689a17f92f700e67a516c9652b
function drawGraphDefault () {
    var graphData = [];
    var attribute = "ghi";
    var row = 0;
<<<<<<< HEAD
    var currentTime = new Date(asset_data[0].fields["timestamp"]);
    for (i = 0; i < asset_data.length; i++) {
        var tempTime = new Date(asset_data[i].fields["timestamp"]);
=======
    var currentTime = new Date(data_NREL[0].fields["timestamp"]);
    for (i = 0; i < data_NREL.length; i++) {
        var tempTime = new Date(data_NREL[i].fields["timestamp"]);
>>>>>>> 6ceca417e573e6689a17f92f700e67a516c9652b
        if( currentTime.getDate() === tempTime.getDate() &&
            currentTime.getMonth() === tempTime.getMonth() &&
            currentTime.getFullYear() === tempTime.getFullYear()
        ){

            var dataSet = [];
            dataSet.push(tempTime);
<<<<<<< HEAD
            dataSet.push(asset_data[i].fields[attribute]);
=======
            dataSet.push(data_NREL[i].fields[attribute]);
>>>>>>> 6ceca417e573e6689a17f92f700e67a516c9652b
            /*
            if(currentTime.getTime() === tempTime.getTime()){
                row = i;
            }
            */
            graphData.push(dataSet);
        }
    }
    console.log(graphData);

    drawGraph(attribute, graphData, row);
}
<<<<<<< HEAD
/*
=======

>>>>>>> 6ceca417e573e6689a17f92f700e67a516c9652b
function drawGraph(attribute, graphData, dot) {
    var data = new google.visualization.DataTable();
    data.addColumn('datetime', 'X');
    data.addColumn('number', attribute);
    data.addRows(graphData);

    var options = {
        legend: 'none'
    }

    var chart = new google.visualization.LineChart(document.getElementById("google_graph"));

    /*google.visualization.events.addListener(chart, 'ready', function(e) {
        chart.setSelection([{row:dot,column:null}]);
    });*/
<<<<<<< HEAD
/*
=======
    
>>>>>>> 6ceca417e573e6689a17f92f700e67a516c9652b
    google.visualization.events.addListener(chart, 'select', function(){
        var selection = chart.getSelection()[0];
        if(chart.getSelection().length > 0) {
            var time =  data.getValue(selection.row, 0);
            loadFormNREL({timestamp: time.toJSON()});

            var timeList = document.getElementById("id_timeStamps").children;
            for(i = 0; i < timeList.length; i++) {
                var tempTime = new Date(timeList[i].value);

                if( time.getTime() === tempTime.getTime()){
                    timeList[i].selected = true;
                }
            }
        }

    });
    chart.draw(data, options);
}
<<<<<<< HEAD
*/
window.onload = loadForm({timestamp: 0});
=======

window.onload = loadFormNREL({timestamp: 0});
>>>>>>> 6ceca417e573e6689a17f92f700e67a516c9652b
