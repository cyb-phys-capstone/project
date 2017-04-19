function loadForm (timestamp) {
    $.get('/generator_view', timestamp, function(response){
        $("#real_time_data").replaceWith(response);

        var list = document.getElementsByClassName("generator-attr");
        for(i = 0; i < list.length; i++) {
            list[i].setAttribute("disabled", "true");
        }
    });
}

function getDataId (name) {
    var dataId = "";

    switch (name) {
      case "Voltage":
        dataId = "output_voltage";
        break;
      case "Current":
        dataId = "output_current";
        break;
      case "Real Power(kW)":
        dataId = "output_real_power1";
        break;
      case "Real Power(kVAR)":
        dataId = "output_real_power2";
        break;
      case "Frequency":
        dataId = "frequency";
        break;
      default:
        break;
    }

    return dataId;
}

function drawGraphDefault () {
    var graphData = [];
    var attribute = "voltage";
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
