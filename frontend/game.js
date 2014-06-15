var cells = $('td'),
memory = [],
piece = $("#piece_storage").html().trim()
user = piece
computer = piece == 'O' ? 'X' : 'O'
if (piece === "O") {
    move = $("#move_storage").html().trim()
    cell = $("#" + move)
    cell.html(computer)
}
cells.click(makeMove)


function tableResize() {
                var w = $(window).width(),
                    h = $(window).height(),
                    table = $("table"),
                    d = Math.min(w,h);
                table.width(0.9*d);
                table.height(0.9*d)
            }
            tableResize();
            $(window).resize(tableResize)


function state(cell) {
    if (cell.innerHTML === user) {return -1}
    else if (cell.innerHTML === computer) {return 1}
    else {return 0}
}

function getBoard() {
    board = '';
    cells.each(function(){
    board += String(state(this)) + ','
    })
    return board.slice(0,-1)
}

function makeMove(event) {
    cells.off()
    var cell = event.target
    if (state(cell) === 0) {
    board = getBoard()
    memory.push("\""+getBoard()+"\","+cell.id+",-1,");
    cell.innerHTML = user;
    $.ajax({
        type: 'POST',
        url: './play.py',
        data: {'board':getBoard()},
        success: function(data){
        move = data.trim()
        if ('123456789'.search(move) != -1) {
            console.log(move)
                move_cell = document.getElementById(move)
            memory.push("\""+getBoard()+"\","+move_cell.id+",1,")
            move_cell.innerHTML = computer;
        }
        else {endGame(move)}
        cells.click(makeMove)
        },
        async:true
    });
    //console.log(move)
    }
}

    function endGame(winner) {
    console.log(winner)
    var el = $("#overlay"),
    p = el.find('p'),
    winner = winner.split('\n'),
    outcome;
    el.toggleClass('visible')
    lane = winner[1].split(',')
    if (winner[0] === "user") {
        outcome = -1
        p.html("You&rsquo;ve won!");
        p.addClass('win');
        $.each(lane,function(i, val){
        $("#"+val).addClass('win')
        })
        } else if (winner[0] === "computer") {
            outcome = 1
            p.html("Sorry you lost!");
            p.addClass('lose');
            $.each(lane,function(i, val){
            cell = $("#"+val)
            cell.html(computer)
            cell.addClass('lose')
            })
            } else if (winner[0] === "tie") {
                outcome = 0
                p.html("A tie!");
                p.addClass('tie');
                $.each(lane,function(i, val){
                cell = $("#"+val)
                cell.html(computer)
                })
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
