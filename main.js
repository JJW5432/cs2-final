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
	var message = document.createElement("H3");
	if (won) {
		message.innerHTML = "You've won!";
	} else {
		message.innerHTML = "Sorry you lost!";
	}
	document.body.appendChild(message);
	var cells = document.getElementsByTagName('td');
	for (var i in cells) {
		var cell = cells[i];
		cell.removeEventListener('click', makeMove);
	}
}

var cells = document.getElementsByTagName('td');
for (var i in cells) {
	var cell = cells[i];
	cell.onclick = makeMove;
}