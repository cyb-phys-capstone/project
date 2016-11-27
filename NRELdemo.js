
function getSolarData(){
    var request = new XMLHttpRequest();
    console.log('test');
    var solarReq='/api/solar/solar_resource/v1.format'
    var key='';
    request.onreadystatechange = function(){
        if((request.readyState == 4) && (request.status ==200)){
           var jsonOBJ = JSON.parse(request.responseText);
                        
            displaySolarData(jsonOBJ.outputs.avg_dni, jsonOBJ.outputs.avg_ghi, jsonOBJ.outputs.avg_lat_tilt);
        }
    }
    request.open('GET','http://developer.nrel.gov/api/solar/solar_resource/v1.json?api_key=DEMO_KEY&lat=33&lon=-111' ,true);
    //request.setRequestHeader()
    request.send(null);        
}

function displaySolarData(dni, ghi, lat){
    //dni
    document.getElementById('dni_ann').innerHTML = dni.annual;
    for(var key in dni.monthly){
        var d='dni_';
        d+=key;
        document.getElementById(d).innerHTML = dni.monthly[key];
    }
    //ghi
    document.getElementById('ghi_ann').innerHTML = ghi.annual;
    for(var key in ghi.monthly){
        var g='ghi_';
        g+=key;
        document.getElementById(g).innerHTML = ghi.monthly[key];
    }
    //tilt
    document.getElementById('lat_ann').innerHTML = lat.annual;
    for(var key in lat.monthly){
        var l='lat_';
        l+=key;
        document.getElementById(l).innerHTML = lat.monthly[key];
    }
    
}
