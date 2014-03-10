$(document).ready(function() {
	
    // lab slider toggles
    $('.excursion').find('.price').hide().end().find('.toggle').click(function() {
            $(this).siblings('.price').slideToggle();
    });
});