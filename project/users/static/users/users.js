$(document).ready(function(){
    $("#signup").hide()
    $("#login").hide()
    $('#signup_button').on('click', function(e) {
        $("#buttons").hide()
        $("#signup").show()
    })
    $('#login_button').on('click', function(e) {
        $("#buttons").hide()
        $("#login").show()
    })    
})
