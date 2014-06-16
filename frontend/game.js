var cells = $('td'),
    memory = [],
    piece = $("#piece_storage").html().trim(),
    user = piece,
    computer = piece === 'O' ? 'X' : 'O';

if (piece === "O") {
    var move = $("#move_storage").html().trim(),
        cell = $("#" + move);
    cell.html(computer);
}

function tableResize() {
    "use strict";
    var w = $(window).width(),
        h = $(window).height(),
        table = $("table"),
        d = Math.min(w, h);
    table.width(0.9 * d);
    table.height(0.9 * d);
    $("td").css('font-size', 0.9 * 0.3 * 0.9 * d);
}
tableResize();
$(window).resize(tableResize);


function state(cell) {
    "use strict";
    if (cell.innerHTML === user) {
        return -1;
    } else if (cell.innerHTML === computer) {
        return 1;
    } else {
        return 0;
    }
}

function getBoard() {
    "use strict";
    var board = '';
    cells.each(function () {
        board += String(state(this)) + ',';
    });
    return board.slice(0, -1);
}

function makeMove(event) {
    "use strict";
    cells.off();
    var cell = event.target,
        board = getBoard();
    if (state(cell) === 0) {
        memory.push("\"" + getBoard() + "\"," + cell.id + ",-1,");
        cell.innerHTML = user;
        $.ajax({
            type: 'POST',
            url: './play.py',
            data: {
                'board': getBoard()
            },
            success: function (data) {
                move = data.trim();
                if ('123456789'.search(move) !== -1) {
                    //console.log(move)
                    var move_cell = document.getElementById(move);
                    memory.push("\"" + getBoard() + "\"," + move_cell.id + ",1,");
                    move_cell.innerHTML = computer;
                } else {
                    endGame(move);
                }
                cells.click(makeMove);
            },
            async: true
        });
        //console.log(move)
    }
}
cells.click(makeMove);

function endGame(move) {
    "use strict";
    //console.log(winner);
    var el = $("#overlay"),
        p = el.find('p'),
        winner = move.split('\n'),
        lane = winner.length > 1 ? winner[1].split(',') : [],
        outcome;
    el.toggleClass('visible');

    if (winner[0] === "user") {
        outcome = -1;
        p.html("You&rsquo;ve won!");
        p.addClass('win');
        $.each(lane, function (i, val) {
            $("#" + val).addClass('win');
        });
    } else if (winner[0] === "computer") {
        outcome = 1;
        p.html("Sorry you lost!");
        p.addClass('lose');
        $.each(lane, function (i, val) {
            cell = $("#" + val);
            cell.html(computer);
            cell.addClass('lose');
        });
    } else if (winner[0] === "tie") {
        outcome = 0;
        p.html("A tie!");
        p.addClass('tie');
        $.each(lane, function (i, val) {
            cell = $("#" + val);
            cell.html(computer);
        });
    }
    cells.off('click');
    $.each(memory, function (i, val) {
        memory[i] = val + String(outcome) + ',';
    });
    $.ajax({
        type: 'POST',
        url: './memory.py',
        data: {
            'memory': memory.join('\n')
        },
        success: function (data) {
            //console.log(data)
        },
        async: true
    });
}
