pieces = $(".piece")
pieces.click(function(){
	$(".piece").each(function(i){
		$(this).toggleClass('selected')
	})
})
play = $("h2")
play.click(function(){
	piece = $(".piece.selected").html()
	$("form #piece").val(piece)
	$("form").submit()
})