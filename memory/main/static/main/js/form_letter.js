function to_back_button() {
    $('.letter-front-side').on('click', 'button', function() {
        if ($('.letter-back-side').hasClass('turn-front')) {
                $('.letter-back-side').removeClass('turn-front');
            }
        $('.letter-front-side').addClass('turn-back');
        $('.letter-back-side').addClass('see');
    });
}

function to_front_button() {
    $('.letter-back-side').on('click', 'button[name=back]', function() {
        $('.letter-back-side').removeClass('see');
        $('.letter-back-side').addClass('turn-front');
        $('.letter-front-side').removeClass('turn-back');
    });
}

$(function() {
    to_back_button();
    to_front_button();
});