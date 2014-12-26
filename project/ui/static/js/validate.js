(function( $ ){
	var Conf = {
		passed: null,
		failed: null,
	};

	var failedCount = 0;

	var processValidation = function( thisConf, error_message, $input ) {
		if ( typeof error_message == 'undefined' || error_message == true ) {
			return;
		}

		thisConf.set(error_message, $input);
		
		failedCount++;
		return false;
	};

	var processRule = function( thisConf, $input ) {
		var attr = $input.attr( 'validate' ).split( ':' ), //array of params
			requirement = attr[1],
			value = $input.val(), //link to input value
			rule = attr[0];

		thisConf.hide( $input );

		//checks if field is required, and length 
		if ( isNaN( requirement ) === false && requirement && value.length < requirement ) {
			return processValidation( thisConf, 'Must be ' + requirement + ' characters', $input );
		}

		//checks if empty to stop processing 
		if ( isNaN( requirement ) === false && value.length === 0 ) {
			return;
		}

		if ( rule in thisConf.rule ) {
			return processValidation( thisConf, thisConf.rule[rule].apply( this, [value, requirement] ), $input );
		}
	};
		
	$.fn.validate = function( ConfObj, event ) {
		event = event || window.event;
		
		failedCount = 0; //reset failed count ever time function is ran
		var isForm = false;

		if( typeof ConfObj === 'function' && ConfObj != event ){
			ConfObj = {
				passed: ConfObj
			}
		}
		var thisConf = $.extend( true, Conf, ConfObj );

		if( this.is( '[validate]' ) ){
			processRule( thisConf, this );

		}else{
			isForm = true;
			this.find( '[validate]' ).each( function (){
				processRule( thisConf, $( this ) );

			});
		}

		if( failedCount === 0 ) { //no errors
			if( this.is( '[validatePassed]' ) ){
				thisConf.passed = window[ this.attr( 'validatePassed' ) ];
			}

			if( isForm && (typeof thisConf.passed === 'function') ){
				thisConf.passed( this, thisConf, event );
			}

			return true;
		} else { //errors
			if( this.is( '[validateFailed]' ) ){
				thisConf.failed =  window[ this.attr( 'validateFailed' ) ]
			}

			if( isForm  && (typeof thisConf.failed === 'function') ){
				thisConf.failed( this, thisConf, failedCount, event );
			}

			//stops form from precessing
			event.preventDefault();
			event.defaultPrevented;
			return false;
		}
	};

	$.fn.validateOnSubmit = function( ConfObj, event ) {
		//$( this ).off(); //clear old bind event
		$( this ).on( 'submit', function ( event ){
			$( this ).validate( ConfObj, event );
		});
	};

	jQuery.extend({
		validateConf: function( ConfObj ) {
			if(!ConfObj) return Conf ;
			$.extend( true, Conf, ConfObj );
		},
		validateInit: function( ConfObj ) {
			//$( this ).off(); //clear old bind event
			$( '[action]' ).on( 'submit', function ( event ){
				$( this ).validate( ConfObj, event );
			});
		},
		validateTestRule: function( rule, value ){

			//console.log(arguments)
			if ( Conf.rule[ rule ]( value ) ){
				return false;
			}else{
				return true;
			}
		}
	});
}( jQuery ));

//load configuration object globally
$.validateConf({
	//function to set error messages for input fields.
	set: function( error_message, $input ){
		$( '<b>' ).html( ' - ' + error_message ).appendTo( $input.siblings( 'label' ) );
		$input.css('background-color', '#FFFF66');
		$input.parent().addClass( "has-error" );
	},

	//must remove what ever the set function did.
	hide: function( $input ){
		$input.siblings( 'label' ).children( 'b' ).remove(); //removes old error
		$input.css('background-color', '#ffffff');
		$input.parent().removeClass( "has-error" ); //removes has-error class
	},
	//rules to be called during validation processing
	rule:{
		eq: function( value, options ){

			//validates with 2 fields are equal
			//the option argument takes the name of the input to match too
			var compare = $( '[name=' + options + ']' ).val();

			if( value != compare ){
				return "Miss-match";
			}
		},
		ip: function( value ) {

			//validates IPv4 address

			var reg = /(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)/;
			if ( !reg.test( value ) ) {
				return "IP is out of range; Malformed";
			}

			value = value.split( '.' );// split into octets

			if(value.length != 4) return "IP is out of range; Malformed";

		},
		host: function( value ) {
			
			//validates legal host name match of
			//needs more testing
			var reg = /^(?=.{1,255}$)[0-9A-Za-z](?:(?:[0-9A-Za-z]|-){0,61}[0-9A-Za-z])?(?:\.[0-9A-Za-z](?:(?:[0-9A-Za-z]|-){0,61}[0-9A-Za-z])?)*\.?$/;
			if ( !reg.test( value ) ) {
				return "Invalid";
			}
		},
		FQDN: function( value ) {

			//validates a Fully Qualified Domain Name
			var reg = /(?=^.{4,255}$)(^((?!-)[a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,63}$)/;
			if ( !reg.test( value ) ) {
				return "Invalid";
			}
		},
		user: function( value ) {

			//validates user name with letter, numbers, -, _, . and @ only. Emails are allowed
			var reg = /^[a-z0-9\_\-\@\.]{1,32}$/i;
			if ( !reg.test( value ) ) {
				return 'Invalid';
			}
		},
		email: function( value ){

			//validated email address
			//more testing
			var pattern = new RegExp(/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i);
				if( !pattern.test( value ) ){
					return 'Invalid';
				}
		},
		password: function( value ){

			//simple password check must have 1 number 1 up case
			var reg = /^(?=[^\d_].*?\d)\w(\w|[!@#$%]){1,256}/;
			if ( !reg.test( value ) ) {
				return 'Try again'; // "try again"? <-- fuck you!
			}
		},
		URLpub: function( value ){ //Credit Amos here

			var exp = /^(https?|ftp):\/\/(((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:)*@)?(((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]))|((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?)(:\d*)?)(\/((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)+(\/(([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)*)*)?)?(\?((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|[\uE000-\uF8FF]|\/|\?)*)?(\#((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|\/|\?)*)?$/i;			var regex = new RegExp( exp );

			if ( !regex.test( value ) ) {
				return "Not a Valid URL";
			}
		}
	},
});
