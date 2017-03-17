import random
import sys
from movie import Movie
from movies_finder import *


def init_script(seed):

	random.seed(seed)
	movie_list =[]
	total_movies = 10

	for x in range (1, total_movies + 1):
		score = round(random.uniform(0, 10), 1)
		movie = Movie(x, score)
		movie_list.append(movie)

	for movie in movie_list:
		for x in range(0, random.randint(0, 10)):
			index = random.randint(0, total_movies - 1)
			movie.addSimilarMovies(movie_list[index])

	return movie_list


def main(movie_id=int(sys.argv[1]), movies_to_show = int(sys.argv[2]) ):

	movie_list = init_script(10)

	if movie_id > len(movie_list) - 1:
		movie_id = len(movie_list) - 1

	elif movie_id < 0:
		movie_id = 0

	recommended_movies = getMovieRecommedation(movie_list[movie_id - 1], movies_to_show)

	for x in recommended_movies:
		print x.getId(), x.getRating()

	# print map(lambda x: [x.getId(), x.getRating(), map(lambda y: y.getId(), x.getSimilaMovies() )], movie_list)


main()
