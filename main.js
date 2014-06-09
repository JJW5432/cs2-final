var cells = document.getElementsByTagName('td');

function coords(n) {
	var ys = [1, 1, 1, 0, 0, 0, -1, -1, -1],
		xs = [-1, 0, 1, -1, 0, 1, -1, 0, 1],
		y = ys[n-1],
		x = xs[n-1];
	return [x,y]
}

function state(cell) {
  if (cell.innerHTML === "O") {return -1}
  else if (cell.innerHTML === "X") {return 1}
  else {return 0}
}

function getMove(){
	var request = new XMLHttpRequest(),
	   board = '';  
	for (var i=0; i<cells.length; i++){
		cell = cells[i];
		coord = coords(Number(cell.id))
		board += String(coord[0]) + ',' + String(coord[1]) + ',' + String(state(cell)) + ','
	}
    board = board.slice(0,-1);
    console.log(board);
	/*request.open('POST', './move.py', true);

	request.onload = function() {
  		if (request.status >= 200 && request.status < 400){
    		// Success!
    		resp = request.responseText;
 			} else {

  			}
  	return resp*/
  	return "1"
};

/*request.onerror = function() {
  // There was a connection error of some sort
};

request.send();
}*/

function makeMove(event) {
	var cell = event.target
	if (state(cell) === 0) {
		move = getMove(cell);
		if ('123456789'.search(move) != -1) {
			cell.innerHTML = 'O';
			document.getElementById(move).innerHTML = 'X';
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
