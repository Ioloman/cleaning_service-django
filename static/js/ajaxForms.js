function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


$(document).ready(() => {
    $.ajaxSetup({
        headers: {"X-CSRFToken": getCookie("csrftoken")}
    });
    $("#editButton").on("click", (event) => {
        if ($("input[required]").val().length !== 0) {
            event.preventDefault();
            const button = $("#editButton");
            $.ajax({
                url: button.attr("formaction"),
                data: button.parents("form").serialize(),
                type: "PUT",
                dataType: "json"
            }).done((data, textStatus, jqXHR) => {
                if (data.status === 'Success'){
                    window.location.href = data.redirectTo;
                    alert('Успешно')
                }
                else
                    alert('Ошибка');
            }).fail((jqXHR, textStatus, error) => {
                alert(`Error: ${textStatus} ${error}`)
            });
        }
    });
    $("#deleteButton").on("click", (event) => {
        event.preventDefault();
        const button = $("#deleteButton");
        $.ajax({
            url: button.attr("formaction"),
            type: "DELETE",
            dataType: "json"
        }).done((data, textStatus, jqXHR) => {
            if (data.status === 'Success')
                window.location.href = data.redirectTo;
            else
                alert('Ошибка');
        }).fail((jqXHR, textStatus, error) => {
            alert(`Error: ${textStatus} ${error}`)
        });
    });
    $("#createButton").on("click", (event) => {
        if ($("input[required]").val().length !== 0) {
            event.preventDefault();
            const button = $("#createButton");
            $.ajax({
                url: button.attr("formaction"),
                data: button.parents("form").serialize(),
                type: "POST",
                dataType: "json"
            }).done((data, textStatus, jqXHR) => {
                if (data.status === 'Success') {
                    window.location.href = data.redirectTo;
                    alert('Успешно')
                }
                else
                    alert('Ошибка');
            }).fail((jqXHR, textStatus, error) => {
                alert(`Error: ${textStatus} ${error}`)
            });
        }
    });

});