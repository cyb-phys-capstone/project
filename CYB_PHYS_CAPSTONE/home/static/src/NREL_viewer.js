google.charts.load('current', {'packages':['corechart', 'line']});
google.charts.setOnLoadCallback(function(){drawGraphDefault()});

function selectTime () {

    var timeChosen = {timestamp : $('#id_timeStamps').val()};

    loadFormNREL (timeChosen);
}

function loadFormNREL (timestamp) {
    $.get('/NREL_view', timestamp, function(response){
        $("#NREL_data_viewer").replaceWith(response);

        var list = document.getElementsByClassName("nrel-attr");
        for(i=0; i < list.length; i++) {
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

function getGraphData () {

    var selection = document.getElementById("data_select").children;
    var attribute;

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
            graphData.push(dataSet);
        }

    }

    drawGraph(attribute, graphData);
}

function drawGraphDefault () {
    var graphData = [];
    var attribute = "ghi";
    var currentTime = new Date(data_NREL[0].fields["timestamp"]);
    for (i = 0; i < data_NREL.length; i++) {
        var tempTime = new Date(data_NREL[i].fields["timestamp"]);
        if( currentTime.getDate() === tempTime.getDate() &&
            currentTime.getMonth() === tempTime.getMonth() &&
            currentTime.getFullYear() === tempTime.getFullYear()
        ){

            var dataSet = [];
            dataSet.push(tempTime);
            dataSet.push(data_NREL[i].fields[attribute]);
            graphData.push(dataSet);
        }
    }
    console.log(graphData);

    drawGraph(attribute, graphData);
}

function drawGraph(attribute, graphData) {
    var data = new google.visualization.DataTable();
    data.addColumn('datetime', 'X');
    data.addColumn('number', attribute);
    data.addRows(graphData);

    var options = {
        legend: 'none'
    }

    var chart = new google.visualization.LineChart(document.getElementById("google_graph"));
    chart.draw(data, options);
}


window.onload = loadFormNREL({timestamp: 0});
