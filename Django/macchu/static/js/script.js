function change_recommend_button_status() {
    imgs = $('#selected-container img');
    if (imgs.length == 3){
        $("#button-1").attr("disabled", false);
    } else {
        $("#button-1").attr("disabled", true);
    }
}

$(function() {

    $("#button-1").attr("disabled", true);

    $('#beer-container').on('click', 'img', function(event) {
        imgs = $('#selected-container img');
        if (imgs.length < 3) {
            $(this).appendTo($('#selected-container'));
        }

        change_recommend_button_status();
        
    });

    $('#selected-container').on('click', 'img', function(event) {                
        $(this).appendTo($('#beer-container'));

        change_recommend_button_status();
    });
});