function getMove(cell){
	return '1'
}

function makeMove(event) {
	var cell = event.target
	if (cell.getAttribute("state") === "0") {
		move = getMove(cell);
		if ('123456789'.search(move) != -1) {
			cell.setAttribute('data-state', '-1');
			document.getElementById(move).setAttribute('data-state', '1');
		}
		else if (move === "user") { //the game is won
			endGame(true);
		}
		else {
			endGame(false)
		}
	}
}
	
function endGame(won) {
	var el = document.getElementById("overlay");
	el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
	if (won) {
		el.getElementsByTagName('p')[0].innerHTML = "You've won!";
	} else {
		el.getElementsByTagName('p')[0].innerHTML = "Sorry you lost!";
	}
	var cells = document.getElementsByTagName('td');
	for (var i in cells) {
		var cell = cells[i];
		cell.onclick=null;
	}
}

var cells = document.getElementsByTagName('td');
for (var i in cells) {
	var cell = cells[i];
	cell.onclick = makeMove;
}