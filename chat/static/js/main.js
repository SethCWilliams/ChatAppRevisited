(function ($) {
    $(function () {
        // console.log('Ready to go!');

        var csrftoken = $("[name=csrfmiddlewaretoken]").val();

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        function showMessageItem(message) {
            let date = moment(message['date']).format('MMMM Do YYYY, h:mm:ss a');
            console.log(message);
            var user_id = $('#user_id').val();
            console.log(user_id);
            var message_class = '';
            console.log(message['user']['id']);
            if (parseInt(user_id) === parseInt(message['user']['id'])) {
                 message_class = 'my_message';
            } else {
                 message_class = 'other_message';
            }
            $('#message_container').append('<div id="message_div" class="'+ message_class + '"><p id="username_message">' + message.user.username + '</p><p id="text_message">' + message.text + '</p><p id="date_message">' + date + '</p></div>');

        }

        $('#add-text-form').on('submit', function (event) {
            event.preventDefault();

            var messageTypedIn = $('#messages').val();
            var user = localStorage.getItem('logged_in_user');
            console.log(messageTypedIn);

            $.ajax('/api/message/', {
                'method': 'POST',
                'data': {'text': messageTypedIn},
                'success': function (data) {
                    $('#messages').val('');
                    console.log('success!');
                    // showMessageItem(data);
                },
                'error': function (xhr) {
                    console.log(xhr.statusText);
                }
            });
            // showMessageItem(data);
            console.log('Add Message')
        });

        function updateScroll() {
            var element = document.getElementById("message_container");
            element.scrollTop = element.scrollHeight;
        }
        function loadMessages() {
            $.ajax('/api/message/', {
                'method': 'GET',
                'success': function (data) {
                    $('#message_container').empty();
                    data.forEach(function (message) {
                        showMessageItem(message)
                    });
                    updateScroll();
                },
                'error': function (xhr) {
                    console.log(xhr.statusText);
                }
            });
        }

        setInterval(loadMessages, 1000);


    });

}(jQuery));
