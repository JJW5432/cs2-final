function toggle(){
	$(".piece").each(function(i){
		$(this).toggleClass('selected')
		$(this).off()
		$(".piece").not('.selected').click(toggle)
	})
}

$(".piece").not('.selected').click(toggle)
play = $("h2")
play.click(function(){
	piece = $(".piece.selected").html()
	$("form #piece").val(piece)
	$("form").submit()
})