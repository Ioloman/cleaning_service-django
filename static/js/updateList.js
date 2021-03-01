$(document).ready(() => {
    $("#selectList").change(
        (event) => {
            $.get(
                "/ajax/update-list/",
                {type_: $('#selectList option:selected').val()},
                "html"
            ).done((data, textStatus, jqXHR) => {
                $('#serviceList').html(data)
            }).fail((jqXHR, textStatus, error) => {
                alert(`Error: ${textStatus} ${error}`)
            });
        }
    )
});