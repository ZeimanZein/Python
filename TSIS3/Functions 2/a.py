# Dictionary of movies
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

#Write a function that takes a single movie and returns True if its IMDB score is above 5.5

def single_movie(movie):
    """if(movie["imdb"] > 5.5):
        return True
    else:
        return False
check = single_movie(movies[5])
if(check):
    print("True")
else:
    print("False")"""

    for m in movies:
        if m["name"] == movie and m["imdb"] > 5.5:
            return True
        elif m["name"] == movie and m["imdb"] < 5.5:
            return False
            
check = single_movie("Detective")
if(check):
    print("True")
else:
    print("False")


#Write a function that returns a sublist of movies with an IMDB score above 5.5.

def sublist_movie(movies):
    movies_above = []
    for m in movies:
        if m["imdb"] > 5.5:
            movies_above.append(m["name"])
    return movies_above

movies_above = sublist_movie(movies)
print(movies_above)

#Write a function that takes a category name and returns just those movies under that category.

def return_movie_category(movies,cat_name):
    out_list=[]
    for i in movies:
        curr_cat=i['category']
        if cat_name.lower()==curr_cat.lower():
            out_list.append(i)
    return out_list
out_list = return_movie_category(movies, "Romance")
print(out_list)

"""def movies_category(category):
    movies_category = []
    for m in movies:
        if m["category"] == category:
            movies_category.append(m["name"])
    return movies_category
romance_movies = movies_category("Romance")
print romance_movies
['The Choice', 'Colonia', 'Love', 'Bride Wars', 'We Two']
"""

#Write a function that takes a list of movies and computes the average IMDB score.

def movies_average_score(movies_list):
    movies_scores = []
    for movie in movies_list:
        score = movie["imdb"]
        movies_scores.append(score)
    average_score = sum(movies_scores) / len(movies_scores)
    return average_score

print(movies_average_score(movies))

#Write a function that takes a category and computes the average IMDB score.

def avg_imdb_acc_to_cat(movies,cat_name):
    cat_movies=return_movie_category(movies,cat_name)
    avg_score=avg_imdb_score(cat_movies)
    return avg_score

print(" ")
print("Average IMDB of movies in the Thriller category is: ")
s2=avg_imdb_acc_to_cat(movies,'Thriller')
print(s2)