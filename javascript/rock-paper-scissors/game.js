function Rock(){
	this.element = 'rock';

	this.playAgainst = function(other){
		if(other == 'scissors')
			return 'wins';
		else if(other == 'paper'){
			return 'lose';
		}
		else
			return 'tie';
	}

	this.getName = function(){
		return this.element;
	}
}

function Paper(){
	this.element = 'paper';

	this.playAgainst = function(other){
		if(other == 'rock')
			return 'wins';
		else if(other == 'scissors'){
			return 'lose';
		}
		else
			return 'tie';
	}

	this.getName = function(){
		return this.element;
	}
}

function Scissors(){
	this.element = 'scissors';

	this.playAgainst = function(other){
		if(other == 'paper')
			return 'wins';
		else if(other == 'rock'){
			return 'lose';
		}
		else
			return 'tie';
	}

	this.getName = function(){
		return this.element;
	}
}


function game(hand1, hand2){
	var bet =  hand1.playAgainst(hand2.getName());
	return bet;
}


describe("Game test", function() {
	it("rock vs scissors -> rock wins", function() {
		expect(game(new Rock(), new Scissors())).toBe('wins');	
	});
	it("rock vs rock -> tie", function() {
		expect(game(new Rock(), new Rock())).toBe('tie');	
	});
	it("rock vs paper -> rock lose", function() {
		expect(game(new Rock(), new Paper())).toBe('lose');	
	});
});

