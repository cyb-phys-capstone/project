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

function getTimeStamp () {
    return $('#time_select').val();
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
