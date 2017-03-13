
function selectTime () {
    console.log($('#id_timeStamps').val());
    console.log('something');

    var reqObject = {timestamp : $('#id_timeStamps').val()};

    $.get('/NREL_view', reqObject, function(response){
        $("#NREL_data_viewer").replaceWith(response);

        var list = document.getElementsByClassName("nrel-attr");
        for(i=0; i < list.length; i++) {
            list[i].setAttribute("disabled", "true");
        }
    });
}

