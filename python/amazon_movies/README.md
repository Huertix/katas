There is a network of similar movies which are attributed by a unique identifier and a rating. each movie in the network is realted to one or more movies in the network throught a direct connection.

Design a way to find th N highest rated movies for a given movie in the network of realted movies. The original movie should not be considered as a potential recommendation. if the number of requested movies is greater than the total number of movies, then output all the related movies

Input
The input to the function/method consists of two arguments - movie, representing the node of the origianl movie in the movie network and N, an integer representing the number of requested movies.

Output
Return a list containing the nodes of the N highest rated movies.

Constraints
0 <= N

Note:

		A(5.0)
		 /\
		/  \
   B(6.2)   C(6.0)
        \  / 
         \/
       C(7.0)
       
Input:
movie = A
N = 10

Output:
B,C,D

Explanation:
Although 10 movies are requested, but only 3 related movies are available. So, the ouput is B, C, D.

Helper Description
The following class is used to represent a movie:

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



# RETURN AN EMPTY LIST IF NO SIMILAR MOVIE TO THE GIVEN MOVIE IS FOUND
def getMovieRecommedation(movie, N):
	pass