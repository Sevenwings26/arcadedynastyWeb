
$(document).ready(function() {
    $('#register-submit').on('click', function(event) {
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url: '{% url "signup" %}',
            data: {
                username: $('#register-username').val(),
                email: $('#register-email').val(),
                password1: $('#register-password').val(),
                password2: $('#register-confirm-password').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(response) {
                if (response.success) {
                    window.location.href = '/';
                } else {
                    alert('Signup failed. Please try again.');
                }
            },
            error: function(response) {
                alert('Signup failed. Please try again.');
            }
        });
    });

    $('#login-submit').on('click', function(event) {
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url: '{% url "login" %}',
            data: {
                username: $('#login-email').val(),
                password: $('#login-password').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(response) {
                if (response.success) {
                    window.location.href = '/';
                } else {
                    alert('Login failed. Please try again.');
                }
            },
            error: function(response) {
                alert('Login failed. Please try again.');
            }
        });
    });
});
