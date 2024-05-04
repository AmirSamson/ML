favorite_movies = ["Dune","Karate Kid","Lego","Sandman"]

favorite_movies.append("Terminator") # For adding a new item to the List we use ".append()"

print(len(favorite_movies)) # for Knowing the length of the List
print(favorite_movies)

favorite_movies.insert(1,"Iron Man") 
# For adding a new item to a spicific place in the List use ".insert(1,"")"
print(favorite_movies)

del(favorite_movies[3]) # For Deleting an item at a spicific place in the List use "del(""[1])"
print(favorite_movies)

del(favorite_movies[0:])
print(favorite_movies)