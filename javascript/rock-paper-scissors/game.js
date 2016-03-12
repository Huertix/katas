function game(hand1,hand2){
	if(hand1 == hand2)
		return 'tie';
	else if(hand1 == 'rock' && hand2=='paper')
		return 'lose';
	else if(hand1 == 'scissors' && hand2=='rock')
		return 'lose';
	else if(hand1 == 'paper' && hand2=='scissors')
		return 'lose';
	else if(hand1 == '' && hand2=='')
		return 'lose';
	else if(hand1 == '' && hand2=='')
		return 'lose';
	else
		return 'wins';
}



/*
rules:
	#done rock vs rock -> tie
	rock vs scissors -> wins
	rock vs paper -> lose
	scissors vs rock -> lose
	#done scissors vs scissors -> tie
	scissors vs paper -> wins
	paper vs rock -> wins
	paper vs scissors -> lose
	#done paper vs paper -> tie
*/
describe("game1", function() {
	it("rock vs rock", function() {
		expect(game('rock','rock')).toBe("tie");		
	});
});
describe("game2", function() {
	it("rock vs scissors", function() {
		expect(game('rock','scissors')).toBe("wins");		
	});
});
describe("game3", function() {
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
