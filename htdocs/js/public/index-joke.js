$('#main-joke-button').on('click', function (e) {
        e.preventDefault();
        let $button = $(this);
        let apiURL = $button.attr('href');

        $.ajax({
            url: apiURL,
            method: 'GET',
        }).done(function (data, status, xhr) {
            if (xhr?.status == 200) {
                // $('#joke-container').html(data?.text);
            }
        }).fail(function (e) {

        })
    }
)