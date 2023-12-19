function validate_form() {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    let forms = document.querySelectorAll('.needs-validation');

  // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) {
                if (!form.checkValidity()) {
                    event.preventDefault();
                    event.stopPropagation();
                }

            form.classList.add('was-validated');
          }, false)
    });
}

function check_box_name_from() {
    $('#check-name_from').change(function() {
        input = $('#id_name_from');

        if ($(this).is(':checked')) {
            input.attr('required', false);
            input.val('');
            input.attr('disabled', true);
        } else {
            input.attr('required', true);
            input.attr('disabled', false);
        }
    });
}

$(function () {
    validate_form();
    check_box_name_from();
});