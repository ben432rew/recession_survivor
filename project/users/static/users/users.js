$(document).ready(function(){
    $("#signup").hide()
    $("#login").hide()
    $('#signup_button').on('click', function(e) {
        $( ".views" ).hide()
        $("#signup").show()
    })
    $('#login_button').on('click', function(e) {
        $( ".views" ).hide()
        $("#login").show()
    })    
})
