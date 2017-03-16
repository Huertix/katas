import random

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
		self.similar.append(movie)



def getMovieRecommedation(movie, N):
	pass

def init(seed):

	random.seed(seed)
	movie_list =[]

	for x in range (1, 21):
		score = round(random.uniform(0, 9), 1)
		movie = Movie(x, score)
		movie_list.append(movie)

	for movie in movie_list:
		for x in range(0, random.randint(0, 10)):
			index = random.randint(0, 19)
			movie.addSimilarMovies(movie_list[index])

	return movie_list


def main():

	movie_list = init(10)



main()
