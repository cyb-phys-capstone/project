google.charts.load('current', {'packages':['corechart', 'line']});
google.charts.setOnLoadCallback(function(){drawGraphDefault()});

var asset_data;

function updateTimestamps(){
  var select = document.getElementById("time_select");
  var current = new Date($('#datetimepicker12').datetimepicker("date")._d);

  // clear the dropdown
  $('#time_select').find('option').remove().end()

  // add the times
  for (var i = 0; i < asset_data.length; i++){
    var timestamp = asset_data[i].fields.timestamp;
    var theDate = new Date(timestamp);

    // only get the times for today's date
    if (theDate.getMonth() == current.getMonth() && theDate.getDate() == current.getDate() && theDate.getFullYear() == current.getFullYear()){
      // format to 00:00
      var str = (theDate.getHours() < 10 ? '0' : '') + theDate.getHours() + ":" + (theDate.getMinutes() < 10 ? '0' : '') + theDate.getMinutes();

      // add to the dropdown
      var option = document.createElement("option");
      option.value = timestamp;
      option.text = str;
      select.add(option);
    }
  }
}

// Sets up the data object from Django
function setup(data) {
  asset_data = data;

  updateTimestamps();
}

function selectTime () {
    var timeChosen = {timestamp : $('#time_select').val()};
    loadForm (timeChosen);
}

$('#datetimepicker12').datetimepicker({
    inline: true,
    sideBySide: true
}).on('dp.change', function(e) {
    updateTimestamps();
    selectTime();
    getGraphData();
});

function loadForm (timestamp) {
    $.get('/battery_view', timestamp, function(response){
        $("#real_time_data").replaceWith(response);

        var list = document.getElementsByClassName("battery-attr");
        for(i = 0; i < list.length; i++) {
            list[i].setAttribute("disabled", "true");
        }
    });
}

function getTimeStamp () {
    return $('#time_select').val();
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

    for (i = 0; i < asset_data.length; i++) {

        var tempTime = new Date(asset_data[i].fields["timestamp"]);
        if( currentTime.getDate() === tempTime.getDate() &&
            currentTime.getMonth() === tempTime.getMonth() &&
            currentTime.getFullYear() === tempTime.getFullYear()
        ){

            var dataSet = [];
            dataSet.push(tempTime);
            dataSet.push(asset_data[i].fields[attribute]);
            if(currentTime.getTime() === tempTime.getTime()){
                row = i;
            }
            graphData.push(dataSet);
        }

    }

    drawGraph(attribute, graphData, row);
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

    google.visualization.events.addListener(chart, 'select', function(){
        var selection = chart.getSelection()[0];
        if(chart.getSelection().length > 0) {
            var time =  data.getValue(selection.row, 0);
            loadForm({timestamp: time.toJSON()});

            var timeList = document.getElementById("time_select").children;
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

window.onload = loadForm({timestamp: 0});
