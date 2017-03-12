
function selectTime () {
    console.log($('#id_timeStamps').val());
    console.log('something');

    var reqObject = {timestamp : $('#id_timeStamps').val()};

    $.get('/NREL_view', reqObject, function(response){
        $("#NREL_data_viewer").replaceWith(response);
    })
}

