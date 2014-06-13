var cells = $('td'),
	memory = []
cells.click(makeMove)


function state(cell) {
  if (cell.innerHTML === "O") {return -1}
  else if (cell.innerHTML === "X") {return 1}
  else {return 0}
}

function getBoard() {
    board = '';  
    cells.each(function(){
		board += String(state(this)) + ','
    })
    return board.slice(0,-1)
}

function getMove(){
    var board = getBoard(), results;
    $.ajax({
	type: 'POST',
	url: './play.py',
	data: {'board':board},
	success: function(data){
	    var move = data.trim()
	    if ('123456789'.search(move) != -1) {
	    	move_cell = document.getElementById(move)
		move_cell.innerHTML = 'X';
		memory.push("\""+getBoard()+"\","+move_cell.id+",1,")	
	    }
	    else {endGame(move)};
	    cells.click(makeMove)
},
	async:true
	});
    return false
};

function makeMove(event) {
    var cell = event.target;
    cells.off('click')
	if (state(cell) === 0) {
	    memory.push("\""+getBoard()+"\","+cell.id+",-1,");
	    cell.innerHTML = 'O';
	    getMove(cell);
	}
        return false
}
	
function endGame(winner) {
    console.log(winner)
    var el = $("#overlay"),
    p = el.find('p'),
    winner = winner.split('\n'),
    outcome;
	el.toggleClass('visible')
	if (winner[0] === "user") {
	    outcome = -1*(9-memory.length+1)
	    if (outcome === -5) {outcome=-9}
	    lane = winner[1].split(',')
	    p.html("You&rsquo;ve won!");
		p.addClass('win');
	    $.each(lane,function(i, val){
		$("#"+val).addClass('win')
	    })
	} else if (winner[0] === "computer") {
	    outcome = 9-memory.length+1
	    lane = winner[1].split(',')
	    p.html("Sorry you lost!");
	    p.addClass('lose');
	    $.each(lane,function(i, val){
		cell = $("#"+val)
		cell.html('X')
		cell.addClass('lose')
	    })
	} else if (winner[0] === "tie") {
	    outcome = 3
	    p.html("A tie!");
	    p.addClass('tie');
	}
	cells.off('click')
    $.each(memory, function(i, val){
	memory[i] = val + String(outcome) + ',';
    })
	$.ajax({
		type: 'POST',
		url: './memory.py',
		data: {'memory':memory.join('\n')},
	    success: function(data){console.log(data)},
		async: true
	});
}
