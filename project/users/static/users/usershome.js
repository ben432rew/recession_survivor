$(document).ready(function(){
    $("#change_pass_modal").hide()
    $('#change_pass_btn').on('click', function(e) {
        $( "#main" ).hide();
        $("#change_pass_modal").show();
    }) 
})
