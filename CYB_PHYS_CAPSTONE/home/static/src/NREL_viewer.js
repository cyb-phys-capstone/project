
function selectTime () {

    var timeChosen = {timestamp : $('#id_timeStamps').val()};

    loadFormNREL (timeChosen);
}

function loadFormNREL (timestamp) {
    $.get('/NREL_view', timestamp, function(response){
        $("#NREL_data_viewer").replaceWith(response);

        var list = document.getElementsByClassName("nrel-attr");
        for(i=0; i < list.length; i++) {
            list[i].setAttribute("disabled", "true");
        }
    });
}

window.onload = loadFormNREL({timestamp: 0});