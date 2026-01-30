"""PRACTICE"""
# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

movies = []
user_input = input("Enter your favorite movie: ") # Shortcut : movies.append(input("Enter yourmovie name"))
movies.append(user_input)
user_input = input("Enter your favorite movie: ")
movies.append(user_input)
user_input = input("Enter your favorite movie: ")
movies.append(user_input)
print(movies)

