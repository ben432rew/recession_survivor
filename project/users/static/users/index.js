$(document).ready(function(){
    $( "#signup_modal" ).hide()

    var hash = location.hash.replace( '#', '' );
    if( hash === "signup" ){
    	$( ".views" ).slideUp()
        $("#signup_modal" ).slideDown()
    }
    if( hash === "login" ){
    	$( ".views" ).slideUp()
        $("#login_modal" ).slideDown()
    }
    console.log(hash)
    $('#signup_button').on('click', function(e) {
        $( ".views" ).slideUp()
        $("#signup_modal").slideDown()
    })
    $('#login_button').on('click', function(e) {
        $( ".views" ).slideUp()
        $("#login_modal").slideDown()
    })    
})
