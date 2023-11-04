$(document).ready(function($) {
    $('.wrap-table table tbody tr[data-href]').on('click', function() {
        window.location = $(this).data("href");
    });
});