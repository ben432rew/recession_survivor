$(document).ready(function(){
    $("#signup_modal").hide()
    $("#login_modal").hide()
    $('#signup_button').on('click', function(e) {
        $( ".views" ).hide()
        $("#signup_modal").show()
    })
    $('#login_button').on('click', function(e) {
        $( ".views" ).hide()
        $("#login_modal").show()
    })    
})
