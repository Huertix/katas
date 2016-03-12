
var hash = {
	'rock-paper':'lose',
	'scissors-rock':'lose',
	'paper-scissors':'lose',
	'rock-scissors':'wins',
	'scissors-paper':'wins',
	'paper-rock':'wins',
	'rock-rock':'tie',
	'scissors-scissors':'tie',
	'paper-paper':'tie'
}

function game(hand1,hand2){
	return hash[hand1+'-'+hand2];
}



describe("game1 - tie", function() {
	it("rock vs rock", function() {
		expect(game('rock','rock')).toBe("tie");		
	});
	it("scissors vs scissors", function() {
		expect(game('scissors','scissors')).toBe("tie");		
	});
	it("paper vs paper", function() {
		expect(game('paper','paper')).toBe("tie");		
	});
});

describe("game2 - win", function() {
	it("rock vs scissors", function() {
		expect(game('rock','scissors')).toBe("wins");		
	});
	it("scissor vs paper", function() {
		expect(game('scissors','paper')).toBe("wins");		
	});
	it("paper vs rock", function() {
		expect(game('paper','rock')).toBe("wins");		
	});
});

describe("game3 - lose", function() {
	it("rock vs paper", function() {
		expect(game('rock','paper')).toBe("lose");		
	});
	it("scissors vs rock", function() {
		expect(game('scissors','rock')).toBe("lose");		
	});
	it("rock vs paper", function() {
		expect(game('paper','scissors')).toBe("lose");		
	});
});
