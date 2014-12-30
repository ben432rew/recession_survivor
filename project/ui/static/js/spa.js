( function( $ ){
	"use strict";

	var Spa = function () {

		var Spa = {
			update: function ( url ) {
				Spa.dom.$ajaxLoadingImage.show()
				this.dom.$body.css( {
					cursor: 'wait'
				} );

				// $jq.__currentPage.unloadPage();

				this.resetCurrentPage();

				this.dom.$content.hide( function (){
					$.ajax( {
						url: url,
						method: 'GET',
						success: function( data ) {
							Spa.dom.$ajaxLoadingImage.hide()
							Spa.dom.$content.html( data ).show();

							Spa.dom.$body.css( {
								cursor:'auto'
							} );
						},
						crossDomain: false
					});
				});
			},
			resetCurrentPage: function(){
				this.__currentPage = {
					unloadEvent: function(){}
				};
			},
			dom : {}
		}

		return Spa
	};

	jQuery.extend( {
		Spa: Spa()
	} );

	if ( 'pushState' in history ){
		console.log('ran')
		// Convert links

		$( window ).on( "popstate", function( event ) {
			$.Spa.update( history.state.url );
		} );
		
		$( document ).ready( function(){
			// cache some dom elements
			$.Spa.dom.$body = $( 'body' );
			$.Spa.dom.$content = $( 'main' );
			$.Spa.dom.$ajaxLoadingImage = $( '#ajaxLoadingImage' );

			$( 'body' ).on('click', 'a.ajax', function( event ){

				//stop link from firing
				event.preventDefault();
				var url = $( this ).attr( 'href' );

				history.pushState( { url: url }, '', url );
				$.Spa.update( url );

				return ;
			} );

		} );

	}
} )( jQuery );

(function($){
    $.fn.serializeObject = function(){

        var self = this,
            json = {},
            push_counters = {},
            patterns = {
                "validate": /^[a-zA-Z][a-zA-Z0-9_]*(?:\[(?:\d*|[a-zA-Z0-9_]+)\])*$/,
                "key":      /[a-zA-Z0-9_]+|(?=\[\])/g,
                "push":     /^$/,
                "fixed":    /^\d+$/,
                "named":    /^[a-zA-Z0-9_]+$/
            };


        this.build = function(base, key, value){
            base[key] = value;
            return base;
        };

        this.push_counter = function(key){
            if(push_counters[key] === undefined){
                push_counters[key] = 0;
            }
            return push_counters[key]++;
        };

        $.each($(this).serializeArray(), function(){

            // skip invalid keys
            if(!patterns.validate.test(this.name)){
                return;
            }

            var k,
                keys = this.name.match(patterns.key),
                merge = this.value,
                reverse_key = this.name;

            while((k = keys.pop()) !== undefined){

                // adjust reverse_key
                reverse_key = reverse_key.replace(new RegExp("\\[" + k + "\\]$"), '');

                // push
                if(k.match(patterns.push)){
                    merge = self.build([], self.push_counter(reverse_key), merge);
                }

                // fixed
                else if(k.match(patterns.fixed)){
                    merge = self.build([], k, merge);
                }

                // named
                else if(k.match(patterns.named)){
                    merge = self.build({}, k, merge);
                }
            }

            json = $.extend(true, json, merge);
        });

        return json;
    };
})(jQuery);
