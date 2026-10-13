import csv
import re

with open("movies.csv", "r") as file:
    movies = list(csv.DictReader(file))

print("All Movie Records:")
for movie in movies:
    print(movie)

mid = input("\nEnter Movie ID to search: ")
found = False

for movie in movies:
    if movie["Movie ID"] == mid:
        print("Movie Found:", movie)
        found = True
        break

if not found:
    print("Movie not found.")

title = input("\nEnter movie title to search: ")
found = False

for movie in movies:
    if re.search(title, movie["Title"], re.IGNORECASE):
        print("Movie Found:", movie)
        found = True

if not found:
    print("Movie title not found.")
