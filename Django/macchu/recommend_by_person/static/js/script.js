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

data = [
    {"name": "하이트", "ABU": "4%"},
    {"name": "스텔라", "ABU": "6.7%"},
    {"name": "곰표", "ABU": "4.3%"},
    {"name": "말표", "ABU": "6.7%"},
    {"name": "하이트", "ABU": "4.9%"},
    {"name": "기린", "ABU": "6.1%"},
    {"name": "사포로", "ABU": "5%"},
    {"name": "클라우드", "ABU": "3.8%"}, 
    {"name": "테라", "ABU": "8%"},
    {"name": "퇴근길", "ABU": "5.9%"}, 
]
$(function() {
    $('#button-1').on('click', function(event){
        var beer = $('<img></img>');
        var name1 = '곰표';
        // $('#rank-change').load("static/js/rank.txt"); //삭제용참고용
        $("#beer-container").empty();
        $('<img></img>').attr('src','static/images/'+ data[0]['name'] +'.png').appendTo('#recommended-container');
        $('<img></img>').attr('src','static/images/'+ data[0]['name'] +'.png').appendTo('#recommended-1');
        $('<img></img>').attr('src','static/images/'+ data[1]['name'] +'.png').appendTo('#recommended-container');
        $('<img></img>').attr('src','static/images/'+ data[2]['name'] +'.png').appendTo('#recommended-container');
        $('<img></img>').attr('src','static/images/'+ data[3]['name'] +'.png').appendTo('#recommended-container');
        $('<img></img>').attr('src','static/images/'+ data[4]['name'] +'.png').appendTo('#recommended-container');
        $('<img></img>').attr('src','static/images/'+ data[5]['name'] +'.png').appendTo('#recommended-container');
        $('<img></img>').attr('src','static/images/'+ data[6]['name'] +'.png').appendTo('#recommended-container');
        $('<img></img>').attr('src','static/images/'+ data[7]['name'] +'.png').appendTo('#recommended-container');
        $('<img></img>').attr('src','static/images/'+ data[8]['name'] +'.png').appendTo('#recommended-container');
        $('<img></img>').attr('src','static/images/'+ data[9]['name'] +'.png').appendTo('#recommended-container');

        
        $('<img></img>').attr('src','static/images/'+ data[5]['name'] +'.png').appendTo('#ranking-container');
        $('<img></img>').attr('src','static/images/'+ data[4]['name'] +'.png').appendTo('#ranking-container');
        $('<img></img>').attr('src','static/images/'+ data[3]['name'] +'.png').appendTo('#ranking-container');
        $('<img></img>').attr('src','static/images/'+ data[9]['name'] +'.png').appendTo('#ranking-container');
        $('<img></img>').attr('src','static/images/'+ data[8]['name'] +'.png').appendTo('#ranking-container');
        $('<img></img>').attr('src','static/images/'+ data[7]['name'] +'.png').appendTo('#ranking-container');
        $('<img></img>').attr('src','static/images/'+ data[6]['name'] +'.png').appendTo('#ranking-container');
        $('<img></img>').attr('src','static/images/'+ data[2]['name'] +'.png').appendTo('#ranking-container');
        $('<img></img>').attr('src','static/images/'+ data[1]['name'] +'.png').appendTo('#ranking-container');
        $('<img></img>').attr('src','static/images/'+ data[0]['name'] +'.png').appendTo('#ranking-container');

        


    
        
        // $('<img></img>').appendTo('../static/images/'+data[0]['name']+'.png')
        // $('#beer-container').appendTo('../static/images/'+data[0]['name']+'.png')
    });
});
    
    



// var key = ['name_ko','alcohol']
// $(function(){
//     $.ajax({
//         "url": 'http://localhost:8000/search/' + key,
//         "method": "GET",
//         "dataType": "json",
//             // "data" : //
//         "success": function(data1, status, xhr) {
//         }
//     })
// })



