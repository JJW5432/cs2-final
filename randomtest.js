function testRandom(){
	var results = {};
	for (var i = 0; i<100; i++){
		$.ajax({
				type: 'POST',
				url: 'http://lisa.stuy.edu/~jake.waksbaum/proj/play.py',
				data: {'board':'1,-1,1,0,1,-1,-1,0,-1'},
				success: function(data){
					x = Number(data.trim())
					if (x in results) {results[x]++} else {results[x] = 1}
				},
				async:false
			});
	}
	return results;
}