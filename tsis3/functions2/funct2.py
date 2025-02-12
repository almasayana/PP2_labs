movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
def is_imdb_above_5_5(movie):
    return True if movie['imdb'] > 5.5 else False

movie = {
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
}
print(is_imdb_above_5_5(movie)) 
print()


#2
def filter_above_5_5(movies):
    return [movie for movie in movies if movie['imdb'] > 5.5]

movies_above_5_5 = filter_above_5_5(movies)
print("Movies with IMDB above 5.5:")
for movie in movies_above_5_5:
    print(f"{movie['name']} - IMDB: {movie['imdb']}")
print()


#3
def filter_by_category(movies, category):
    return [movie for movie in movies if movie['category'] == category]

romance_movies = filter_by_category(movies, "Suspense")
print("Movies of the selected category:")
for movie in romance_movies:
    print(f"{movie['name']} - IMDB: {movie['imdb']}")
print()


#4
def average_imdb(movies):
    if not movies:
        return 0.0
    total = sum(movie["imdb"] for movie in movies)
    return total / len(movies)

avg_rating = average_imdb(movies)
print(f"Average IMDB score for all movies: {avg_rating:.2f}")
print()


#5

def average_imdb_by_category(movies, category):
    category_movies = filter_by_category(movies, category)
    return average_imdb(category_movies)

category = "Suspense"
avg_romance = average_imdb_by_category(movies, category)
print(f"Average IMDB score for {category} movie: {avg_romance:.2f}")