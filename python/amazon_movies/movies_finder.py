# Merge Sort Algorithm. merge method
def merge(list1, list2):
	result = []
	i = j = 0

	# It orders the list from greater to smaller '>'
	# run the lists fully
	# insert the next value only if it is bigger than the other and increse the index
	while (i < len(list1) and j < len(list2)):
		if list1[i].getRating() > list2[j].getRating():
			result.append(list1[i])
			i += 1
		else:
			result.append(list2[j])
			j += 1

	# update the result list from the index until the end of each list
	result += list1[i:]
	result += list2[j:]

	return result


# Merge Sort Algorithm. Divide recursive method
def merge_sort_movies(recommended_movies):
	if not recommended_movies or len(recommended_movies) <= 1:
		return recommended_movies

	half = len(recommended_movies)/2
	left = merge_sort_movies(recommended_movies[:half])
	right = merge_sort_movies(recommended_movies[half:])
	return merge(left,right)


# Navigate through all the linked movies
def get_linked_movies(movie, movies_visited, aux_list):
	if movie.getId() in aux_list:
		return
	
	movies_visited.append(movie)
	aux_list.append(movie.getId())
	for movie in movie.getSimilaMovies():
		get_linked_movies(movie, movies_visited, aux_list)

	return movies_visited
	

def getMovieRecommedation(movie, N):
	movies_visited = []
	movies_visited_ids = []
	recommended_movies = get_linked_movies(movie, movies_visited, movies_visited_ids)
	recommended_movies = merge_sort_movies(recommended_movies)

	# Remove the requested movie from the result list
	index = 0
	for movie_x in recommended_movies:
		if movie_x.getId == movie.getId:
			recommended_movies.pop(index)
		index = index + 1

	return recommended_movies[0:N]
