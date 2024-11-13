document.addEventListener('DOMContentLoaded', function() {
    var alertSuccess = document.querySelector('.alert-success');
    if (alertSuccess) {
        alertSuccess.classList.add('fade-out');

        setTimeout(function() {
            alertSuccess.classList.add('hidden');
        }, 3000);
    }
});
