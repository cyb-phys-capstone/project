function loadForm (timestamp) {
    $.get('/battery_view', timestamp, function(response){
        $("#real_time_data").replaceWith(response);

        var list = document.getElementsByClassName("battery-attr");
        for(i = 0; i < list.length; i++) {
            list[i].setAttribute("disabled", "true");
        }
    });
}

function getDataId (name) {
    var dataId = "";

    switch (name) {
      case "SOC":
        dataId = "current_soc";
        break;
      case "Voltage":
        dataId = "current_voltage";
        break;
      case "KW":
        dataId = "current_kw";
        break;
      case "KVAR":
        dataId = "current_kvar";
        break;
      case "State":
        dataId = "state";
        break;
      default:
        break;
    }

    return dataId;
}

function drawGraphDefault () {
    var graphData = [];
    var attribute = "current_soc";
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
