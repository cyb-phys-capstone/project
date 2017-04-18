function loadForm (timestamp) {
    $.get('/nrel_view', timestamp, function(response){
        $("#real_time_data").replaceWith(response);

        var list = document.getElementsByClassName("asset-attr");
        for(i = 0; i < list.length; i++) {
            list[i].setAttribute("disabled", "true");
        }
    });
}

function getDataId (name) {
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

function drawGraphDefault () {
    var graphData = [];
    var attribute = "ghi";
    var row = 0;

    var currentTime = new Date(asset_data[0].fields["timestamp"]);
    for (i = 0; i < asset_data.length; i++) {
        var tempTime = new Date(asset_data[i].fields["timestamp"]);
        if( currentTime.getDate() === tempTime.getDate() &&
            currentTime.getMonth() === tempTime.getMonth() &&
            currentTime.getFullYear() === tempTime.getFullYear()
        ){

            var dataSet = [];
            dataSet.push(tempTime);
            dataSet.push(asset_data[i].fields[attribute]);
            graphData.push(dataSet);
        }
    }

    drawGraph(attribute, graphData, row);
}

window.onload = loadForm({timestamp: 0});
