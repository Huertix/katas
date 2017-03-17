class Movie:
	id = None
	rating = None
	similar = None

	def __init__(self, movieId, rating):
		self.id = movieId
		self.rating = rating
		self.similar = []

	def getId(self):
		return self.id

	def getRating(self):
		return self.rating

	def getSimilaMovies(self):
		return self.similar

	def addSimilarMovies(self, movie):
		if movie.getId() == self.id:
			return 
		if movie in self.similar:
			return
		self.similar.append(movie)