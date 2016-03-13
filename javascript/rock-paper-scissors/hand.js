//closure
module.exports = function(name){

	var _name = name;

	return{
		getName:	function() { return _name},
		playAgaint:	function(other) { 
							
							switch( _name ){
							
							case other: return 'tie'; break;
							
							case 'rock':
								if(other === 'scissors')
									return 'wins';
								else if(other === 'paper')
									return 'lose';
								break;
							
							case 'paper':
								if(other === 'rock')
									return 'wins';
								else if(other === 'scissors')
									return 'lose';	
								break;
							
							case 'scissors':
								if(other === 'paper')
									return 'wins';
								else if(other === 'rock')
									return 'lose';	
								break;
							}
		}							
	}
}
