$(function ($) {
    const formId = '#user_reg'
    $(formId).submit(function (e){
        e.preventDefault()
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',
            success: function (response) {
                window.location.reload()
            },
            error: function (response) {
                if (response.status === 400) {
                    $('.text-danger').each((index, el) => {
                        $(el).remove()
                    })
                    for (let key in response.responseJSON.errors) {
                        $(formId).find('input[name="' + key + '"]').after(() => {
                            let result = ''
                            result += response.responseJSON.errors[key] + '<br>'
                            return '<div class="text-danger">' + result + '</div>'
                        })
                        //$('.text-danger').text(response.responseJSON.errors).removeClass('d-none')
                    }
                }
            }
        })
    })

    $('#user_login').submit(function (e){
        e.preventDefault()
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',
            success: function (response) {
                window.location.reload()
            },
            error: function (response) {
                if (response.status === 400) {
                    $('.text-danger').text(response.responseJSON.error).removeClass('d-none')
                }
            }
        })
    })

    $('#book_add').submit(function (e){
        e.preventDefault()
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',
            success: function (response) {
                window.location.href = '/success';
            },
            error: function (response) {
                if (response.status === 400) {
                    $('.text-danger').text(response.responseJSON.error).removeClass('d-none')
                }
            }
        })
    })
})