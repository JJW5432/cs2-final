function testRandom(board) {
    "use strict";
    var results = {};
    for (var i = 0; i < 100; i++) {
        $.ajax({
            type: 'POST',
            url: 'http://lisa.stuy.edu/~jake.waksbaum/proj/play.py',
            data: {
                'board': board
            },
            success: function(data) {
                var x = Number(data.trim())
                if (x in results) {
                    results[x]++
                } else {
                    results[x] = 1
                }
            },
            async: false
        });
    }
    return results;
}
