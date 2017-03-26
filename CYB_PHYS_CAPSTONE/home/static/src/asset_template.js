
/* How to calendar is created */
$('#datetimepicker12').datetimepicker({
    inline: true,
    sideBySide: true
}).on('dp.change', function(e) {
    //When calendar date is selected save the date as variable below
    var date = new Date($('#datetimepicker12').datetimepicker("date")._d);

    //Do something with date

});