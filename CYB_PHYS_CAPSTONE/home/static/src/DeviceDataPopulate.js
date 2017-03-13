/**
 * Created by Eric on 3/12/2017.
 */
function getDeviceData() {
    var request = new XMLHttpRequest();
    console.log('test');

    request.onreadystatechange = function () {
        if ((request.readyState == 4) && (request.status == 200)) {
            var jsonOBJ = JSON.parse(request.responseText);

            populateDeviceField();
        }
    }
    request.open('GET', 'http://developer.nrel.gov/api/solar/solar_resource/v1.json?api_key=DEMO_KEY&lat=33&lon=-111', true);
    //request.setRequestHeader()
    request.send(null);
}

//Populates
function populateDeviceField(asset, nodeName, manufacturer, model, weight, dimension, resistance, voltageMax, currentMax) {

    document.getElementById('assetNum').innerHTML = asset;
    document.getElementById('nodeName').innerHTML = nodeName;
    document.getElementById('manufacturer').innerHTML = manufacturer;
    document.getElementById('model').innerHTML = model;
    document.getElementById('weight').innerHTML = weight;
    document.getElementById('dimension').innerHTML = dimension;
    document.getElementById('resistance').innerHTML = resistance;
    document.getElementById('voltageMax').innerHTML = voltageMax;
    document.getElementById('currentMax').innerHTML = currentMax;

}

function populateNodeSelcector() {
    console.log("Populating Drop Down");
    var selectNodeList = document.getElementById("nodeList");
    for (var i = 2011; i >= 1900; --i) {
        var option = document.createElement('option');
        option.text = option.value = i;
        selectNodeList.add(option, 0);
    }
}