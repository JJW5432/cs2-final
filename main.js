var cells = document.getElementsByTagName('td');

function coords(n) {
	var ys = [1, 1, 1, 0, 0, 0, -1, -1, -1],
		xs = [-1, 0, 1, -1, 0, 1, -1, 0, 1],
		y = ys[n-1],
		x = xs[n-1];
	return [x,y]
}

function getMove(cell){
	request = new XMLHttpRequest();
	board = '';
	for (var i in cells) {
		cell = cells[i];
		coord = coords(Number(cell.id))
		board += String(coord[0]) + ',' + String(coord[1]) + String(cell.getAttribute("state"))
	}
	/*request.open('POST', './move.py', true);

	request.onload = function() {
  		if (request.status >= 200 && request.status < 400){
    		// Success!
    		resp = request.responseText;
 			} else {

  			}
  	return resp*/
  	return board;
};

request.onerror = function() {
  // There was a connection error of some sort
};

request.send();
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


for (var i in cells) {
	var cell = cells[i];
	cell.onclick = makeMove;
}