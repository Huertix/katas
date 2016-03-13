var hand = require('./hand.js');

function game(hand1, hand2){
	var bet1 = hand(hand1);
	var bet2 = hand(hand2);
	return bet1.playAgaint(bet2.getName());
}



describe("Rock", function() {
	it("rock vs scissors -> rock wins", function() {
		expect(game('rock', 'scissors')).toBe('wins');	
	});
	it("rock vs rock -> tie", function() {
		expect(game('rock','rock')).toBe('tie');	
	});
	it("rock vs paper -> rock lose", function() {
		expect(game('rock','paper')).toBe('lose');	
	});
});

describe("Paper", function() {
	it("paper vs scissors -> rock wins", function() {
		expect(game('paper', 'scissors')).toBe('lose');	
	});
	it("paper vs rock -> tie", function() {
		expect(game('paper','rock')).toBe('wins');	
	});
	it("paper vs paper -> rock lose", function() {
		expect(game('paper','paper')).toBe('tie');	
	});
});

describe("Scissors", function() {
	it("scissors vs scissors -> tie", function() {
		expect(game('scissors', 'scissors')).toBe('tie');	
	});
	it("scissors vs rock -> scissors lose", function() {
		expect(game('scissors','rock')).toBe('lose');	
	});
	it("scissors vs paper -> scissors wins", function() {
		expect(game('scissors','paper')).toBe('wins');	
	});
});
