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
        for(i = 0; i < list.length; i++) {
            list[i].setAttribute("disabled", "true");
        }
    });
}

function getDataId (name) {
    var dataId = "";

    if(name === "Ghi"){
        dataId = "ghi";
    }else if(name === "Dni") {
        dataId = "dni";
    }else if(name === "Dhi") {
        dataId =  "dhi";
    }else if(name === "Air Temp") {
        dataId = "air_temp";
    }else if(name === "Rel humid") {
        dataId = "rel_humid";
    }else if(name === "Wind speed") {
        dataId = "wind_speed";
    }else if(name === "Wind dir") {
        dataId = "wind_dir";
    }else if(name === "Station Pressure") {
        dataId = "station_pressure";
    }

    return dataId;
}

function getGraphData () {
    console.log(data_NREL);
    console.log(data_NREL.length);

    var selection = document.getElementById("data_select").children;
    console.log(selection);
    var attribute;

    for(i = 0; i < selection.length; i++) {
        if(selection[i].selected === true ) {
            attribute = getDataId(selection[i].innerHTML);
        }
    }

    var graphData = []
    for (i = 0; i < data_NREL.length; i++) {
        var dataSet = [];
        dataSet.push( new Date(data_NREL[i].fields["timestamp"]));
        dataSet.push(data_NREL[i].fields[attribute]);
        graphData.push(dataSet);
    }
    console.log(graphData);

    drawGraph(attribute, graphData);
}

function drawGraphDefault () {
    var graphData = []
    for (i = 0; i < data_NREL.length; i++) {
        var dataSet = [];
        dataSet.push( new Date(data_NREL[i].fields["timestamp"]));
        dataSet.push(data_NREL[i].fields['ghi']);
        graphData.push(dataSet);
    }
    var attribute = "ghi";

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
