/*
>>>>>>> 80d7f48aaff1a75e14b4155961de7b8863fa0163
$(document).ready(function(){
    $("#str").click(function(){
        $(this).hide();
	});
<<<<<<< HEAD
});
=======
});
*/

$(function (){
    if($('#character').val()== "true"){
         $("input:checkbox").prop('checked',true);
    }else{
        $("input:checkbox").prop('checked', false);
    }
});
