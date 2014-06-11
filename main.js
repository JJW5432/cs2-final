var cells = $('td'),
	memory = []

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

function getBoard() {
    board = '';  
    cells.each(function(){
		coord = coords(Number(this.id))
		board += String(coord[0]) + ',' + String(coord[1]) + ',' + String(state(this)) + ','
    })
    return board.slice(0,-1)
}

function getMove(){
    var board = getBoard(), results;
    $.post('./move.py', {'board':board})
    	.done(function(data){
    		results = data
    	});
    return results.trim()
};

function makeMove(event) {
	var cell = event.target
	if (state(cell) === 0) {
	    cell.innerHTML = 'O';
	    memory.append("\""+getBoard()+"\","+cell.id+",-1,")
	    move = getMove(cell);
	    if ('123456789'.search(move) != -1) {
	    	move_cell = document.getElementById(move)
			move_cell.innerHTML = 'X';
			memory.append("\""+getBoard()+"\","+move_.id+",1,")
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
