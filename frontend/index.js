function toggle() {
    "use strict";
    $(".piece").each(function (i) {
        $(this).toggleClass('selected');
        $(this).off();
    });
    $(".piece").not('.selected').click(toggle);
}

$(".piece").not('.selected').click(toggle);
var play = $("h2");
play.click(function () {
    "use strict";
    var piece = $(".piece.selected").html();
    $("form #piece").val(piece);
    $("form").submit();
});
