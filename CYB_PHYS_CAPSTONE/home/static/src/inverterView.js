function loadForm (timestamp) {
    $.get('/inverter_view', timestamp, function(response){
        $("#real_time_data").replaceWith(response);

        var list = document.getElementsByClassName("asset-attr");
        for(i = 0; i < list.length; i++) {
            list[i].setAttribute("disabled", "true");
        }
    });
}

function getDataId (name) {
    var dataId = "";

    if(name === "Output Voltage"){
        dataId = "output_voltage";
    }else if(name === "Real Power") {
        dataId = "real_power";
    }else if(name === "Reactive Power") {
        dataId =  "reactive_power";
    }else if(name === "Frequency") {
        dataId = "frequency";
    }else if(name === "Input Voltage") {
        dataId = "input_voltage";
    }else if(name === "DC Power") {
        dataId = "dc_power";
    }else if(name === "Battery Charging Voltage") {
        dataId = "battery_charge_volt";
    }else if(name === "Power Factor") {
        dataId = "power_factor";
    }

    return dataId;
}

function drawGraphDefault () {
    var graphData = [];
    var attribute = "output_voltage";
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
