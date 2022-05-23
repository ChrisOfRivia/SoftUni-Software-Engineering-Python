num_films = int(input())

lowest_rating = 0
lowest_name = 0
highest_name = 0
highest_rating = 0
all_ratings = 0


for each_film in range(num_films):
    name_of_film = input()
    rating_of_film = float(input())
    all_ratings += rating_of_film
    if each_film == 0:
        lowest_rating = rating_of_film
        lowest_name = name_of_film

        highest_rating = rating_of_film
        highest_name = name_of_film
    if each_film > 0:
        if rating_of_film > highest_rating:
            highest_rating = rating_of_film
            highest_name = name_of_film

        if rating_of_film < lowest_rating:
            lowest_rating = rating_of_film
            lowest_name = name_of_film

average_ratings = all_ratings / num_films

print(f"{highest_name} is with highest rating: {highest_rating:.1f}")
print(f"{lowest_name} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average_ratings:.1f}")

