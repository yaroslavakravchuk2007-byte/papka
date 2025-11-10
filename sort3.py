def count_movie_votes(n, votes):
   
    movie_counts = {}

    for name in votes:
        movie_counts[name] = movie_counts.get(name, 0) + 1

   
    sorted_movies = sorted(movie_counts.items(),
                           key=lambda x: x[1],
                           reverse=True)

    for movie, count in sorted_movies:
        print(movie, count)



n = 6
votes = [
    "Белое солнце пустыни",
    "Бриллиантовая рука",
    "Белое солнце пустыни",
    "Белое солнце пустыни",
    "Гараж",
    "Бриллиантовая рука"
]

count_movie_votes(n, votes)

